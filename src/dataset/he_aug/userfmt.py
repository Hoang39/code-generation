"""Build a chatml_v5-style user prompt (description / Input / Output / Sample Input / Sample Output)
from a problem's prompt docstring. Sample outputs are produced by running the validated solution."""
import ast, re, signal, types

MARK = re.compile(r"^\s*(>>>|Examples?\b|For example|for example|\[input/output\]|Input:|operator\s*\[)")
NOTE = re.compile(r"^\s*(Notes?|Constraints?)\s*:?\s*$|^\s*(Notes?|Constraints?)\s*:\s*\S")


def _target(prompt):
    tree = ast.parse(prompt.rstrip("\n") + "\n    pass\n")
    defs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    return defs[-1], defs[:-1]


def _split_doc(doc):
    lines = doc.split("\n")
    cut = next((i for i, l in enumerate(lines) if MARK.match(l)), len(lines))
    desc_lines = lines[:cut]
    notes = []
    # a Note/Constraints section that follows the examples
    for j in range(cut, len(lines)):
        if NOTE.match(lines[j]):
            first = re.sub(r"^\s*(Notes?|Constraints?)\s*:?\s*", "", lines[j])
            notes = ([first] if first else []) + lines[j + 1:]
            break
    # a Note section before the examples stays in description unless it is the last block
    return desc_lines, notes


def _bullets(lines):
    out = []
    for l in lines:
        s = l.strip()
        if not s:
            continue
        m = re.match(r"^\d+\.\s*(.*)$", s)
        if m:
            out.append(m.group(1))
        elif out and not out[-1].endswith((".", ":", "]", ")")):
            out[-1] += " " + s
        else:
            out.append(s)
    return out


def _clean_desc(lines):
    text = "\n".join(l.rstrip() for l in lines).strip("\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _call_candidates(doc, name, params):
    cands = []
    for m in re.finditer(r"\b" + re.escape(name) + r"\(", doc):
        i, depth = m.end(), 1
        while i < len(doc) and depth:
            c = doc[i]
            if c in "([{":
                depth += 1
            elif c in ")]}":
                depth -= 1
            i += 1
        if depth:
            continue
        call = doc[m.start():i]
        try:
            node = ast.parse(call, mode="eval").body
            args = [ast.literal_eval(a) for a in node.args]
            kws = {k.arg: ast.literal_eval(k.value) for k in node.keywords}
            kw = dict(zip(params, args))
            kw.update(kws)
            if len(kw) == len(params):
                cands.append(kw)
        except Exception:
            continue
    return cands


def _input_candidates(doc, params):
    cands = []
    for line in doc.split("\n"):
        s = line.strip()
        if s.startswith("Input:"):
            body = re.sub(r"\s+#.*$", "", s[len("Input:"):].strip())
            try:
                node = ast.parse("f(" + body + ")", mode="eval").body
                kw = {k.arg: ast.literal_eval(k.value) for k in node.keywords}
                if set(kw) == set(params):
                    cands.append(kw)
            except Exception:
                pass
    return cands


def _assign_candidates(doc, params):
    cands, cur = [], {}
    for line in doc.split("\n"):
        m = re.match(r"^\s*(\w+)\s*=\s*(.+?)\s*$", line)
        if m and m.group(1) in params:
            try:
                cur[m.group(1)] = ast.literal_eval(m.group(2))
            except Exception:
                cur = {}
                continue
            if len(cur) == len(params):
                cands.append(cur)
                cur = {}
    return cands


def _kind(v):
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, int):
        return "int"
    if isinstance(v, float):
        return "float"
    if isinstance(v, str):
        return "str"
    if isinstance(v, list):
        return "list"
    if isinstance(v, tuple):
        return "tuple"
    if isinstance(v, dict):
        return "dict"
    if v is None:
        return "none"
    return "other"


def _elem_desc(vals):
    kinds = {_kind(v) for v in vals}
    if kinds <= {"int"}:
        return "integers"
    if kinds <= {"int", "float"}:
        return "numbers"
    if kinds == {"str"}:
        return "strings"
    if kinds == {"bool"}:
        return "booleans"
    if kinds == {"tuple"}:
        inner = [x for t in vals for x in t]
        return "tuples of " + (_elem_desc(inner) if inner else "values")
    if kinds == {"list"}:
        inner = [x for t in vals for x in t]
        return "lists of " + (_elem_desc(inner) if inner else "values")
    return "values of mixed types"


