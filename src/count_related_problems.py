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

Xuất dữ liệu train: thêm --jsonl-out để ghi MỖI bài khớp ít nhất 1 keyword (input + output) ra file JSONL,
mỗi bài một dòng, bài khớp nhiều case chỉ được ghi một lần. Hai định dạng (--format):
    chatml   (mặc định) giống opencode_hq/chatml.jsonl của prepare_opencode_hq_10k.ipynb: đã ghép sẵn ChatML của Qwen
             {"text": "<|im_start|>user\\n<input><|im_end|>\\n<|im_start|>assistant\\n<output><|im_end|>"}
    messages chưa áp chat template, lúc train dùng tokenizer.apply_chat_template:
             {"messages": [{"role": "user", "content": "<input>"}, {"role": "assistant", "content": "<output>"}]}
Mặc định KHÔNG có system prompt (như bản đầu). Thêm --system-prompt để thêm system prompt mặc định của Qwen
(hoặc --system-prompt "nội dung khác").
    python3 src/count_related_problems.py --limit 1000000 --hq --jsonl-out opencode_hq/chatml_v2.jsonl   # định dạng chatml
    thêm --hq để chỉ giữ bài qua bộ lọc chất lượng như prepare_opencode_hq_10k.ipynb
"""
import argparse
import json
import re
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KEYWORDS = ROOT / "data" / "base_humaneval_fewshot_failed_keywords.md"
LOCAL_RAW = ROOT / "opencode_hq" / "raw"
NVIDIA_ID = "nvidia/OpenCodeInstruct"
SYSTEM_PROMPT = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."   # như prepare_opencode_hq_10k.ipynb

JUDGE_KEYS = ("requirement_conformance", "logical_correctness", "edge_case_consideration")
MIN_TEST_SCORE, MIN_JUDGE_SCORE = 0.8, 4

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
    """Sinh (id, text, record) của từng bài trong nguồn; id dùng để loại case khỏi chính nó (chỉ humaneval)."""
    try:
        from datasets import load_dataset, load_from_disk
    except ImportError:
        raise SystemExit("Thiếu thư viện `datasets`. Cài bằng: python3 -m pip install datasets")
    if source == "nvidia":
        stream = load_dataset(NVIDIA_ID, split="train", streaming=True)
        for i, ex in enumerate(stream):
            if limit and i >= limit:
                return
            yield None, ex["input"] or "", ex
    elif source == "local":
        ds = load_from_disk(str(LOCAL_RAW))
        for i, ex in enumerate(ds):
            if limit and i >= limit:
                return
            yield None, ex["input"] or "", ex
    elif source == "humaneval":
        for ex in load_dataset("openai/openai_humaneval", split="test"):
            yield ex["task_id"], ex["prompt"], ex
    else:
        raise ValueError(source)


def _to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def is_high_quality(ex):
    """Cùng bộ lọc với prepare_opencode_hq_10k.ipynb (average_test_score và llm_judgement là string)."""
    score = _to_float(ex.get("average_test_score"))
    if score is None or score < MIN_TEST_SCORE:
        return False
    judgement = ex.get("llm_judgement")
    if isinstance(judgement, str):
        try:
            judgement = json.loads(judgement)
        except (json.JSONDecodeError, TypeError):
            return False
    if not isinstance(judgement, dict):
        return False
    for key in JUDGE_KEYS:
        entry = judgement.get(key)
        v = _to_float(entry.get("score") if isinstance(entry, dict) else entry)
        if v is None or v < MIN_JUDGE_SCORE:
            return False
    return True


def to_chatml(ex, system_prompt=None):
    """{"text": ChatML Qwen} — cùng format với prepare_opencode_hq_10k.ipynb; None nếu input/output rỗng."""
    user, assistant = (ex.get("input") or "").strip(), (ex.get("output") or "").strip()
    if not user or not assistant:
        return None
    sys_part = f"<|im_start|>system\n{system_prompt}<|im_end|>\n" if system_prompt else ""
    return {"text": f"{sys_part}<|im_start|>user\n{user}<|im_end|>\n<|im_start|>assistant\n{assistant}<|im_end|>"}


def to_messages(ex, system_prompt=None):
    """{"messages": [(system,) user, assistant]} (chưa áp chat template); None nếu input/output rỗng."""
    user, assistant = (ex.get("input") or "").strip(), (ex.get("output") or "").strip()
    if not user or not assistant:
        return None
    messages = [{"role": "user", "content": user}, {"role": "assistant", "content": assistant}]
    if system_prompt:
        messages.insert(0, {"role": "system", "content": system_prompt})
    return {"messages": messages}


def count_related(cases, texts, progress_every=100_000, on_match=None):
    """Một lượt duyệt: tính số bài liên quan mỗi case và số bài khớp mỗi keyword.
    on_match(record) được gọi một lần cho mỗi bài khớp ít nhất 1 keyword (của case khác chính nó)."""
    kw2cases = {}
    for tid, (_, kws) in cases.items():
        for k in kws:
            kw2cases.setdefault(k.lower(), set()).add(tid)
    all_kws = list(kw2cases)

    case_count, kw_count, total = Counter(), Counter(), 0
    t0 = time.time()
    try:
        for own_id, text, record in texts:
            total += 1
            low = text.lower()
            hit_cases = set()
            for k in all_kws:
                if k in low:
                    kw_count[k] += 1
                    hit_cases |= kw2cases[k]
            hit_cases.discard(own_id)
            case_count.update(hit_cases)
            if hit_cases and on_match:
                on_match(record)
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
    ap.add_argument("--jsonl-out", type=Path, help="ghi các bài khớp (input+output) ra file JSONL (định dạng theo --format), mỗi dòng một JSON")
    ap.add_argument("--hq", action="store_true", help="với --jsonl-out: chỉ ghi bài qua bộ lọc chất lượng (test score/LLM judge)")
    ap.add_argument("--format", choices=["chatml", "messages"], default="chatml", help="định dạng mỗi dòng của --jsonl-out")
    ap.add_argument("--system-prompt", nargs="?", const=SYSTEM_PROMPT, default=None,
                    help="thêm system prompt vào mỗi mẫu (không kèm nội dung = system prompt mặc định của Qwen); mặc định không thêm")
    args = ap.parse_args()
    system_prompt = args.system_prompt
    to_record = to_chatml if args.format == "chatml" else to_messages

    cases = parse_keywords(args.keywords)
    print(f"{len(cases)} case, {len({k.lower() for _, kws in cases.values() for k in kws})} keyword; nguồn: {args.source}")
    sink, written, skipped = None, 0, Counter()
    on_match = None
    if args.jsonl_out:
        args.jsonl_out.parent.mkdir(parents=True, exist_ok=True)
        sink = args.jsonl_out.open("w", encoding="utf-8")

        def on_match(ex):
            nonlocal written
            if args.hq and not is_high_quality(ex):
                skipped["không qua bộ lọc chất lượng"] += 1
                return
            record = to_record(ex, system_prompt)
            if record is None:
                skipped["input/output rỗng"] += 1
                return
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1
    try:
        total, case_count, kw_count = count_related(cases, iter_texts(args.source, args.limit), on_match=on_match)
    finally:
        if sink:
            sink.close()
    if not total:
        raise SystemExit("Không đọc được bài nào.")

    text = render(cases, total, case_count, kw_count, args.source)
    print("\n" + text)
    if args.jsonl_out:
        print(f"\nĐã ghi {written:,} mẫu {args.format} -> {args.jsonl_out}" + (f" (bỏ qua: {dict(skipped)})" if skipped else ""))
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"\nĐã ghi {args.out}")


if __name__ == "__main__":
    main()
