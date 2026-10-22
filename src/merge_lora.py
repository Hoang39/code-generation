"""Merge a LoRA adapter into the fp16/bf16 base model so vLLM / EvalPlus can load it directly.

Usage:
    python src/merge_lora.py --adapter hoangnh39/qwen2.5-coder-7b-opencode-hq10k-v3 \
        --base Qwen/Qwen2.5-Coder-7B --out merged/v3
"""
import argparse
import json

import torch
from huggingface_hub import hf_hub_download
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--adapter", required=True)
    ap.add_argument("--base", default="Qwen/Qwen2.5-Coder-7B")
    ap.add_argument("--revision", default=None)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    # Unsloth adapters often point at a 4-bit base (unsloth/...-bnb-4bit); merging must use the full-precision base.
    cfg = json.load(open(hf_hub_download(args.adapter, "adapter_config.json", revision=args.revision)))
    print("adapter base_model_name_or_path:", cfg.get("base_model_name_or_path"), "| merging onto:", args.base)

    base = AutoModelForCausalLM.from_pretrained(args.base, torch_dtype=torch.bfloat16, device_map="cpu")
    model = PeftModel.from_pretrained(base, args.adapter, revision=args.revision)
    model = model.merge_and_unload()
    model.save_pretrained(args.out, safe_serialization=True)

    tok = AutoTokenizer.from_pretrained(args.adapter, revision=args.revision)
    if not tok.chat_template:
        tok.chat_template = AutoTokenizer.from_pretrained(args.base).chat_template
        print("adapter tokenizer had no chat_template; copied from base")
    tok.save_pretrained(args.out)
    print("saved to", args.out)


if __name__ == "__main__":
    main()