def describe(values):
    """Describe a value type, using all candidate values (first non-empty container wins)."""
    kinds = [_kind(v) for v in values]
    k = kinds[0]
    if k == "bool":
        return "A boolean."
    if k == "int":
        return "An integer."
    if k == "float":
        return "A floating-point number."
    if k == "str":
        return "A string."
    if k == "dict":
        return "A dictionary."
    if k == "none":
        return "`None`."
    if k in ("list", "tuple"):
        noun = "list" if k == "list" else "tuple"
        pool = [v for v in values if _kind(v) == k and v]
        if not pool:
            return f"A {noun}."
        return f"A {noun} of {_elem_desc(pool[0])}."
    return "A value."


class _Timeout(Exception):
    pass


def _alarm(*a):
    raise _Timeout()


def _run(code, name, kw):
    mod = types.ModuleType("sol")
    exec(compile(code, "sol", "exec"), mod.__dict__)
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(5)
    try:
        return getattr(mod, name)(**{k: (list(v) if isinstance(v, list) else v) for k, v in kw.items()})
    finally:
        signal.alarm(0)


def _fmt_out(v):
    if v is None or isinstance(v, (bool, int, float)):
        return repr(v)
    return repr(v)


def build_user(prompt, code, override=None):
    fn, helpers = _target(prompt)
    name = fn.name
    params = [a.arg for a in fn.args.args]
    doc = ast.get_docstring(fn) or ""
    desc_lines, notes = _split_doc(doc)
    desc = _clean_desc(desc_lines)
    cands = _call_candidates(doc, name, params)
    if not cands:
        cands = _input_candidates(doc, params)
    if not cands:
        cands = _assign_candidates(doc, params)
    seen, uniq = set(), []
    for c in cands:
        key = repr(sorted(c.items()))
        if key not in seen:
            seen.add(key)
            uniq.append(c)
    cands = uniq
    results = []
    for c in cands:
        try:
            results.append(_run(code, name, c))
        except Exception:
            results.append(Ellipsis)
    good = [(c, r) for c, r in zip(cands, results) if r is not Ellipsis]
    if not good:
        raise ValueError(f"no samples for {name}")
    picked = [good[0]]
    for c, r in good[1:]:
        if repr(r) != repr(good[0][1]):
            picked.append((c, r))
            break
    sig = f"{name}({', '.join(params)})"
    parts = [f"You are tasked with implementing a function `{sig}`."]
    if desc:
        parts.append(desc)
    for h in helpers:
        hd = ast.get_docstring(h) or ""
        hl, _ = _split_doc(hd)
        hdesc = " ".join(x.strip() for x in _clean_desc(hl).split("\n") if x.strip())
        hs = f"{h.name}({', '.join(a.arg for a in h.args.args)})"
        parts.append(f"The helper function `{hs}` is also part of the solution: {hdesc}")
    text = "\n\n".join(parts)
    text += "\n\n**Input:**\n"
    ann = {a.arg: ast.unparse(a.annotation) for a in fn.args.args if a.annotation is not None}
    for p in params:
        d = describe([c[p] for c in cands])
        if ann.get(p) == "float" and _kind(cands[0][p]) == "int":
            d = "A floating-point number."
        text += f"- `{p}`: {d}\n"
    text += "\n**Output:**\n"
    outs = [r for _, r in good]
    od = describe(outs)
    if _kind(outs[0]) == "bool":
        od = "A boolean (`True` or `False`)."
    elif outs[0] is None and fn.returns is not None:
        od = f"A value of type `{ast.unparse(fn.returns)}`."
    text += f"- {od}\n"
    nb = _bullets(notes)
    if nb:
        text += "\n**Constraints:**\n" + "".join(f"- {b}\n" for b in nb)
    for c, r in picked:
        text += "\n**Sample Input:**\n```python\n" + "\n".join(f"{p} = {c[p]!r}" for p in params) + "\n```\n"
        text += "\n**Sample Output:**\n```\n" + _fmt_out(r) + "\n```\n"
    return text.rstrip("\n")
