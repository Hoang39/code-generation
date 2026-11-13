"""Build chatml_v10 = chatml_v9 + the HumanEval problems that v9.1 / v9.2 get wrong.

The added rows copy the format of the rows already in chatml_v9 (nothing new is invented):
  user      = userfmt.build_user(...)  -> "You are tasked with implementing a function `f(x)`." / description /
              **Input:** / **Output:** / [**Constraints:**] / **Sample Input:** / **Sample Output:**
              (the same layout as the 1.6k "You are tasked with ..." rows of chatml_v9)
  assistant = "```python\n<prompt + canonical solution>\n```\n<|im_end|>"   (v9 ending: fence, newline, <|im_end|>)
  system    = the default Qwen system prompt, as in every v9 row.

Failed set = HumanEval/HumanEval+ failures of v9.1 and v9.2 on Kaggle (data/chatml-v9.{1,2}-merged-eval-results.json),
minus the three problems that fail on Kaggle for every model (15, 100, 139): their solutions are correct locally,
so they are not model errors.

NOTE: the added rows contain HumanEval prompts + canonical solutions, so HumanEval is no longer a clean test for a
model trained on chatml_v10. Read the result as "effect of training on the failed problems", not as a clean score.

Usage: .venv/bin/python src/dataset/he_v10/build.py [--repeat N] [--dry-run]
"""
import argparse
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SYS = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
KAGGLE_ONLY = {15, 100, 139}
RESULTS = [os.path.join(ROOT, "data", f"chatml-v9.{k}-merged-eval-results.json") for k in (1, 2)]
V9 = os.path.join(ROOT, "opencode_hq", "chatml_v9.jsonl")
V7_FAILED = os.path.join(ROOT, "opencode_hq", "chatml_he_failed_v7.jsonl")
OUT_FAILED = os.path.join(ROOT, "opencode_hq", "chatml_he_failed_v9.2.jsonl")
OUT_V10 = os.path.join(ROOT, "opencode_hq", "chatml_v10.jsonl")

_spec = importlib.util.spec_from_file_location("userfmt", os.path.join(HERE, "..", "he_aug", "userfmt.py"))
userfmt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(userfmt)


# userfmt finds the sample calls by parsing the docstring; these four docstrings have none it can parse
# (examples written as "Input: [..]" / "grid : [..]" / "operator[...]"), so the samples are copied from their examples.
MANUAL_SAMPLES = {
    68: [dict(arr=[4, 2, 3]), dict(arr=[])],
    83: [dict(n=1), dict(n=2)],
    115: [dict(grid=[[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], capacity=1), dict(grid=[[0, 0, 0], [0, 0, 0]], capacity=5)],
    160: [dict(operator=["+", "*", "-"], operand=[2, 3, 4, 5]), dict(operator=["**", "//"], operand=[2, 3, 2])],
}


def failed_ids():
    fails = {}
    for path in RESULTS:
        ev = json.load(open(path))["eval"]
        for task, samples in ev.items():
            s = samples[0]
            if not (s["base_status"] == "pass" and s["plus_status"] == "pass"):
                fails.setdefault(int(task.split("/")[1]), []).append(os.path.basename(path)[8:12])
    return fails


def full_code(problem):
    return (problem["prompt"] + problem["canonical_solution"]).strip("\n")


_orig_bullets = userfmt._bullets


def _bullets_star(lines):
    """userfmt._bullets glues "* a" / "* b" lines into one bullet; keep one bullet per "* " line instead."""
    if any(l.strip().startswith("* ") for l in lines):
        return [l.strip()[2:].strip() for l in lines if l.strip().startswith("* ")]
    return _orig_bullets(lines)


def to_text(problem, task_id=None):
    code = full_code(problem)
    orig = userfmt._call_candidates
    userfmt._bullets = _bullets_star
    if task_id in MANUAL_SAMPLES:
        userfmt._call_candidates = lambda doc, name, params: [dict(c) for c in MANUAL_SAMPLES[task_id]]
    try:
        user = userfmt.build_user(problem["prompt"].strip("\n") + "\n", code)
    finally:
        userfmt._call_candidates = orig
        userfmt._bullets = _orig_bullets
    return (f"<|im_start|>system\n{SYS}<|im_end|>\n<|im_start|>user\n{user}<|im_end|>\n"
            f"<|im_start|>assistant\n```python\n{code}\n```\n<|im_end|>")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repeat", type=int, default=1, help="copies of each added row (default 1)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    from evalplus.data import get_human_eval_plus
    problems = get_human_eval_plus()

    fails = failed_ids()
    ids = sorted(set(fails) - KAGGLE_ONLY)
    print(f"{len(fails)} problems fail in v9.1 or v9.2; {len(ids)} kept after dropping {sorted(KAGGLE_ONLY & set(fails))}")

    # sanity check: same code convention as the v7 failed file (the assistant answer is identical for the shared ids)
    v7 = {}
    for line in open(V7_FAILED):
        t = json.loads(line)["text"]
        code = t.split("<|im_start|>assistant\n```python\n")[1].rsplit("\n```", 1)[0]
        v7[code] = True
    shared = [i for i in ids if full_code(problems[f"HumanEval/{i}"]) in v7]
    print(f"{len(shared)}/{len(ids)} answers identical to rows of chatml_he_failed_v7.jsonl")
    assert len(shared) >= 20, "code convention differs from chatml_he_failed_v7.jsonl"

    rows, bad = [], []
    for i in ids:
        try:
            rows.append((i, to_text(problems[f"HumanEval/{i}"], i)))
        except Exception as e:  # noqa: BLE001
            bad.append((i, repr(e)))
    for i, e in bad:
        print(f"!! HumanEval/{i}: cannot build user turn: {e}")
    if bad:
        return 1

    v9 = [json.loads(l)["text"] for l in open(V9)]
    assert all(t.endswith("```\n<|im_end|>") for t in rows_text(rows)), "ending differs from v9"
    existing = set(v9)
    assert not any(t in existing for t in rows_text(rows)), "added row already in v9"
    print(f"built {len(rows)} rows; v9 has {len(v9)} -> v10 will have {len(v9) + len(rows) * args.repeat}")
    if args.dry_run:
        return 0
    with open(OUT_FAILED, "w") as f:
        for i, t in rows:
            f.write(json.dumps({"text": t}, ensure_ascii=False) + "\n")
    with open(OUT_V10, "w") as f:
        for t in v9:
            f.write(json.dumps({"text": t}, ensure_ascii=False) + "\n")
        for _ in range(args.repeat):
            for i, t in rows:
                f.write(json.dumps({"text": t}, ensure_ascii=False) + "\n")
    print("wrote", OUT_FAILED, "and", OUT_V10)
    print("ids:", ids)
    return 0


def rows_text(rows):
    return [t for _, t in rows]


if __name__ == "__main__":
    sys.exit(main())
