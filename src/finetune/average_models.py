"""Linear weight averaging of two merged checkpoints that share the same base (model soup).

    out = (1 - alpha) * A + alpha * B        # alpha = 0.5 by default

Both inputs must be full (merged) models with identical architecture and tensor names, e.g. the outputs of
merge_lora.py. Tensors are streamed shard by shard (safetensors, lazy), so peak RAM is about one shard, not two models.
Tokenizer / generation_config / config are taken from A (--tokenizer-from B to override).

Usage:
    python src/finetune/average_models.py \
        --a hoangnh39/qwen2.5-coder-7b-opencode-v7-merged \
        --b hoangnh39/qwen2.5-coder-7b-opencode-v9.1-merged \
        --alpha 0.5 --out merged/soup-v7-v9.1 --tokenizer-from b \
        --push-to hoangnh39/qwen2.5-coder-7b-opencode-soup-v7-v9.1-merged   # --push-to optional

The tokenizer and generation_config should come from the model whose end-of-turn format you want to keep:
v9.1 ends every answer with "```\\n<|im_end|>", v7 with "```<|im_end|>"; check the stop behaviour after averaging.
"""
import argparse
import json
import os
import shutil

import torch
from huggingface_hub import HfApi, snapshot_download
from safetensors import safe_open
from safetensors.torch import save_file

SIDE_FILES = ["config.json", "generation_config.json", "tokenizer.json", "tokenizer_config.json",
              "vocab.json", "merges.txt", "special_tokens_map.json", "added_tokens.json", "chat_template.jinja"]


def local_dir(path_or_repo):
    if os.path.isdir(path_or_repo):
        return path_or_repo
    return snapshot_download(path_or_repo, allow_patterns=["*.safetensors", "*.json", "*.txt", "*.jinja"])


def shard_files(d):
    idx = os.path.join(d, "model.safetensors.index.json")
    if os.path.exists(idx):
        wm = json.load(open(idx))["weight_map"]
        return sorted(set(wm.values())), wm
    return ["model.safetensors"], None


def tensor_map(d):
    """tensor name -> shard file for a checkpoint directory."""
    files, wm = shard_files(d)
    if wm is not None:
        return wm
    with safe_open(os.path.join(d, files[0]), "pt") as f:
        return {k: files[0] for k in f.keys()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="HF repo or local dir of merged model A")
    ap.add_argument("--b", required=True, help="HF repo or local dir of merged model B")
    ap.add_argument("--alpha", type=float, default=0.5, help="weight of B (0 = A, 1 = B)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tokenizer-from", choices=["a", "b"], default="a")
    ap.add_argument("--push-to")
    args = ap.parse_args()
    assert 0.0 <= args.alpha <= 1.0

    da, db = local_dir(args.a), local_dir(args.b)
    ma, mb = tensor_map(da), tensor_map(db)
    assert set(ma) == set(mb), f"tensor names differ: only in A {sorted(set(ma) - set(mb))[:5]}, only in B {sorted(set(mb) - set(ma))[:5]}"
    os.makedirs(args.out, exist_ok=True)

    files_a, _ = shard_files(da)
    new_map, total, nbytes, max_rel = {}, 0, 0, 0.0
    for shard in files_a:
        out_tensors = {}
        with safe_open(os.path.join(da, shard), "pt") as fa:
            for name in fa.keys():
                ta = fa.get_tensor(name)
                with safe_open(os.path.join(db, mb[name]), "pt") as fb:
                    tb = fb.get_tensor(name)
                assert ta.shape == tb.shape and ta.dtype == tb.dtype, f"{name}: {ta.shape}/{ta.dtype} vs {tb.shape}/{tb.dtype}"
                mix = ((1 - args.alpha) * ta.float() + args.alpha * tb.float()).to(ta.dtype)
                diff = (ta.float() - tb.float()).norm() / (ta.float().norm() + 1e-12)
                max_rel = max(max_rel, diff.item())
                out_tensors[name] = mix.contiguous()
                new_map[name] = shard
                total += ta.numel()
                nbytes += ta.numel() * ta.element_size()
        save_file(out_tensors, os.path.join(args.out, shard), metadata={"format": "pt"})
        print("wrote", shard, len(out_tensors), "tensors")
        del out_tensors

    if len(files_a) > 1 or os.path.exists(os.path.join(da, "model.safetensors.index.json")):
        json.dump({"metadata": {"total_size": nbytes}, "weight_map": new_map},
                  open(os.path.join(args.out, "model.safetensors.index.json"), "w"), indent=1)
    side = da if args.tokenizer_from == "a" else db
    for fn in SIDE_FILES:
        src = os.path.join(side, fn)
        if os.path.exists(src):
            shutil.copy(src, args.out)
    print(f"averaged {total / 1e9:.2f}B params, alpha={args.alpha}, largest per-tensor relative distance A-B: {max_rel:.4f}")
    print("saved to", args.out)

    if args.push_to:
        api = HfApi()
        api.create_repo(args.push_to, private=True, exist_ok=True)
        api.upload_folder(repo_id=args.push_to, folder_path=args.out, commit_message=f"Weight average alpha={args.alpha}")
        print("pushed to https://huggingface.co/" + args.push_to)


if __name__ == "__main__":
    main()
