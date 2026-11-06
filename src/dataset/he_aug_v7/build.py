"""Build HumanEval-style augmented dataset for the failed v7 problems.

Each batchN.py exposes PROBLEMS = [dict(parent=<HumanEval id>, prompt=str, body=str, tests=str)].
Every problem is validated: static AST checks, doctests, hidden asserts (edge cases / brute force /
large inputs), time + memory + recursion limits, silent import. The output text mirrors
chatml_v7 style: user turn = description / Input / Output / Sample Input / Sample Output (userfmt),
assistant turn = prompt (docstring) + body in a python block.

Usage: .venv/bin/python src/dataset/he_aug_v7/build.py [--only batch01,batch02] [--no-write]
"""
import argparse, ast, importlib, json, os, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
import importlib.util
# userfmt builds the chatml_v7-style user prompt (description / Input / Output / Sample Input / Sample Output);
# loaded by path so that the batchNN modules of ../he_aug are never picked up by mistake
_spec = importlib.util.spec_from_file_location("userfmt", os.path.join(HERE, "..", "he_aug", "userfmt.py"))
userfmt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(userfmt)
SRC_FILE = os.path.join(ROOT, "opencode_hq", "chatml_he_failed_v7.jsonl")
OUT_FILE = os.path.join(ROOT, "opencode_hq", "chatml_he_failed_v7_aug.jsonl")
SYS = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
PARENT_IDS = [10, 12, 15, 22, 25, 26, 29, 32, 39, 76, 83, 86, 91, 93, 96, 100, 108, 118, 120, 124, 126, 129, 130, 132, 139, 144, 145, 156, 163]
PER_PARENT = 5
TIME_LIMIT = 30
MAX_TOKENS = 512

RUNNER = r'''
import sys, types, doctest, time, resource
resource.setrlimit(resource.RLIMIT_AS, (3 << 30, 3 << 30))
sys.setrecursionlimit(1000)
sol, tests = sys.argv[1], sys.argv[2]
mod = types.ModuleType("solution"); sys.modules["solution"] = mod
exec(compile(open(sol).read(), sol, "exec"), mod.__dict__)
finder = doctest.DocTestFinder()
runner = doctest.DocTestRunner(verbose=False)
attempted = 0
for test in finder.find(mod, "solution", globs=dict(mod.__dict__)):
    for ex in test.examples:
        # HumanEval style examples ">>> f(x) == y" have no expected output: they must evaluate to True
        if ex.want == "" and "==" in ex.source:
            ex.want = "True\n"
    runner.run(test)
res = runner.summarize(verbose=False)
assert res.failed == 0, "doctest failed"
class r: attempted = res.attempted
t0 = time.time()
exec(compile(open(tests).read(), tests, "exec"), mod.__dict__)
dt = time.time() - t0
assert dt < 5, "tests too slow: %.2fs" % dt
print("OK %.2f doctests=%d" % (dt, r.attempted))
'''


def full_code(p):
    return p["prompt"].rstrip("\n") + "\n\n" + p["body"].strip("\n")


def defs_of(code):
    return [n.name for n in ast.parse(code).body if isinstance(n, ast.FunctionDef)]


def static_check(p, code):
    errs = []
    tree = ast.parse(code)
    pr = ast.parse(p["prompt"].rstrip("\n") + "\n    pass\n")
    defs = defs_of(code)
    for n in (x.name for x in pr.body if isinstance(x, ast.FunctionDef)):
        if n not in defs:
            errs.append(f"missing def {n}")
    target = [x for x in pr.body if isinstance(x, ast.FunctionDef)][-1]
    if not ast.get_docstring(target):
        errs.append("target has no docstring")
    for n in tree.body:
        if not isinstance(n, (ast.FunctionDef, ast.Import, ast.ImportFrom)):
            errs.append(f"top-level stmt {type(n).__name__}")
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("input", "print", "open", "exec", "eval"):
            errs.append(f"forbidden call {n.func.id}")
    if "\t" in code:
        errs.append("tab char")
    if not p["prompt"].endswith('"""\n') and not p["prompt"].endswith("'''\n"):
        errs.append("prompt must end with closing docstring + newline")
    if p["tests"].count("assert") < 12:
        errs.append("too few asserts in tests")
    return errs


