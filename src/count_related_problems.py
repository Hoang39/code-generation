"""Với mỗi case HumanEval fail của model base, đếm số bài "liên quan" trong một nguồn dữ liệu.

Bài liên quan = đề (cột `input` của nvidia/OpenCodeInstruct) chứa ít nhất 1 keyword của case fail,
so khớp không phân biệt hoa/thường theo substring (nên "bore" khớp cả "bored").
Keyword lấy từ data/base_humaneval_fewshot_failed_keywords.md.

Nguồn (--source):
    nvidia     (mặc định) toàn bộ nvidia/OpenCodeInstruct (~5M mẫu), duyệt streaming, chỉ đọc cột `input`
    local      10K mẫu high-quality đã lọc sẵn trong opencode_hq/raw (dùng để thử nhanh)
    humaneval  164 đề HumanEval (không tính chính case đó vào số bài liên quan)

Chạy:
    python3 src/count_related_problems.py --limit 20000        # thử nhanh trên 20K mẫu đầu
    python3 src/count_related_problems.py                      # toàn bộ nvidia/OpenCodeInstruct
    python3 src/count_related_problems.py --source local --out data/keyword_related_counts.md

Ctrl+C khi đang chạy nguồn nvidia vẫn in/ghi kết quả của phần đã duyệt.
"""
import argparse
import re
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KEYWORDS = ROOT / "data" / "base_humaneval_fewshot_failed_keywords.md"
LOCAL_RAW = ROOT / "opencode_hq" / "raw"
NVIDIA_ID = "nvidia/OpenCodeInstruct"

LINE_RE = re.compile(r"^-\s+(HumanEval/\d+)\s+`([^`]+)`:\s*(.+?)\s*$")


def parse_keywords(path):
    """{task_id: (task_name, [keyword, ...])} theo thứ tự trong file."""
    cases = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = LINE_RE.match(line)
        if not m:
            continue
        task_id, name, kws = m.groups()
        cases[task_id] = (name, [k.strip() for k in kws.split(",") if k.strip()])
    return cases


def iter_texts(source, limit):
    """Sinh (id, text) của từng bài trong nguồn; id dùng để loại case khỏi chính nó (chỉ humaneval)."""
    try:
        from datasets import load_dataset, load_from_disk
    except ImportError:
        raise SystemExit("Thiếu thư viện `datasets`. Cài bằng: python3 -m pip install datasets")
    if source == "nvidia":
        stream = load_dataset(NVIDIA_ID, split="train", streaming=True)
        for i, ex in enumerate(stream):
            if limit and i >= limit:
                return
            yield None, ex["input"] or ""
    elif source == "local":
        ds = load_from_disk(str(LOCAL_RAW))
        for i, text in enumerate(ds["input"]):
            if limit and i >= limit:
                return
            yield None, text or ""
    elif source == "humaneval":
        for ex in load_dataset("openai/openai_humaneval", split="test"):
            yield ex["task_id"], ex["prompt"]
    else:
        raise ValueError(source)


def count_related(cases, texts, progress_every=100_000):
    """Một lượt duyệt: tính số bài liên quan mỗi case và số bài khớp mỗi keyword."""
    kw2cases = {}
    for tid, (_, kws) in cases.items():
        for k in kws:
            kw2cases.setdefault(k.lower(), set()).add(tid)
    all_kws = list(kw2cases)

    case_count, kw_count, total = Counter(), Counter(), 0
    t0 = time.time()
    try:
        for own_id, text in texts:
            total += 1
            low = text.lower()
            hit_cases = set()
            for k in all_kws:
                if k in low:
                    kw_count[k] += 1
                    hit_cases |= kw2cases[k]
            hit_cases.discard(own_id)
            case_count.update(hit_cases)
            if progress_every and total % progress_every == 0:
                print(f"  đã duyệt {total:,} bài ({time.time() - t0:.0f}s)", flush=True)
    except KeyboardInterrupt:
        print(f"\nDừng sớm sau {total:,} bài, in kết quả phần đã duyệt.")
    return total, case_count, kw_count


def render(cases, total, case_count, kw_count, source):
    lines = [f"# Số bài liên quan với từng case fail (nguồn: {source}, đã duyệt {total:,} bài)", ""]
    lines.append("Bài liên quan = đề chứa ít nhất 1 keyword của case (không phân biệt hoa/thường, khớp substring).")
    lines.append("")
    for tid, (name, kws) in cases.items():
        n = case_count[tid]
        lines.append(f"- {tid} `{name}`: **{n:,}** bài liên quan ({n / total:.2%})")
    lines += ["", "## Số bài khớp từng keyword", ""]
    for tid, (name, kws) in cases.items():
        parts = ", ".join(f"{k} ({kw_count[k.lower()]:,})" for k in kws)
        lines.append(f"- {tid} `{name}`: {parts}")
    counts = [case_count[t] for t in cases]
    lines += ["", f"Tổng {len(cases)} case. Trung bình {sum(counts) / len(counts):,.0f} bài liên quan/case, "
                  f"ít nhất {min(counts):,}, nhiều nhất {max(counts):,}."]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--keywords", type=Path, default=DEFAULT_KEYWORDS)
    ap.add_argument("--source", choices=["nvidia", "local", "humaneval"], default="nvidia")
    ap.add_argument("--limit", type=int, default=0, help="chỉ duyệt N bài đầu (0 = tất cả)")
    ap.add_argument("--out", type=Path, help="ghi thêm kết quả ra file Markdown")
    args = ap.parse_args()

    cases = parse_keywords(args.keywords)
    print(f"{len(cases)} case, {len({k.lower() for _, kws in cases.values() for k in kws})} keyword; nguồn: {args.source}")
    total, case_count, kw_count = count_related(cases, iter_texts(args.source, args.limit))
    if not total:
        raise SystemExit("Không đọc được bài nào.")

    text = render(cases, total, case_count, kw_count, args.source)
    print("\n" + text)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"\nĐã ghi {args.out}")


if __name__ == "__main__":
    main()
