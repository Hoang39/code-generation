"""chatml_v9.2.1 = chatml_v9 + the 135 augmentation rows of chatml_he_failed_v9.2_aug (no HumanEval rows).
Checks that every row fits MAX_SEQ_LENGTH = 512 tokens, that the rows are unique and that v9 is unchanged.
Usage: .venv/bin/python src/dataset/he_aug_v10/make_v9_2_1.py
"""
import json
import os
import sys

from transformers import AutoTokenizer

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
V9 = os.path.join(ROOT, "opencode_hq", "chatml_v9.jsonl")
AUG = os.path.join(ROOT, "opencode_hq", "chatml_he_failed_v9.2_aug.jsonl")
OUT = os.path.join(ROOT, "opencode_hq", "chatml_v9.2.1.jsonl")
MAX_SEQ_LENGTH = 512  # same value as the fine-tune notebook

tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-7B")
v9 = [json.loads(l)["text"] for l in open(V9)]
aug = [json.loads(l)["text"] for l in open(AUG)]
rows = v9 + aug
n = [len(tok(t, add_special_tokens=False)["input_ids"]) for t in rows]
over = [(i, k) for i, k in enumerate(n) if k > MAX_SEQ_LENGTH]
print(f"rows {len(rows)} (v9 {len(v9)} + aug {len(aug)}) | duplicates {len(rows) - len(set(rows))}")
print(f"tokens: v9 max {max(n[:len(v9)])}, aug max {max(n[len(v9):])}, all rows max {max(n)}, rows > {MAX_SEQ_LENGTH}: {len(over)}")
if over or len(rows) != len(set(rows)):
    print("not written:", over[:10])
    sys.exit(1)
with open(OUT, "w") as f:
    for t in rows:
        f.write(json.dumps({"text": t}, ensure_ascii=False) + "\n")
print("wrote", OUT)