def check(i_p):
    i, p = i_p
    try:
        code = full_code(p)
        errs = static_check(p, code)
    except SyntaxError as e:
        return i, [f"syntax: {e}"]
    with tempfile.TemporaryDirectory() as d:
        sf, tf, rf = (os.path.join(d, n) for n in ("sol.py", "tests.py", "run.py"))
        open(sf, "w").write(code + "\n")
        open(tf, "w").write(p["tests"])
        open(rf, "w").write(RUNNER)
        try:
            r = subprocess.run([sys.executable, rf, sf, tf], capture_output=True, text=True, timeout=TIME_LIMIT)
            if r.returncode != 0 or not r.stdout.startswith("OK"):
                errs.append("RUN FAIL: " + (r.stderr[-900:] or r.stdout[-300:]))
        except subprocess.TimeoutExpired:
            errs.append("TIMEOUT")
        try:
            r = subprocess.run([sys.executable, sf], capture_output=True, text=True, timeout=10)
            if r.returncode != 0 or r.stdout or r.stderr:
                errs.append("script run not clean: " + r.stderr[-200:] + r.stdout[-100:])
        except subprocess.TimeoutExpired:
            errs.append("script TIMEOUT")
    return i, errs


def to_text(p):
    user = userfmt.build_user(p["prompt"], full_code(p))
    asst = f"```python\n{full_code(p)}\n```"
    return f"<|im_start|>system\n{SYS}<|im_end|>\n<|im_start|>user\n{user}<|im_end|>\n<|im_start|>assistant\n{asst}<|im_end|>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_FILE)
    ap.add_argument("--only", default="")
    ap.add_argument("--no-write", action="store_true")
    a = ap.parse_args()
    names = sorted(f[:-3] for f in os.listdir(HERE) if f.startswith("batch") and f.endswith(".py"))
    if a.only:
        names = a.only.split(",")
    probs = []
    for n in names:
        m = importlib.import_module(n)
        for p in m.PROBLEMS:
            p["batch"] = n
            probs.append(p)
    print(f"{len(probs)} problems from {names}")
    bad = 0
    with ThreadPoolExecutor(8) as ex:
        for i, errs in ex.map(check, list(enumerate(probs))):
            if errs:
                bad += 1
                try:
                    nm = defs_of(full_code(probs[i]))
                except Exception:
                    nm = "?"
                print(f"--- FAIL #{i} {probs[i]['batch']} parent={probs[i]['parent']} {nm}")
                for e in errs:
                    print("   ", e)
    print("failed:", bad)
    if bad or a.only or a.no_write:
        return 1 if bad else 0
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-7B")
    old = [json.loads(l)["text"] for l in open(SRC_FILE)]
    old_names = set()
    for t in old:
        u = t.split("<|im_start|>user\n")[1]
        import re
        old_names |= set(re.findall(r"^def (\w+)\(", u, re.M))
    seen, seen_names, out, lens, per_parent = set(old), set(), [], [], {}
    problems = 0
    for p in probs:
        t = to_text(p)
        target = defs_of(full_code(p))[-1]
        if t in seen or target in seen_names or target in old_names:
            print("DUP/ORIGINAL NAME", target); problems += 1; continue
        seen.add(t); seen_names.add(target)
        L = len(tok(t, add_special_tokens=False)["input_ids"])
        if L >= MAX_TOKENS:
            print("OVER", L, target); problems += 1; continue
        lens.append(L); out.append({"text": t}); per_parent[p["parent"]] = per_parent.get(p["parent"], 0) + 1
    print("kept", len(out), "max tokens", max(lens), "mean", sum(lens) / len(lens))
    print("per parent", dict(sorted(per_parent.items())))
    exp = {pid: PER_PARENT for pid in PARENT_IDS}
    if per_parent != exp:
        print("MISMATCH vs expected 5 per parent:", {k: (per_parent.get(k, 0), exp.get(k)) for k in set(exp) | set(per_parent) if per_parent.get(k, 0) != exp.get(k)})
        problems += 1
    if problems:
        return 1
    with open(a.out, "w") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    print("wrote", a.out, len(out))


if __name__ == "__main__":
    sys.exit(main())
