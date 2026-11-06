"""Build augmented dataset: validate every generated problem (doctest + asserts + timeout + AST), count tokens, write jsonl.

Usage: .venv/bin/python src/dataset/he_aug/build.py [--out PATH] [--only N]
Each batchN.py exposes PROBLEMS = [dict(parent=int, prompt=str, body=str, tests=str)].
"""
import argparse, ast, importlib, json, os, subprocess, sys, tempfile, textwrap
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
import userfmt
SRC_FILE = os.path.join(ROOT, "opencode_hq", "chatml_he_failed_v5.jsonl")
SYS = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
USER_HEAD = "Please provide a self-contained Python script that solves the following problem in a markdown code block:"
TIME_LIMIT = 20

RUNNER = r'''
import sys, types, doctest, time, resource
resource.setrlimit(resource.RLIMIT_AS, (3 << 30, 3 << 30))
sys.setrecursionlimit(1000)
sol, tests = sys.argv[1], sys.argv[2]
mod = types.ModuleType("solution"); sys.modules["solution"] = mod
exec(compile(open(sol).read(), sol, "exec"), mod.__dict__)
r = doctest.testmod(mod, verbose=False)
assert r.failed == 0, "doctest failed"
t0 = time.time()
exec(compile(open(tests).read(), tests, "exec"), mod.__dict__)
dt = time.time() - t0
assert dt < 5, "tests too slow: %.2fs" % dt
print("OK %.2f doctests=%d" % (dt, r.attempted))
'''


def full_code(p):
    return p["prompt"].rstrip("\n") + "\n\n" + p["body"].strip("\n")


def prompt_defs(prompt):
    return [n.name for n in ast.parse(prompt.rstrip("\n") + "\n    pass\n").body if isinstance(n, ast.FunctionDef)]


def static_check(p, code):
    errs = []
    tree = ast.parse(code)
    defs = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
    for n in prompt_defs(p["prompt"]):
        if n not in defs:
            errs.append(f"missing def {n}")
    for n in tree.body:
        if not isinstance(n, (ast.FunctionDef, ast.Import, ast.ImportFrom)):
            errs.append(f"top-level stmt {type(n).__name__}")
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("input", "print", "open", "exec"):
            errs.append(f"forbidden call {n.func.id}")
    return errs


def check(i_p):
    i, p = i_p
    code = full_code(p)
    errs = []
    try:
        errs += static_check(p, code)
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
                errs.append("RUN FAIL: " + (r.stderr[-700:] or r.stdout[-300:]))
        except subprocess.TimeoutExpired:
            errs.append("TIMEOUT")
        # run as plain script: must be silent + fast
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
    ap.add_argument("--out", default=os.path.join(ROOT, "opencode_hq", "chatml_he_failed_v5_aug.jsonl"))
    ap.add_argument("--only", default="", help="comma list of batch names, validate only (no write)")
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
                fn = ast.parse(full_code(probs[i])).body
                nm = [n.name for n in fn if isinstance(n, ast.FunctionDef)]
                print(f"--- FAIL #{i} {probs[i]['batch']} parent={probs[i]['parent']} {nm}")
                for e in errs:
                    print("   ", e)
    print("failed:", bad)
    if bad or a.only or a.no_write:
        return 1 if bad else 0
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-7B")
    old = [json.loads(l) for l in open(SRC_FILE)]
    seen = {o["text"] for o in old}
    seen_names, out, lens, per_parent = set(), [], [], {}
    over = 0
    for p in probs:
        t = to_text(p)
        names_ = tuple(n.name for n in ast.parse(full_code(p)).body if isinstance(n, ast.FunctionDef))
        if t in seen or names_ in seen_names:
            print("DUP", names_); continue
        seen.add(t); seen_names.add(names_)
        L = len(tok(t, add_special_tokens=False)["input_ids"])
        if L >= 1024:
            over += 1; print("OVER", L, names_); continue
        lens.append(L); out.append({"text": t}); per_parent[p["parent"]] = per_parent.get(p["parent"], 0) + 1
    print("kept", len(out), "over", over, "max tokens", max(lens), "mean", sum(lens) / len(lens))
    print("per parent", dict(sorted(per_parent.items())))
    if over:
        return 1
    with open(a.out, "w") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    print("wrote", a.out, len(out))


if __name__ == "__main__":
    sys.exit(main())
