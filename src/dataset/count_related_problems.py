"""Đếm số bài "liên quan" của từng case HumanEval/MBPP fail của model base trong một nguồn dữ liệu, và (tùy chọn) xuất tập train.

Bài liên quan = đề (cột `input` của nvidia/OpenCodeInstruct) chứa ít nhất 1 keyword của case fail,
so khớp không phân biệt hoa/thường theo substring (nên "bore" khớp cả "bored"; thêm --whole-word để chỉ khớp nguyên từ).
Keyword lấy từ data/base_humaneval_fewshot_failed_keywords.md.

Mặc định chỉ in kết quả (số bài mỗi case, mỗi keyword, tổng data khi gộp tất cả keyword). Thêm --out để xuất
MỖI bài được giữ (input + output) ra file JSONL, mỗi bài một dòng, bài khớp nhiều keyword chỉ được ghi một lần.

Nguồn (--source):
    nvidia     (mặc định) toàn bộ nvidia/OpenCodeInstruct (~5M mẫu), duyệt streaming, cần mạng
    local      10K mẫu high-quality đã lọc sẵn trong opencode_hq/raw (dùng để thử nhanh)
    humaneval  164 đề HumanEval (không tính chính case đó vào số bài liên quan)

Bộ lọc (áp dụng cho cả số đếm lẫn file xuất):
    --hq                chỉ xét bài qua bộ lọc chất lượng (average_test_score >= 0.8, 3 điểm LLM judge >= 4),
                        cùng bộ lọc với prepare_opencode_hq_10k.ipynb
    --max-tokens N      bỏ bài có độ dài (input + output, ChatML) từ N token trở lên, vd 1024 giữ bài < 1024 token;
                        đếm bằng tokenizer --tokenizer (mặc định Qwen/Qwen2.5-Coder-7B), chỉ tokenize bài đã khớp keyword
    --max-per-keyword N mỗi keyword giữ tối đa N bài (ưu tiên keyword hiếm trước); bài khớp nhiều keyword chỉ được ghi một lần

Chạy:
    python3 src/dataset/count_related_problems.py --source local                   # thử nhanh, chỉ in
    python3 src/dataset/count_related_problems.py --limit 100000                   # 100K bài đầu của nvidia, chỉ in
    python3 src/dataset/count_related_problems.py --hq --max-tokens 1024 --max-per-keyword 500                      # chỉ in
    python3 src/dataset/count_related_problems.py --hq --max-tokens 1024 --max-per-keyword 500 --out opencode_hq/chatml_v4.jsonl

Cài thêm `pyahocorasick` (pip install pyahocorasick) để quét nhanh hơn nhiều khi duyệt cả 5M mẫu;
không có thư viện này script vẫn chạy bằng vòng lặp thuần Python (chậm hơn). --max-tokens cần `transformers`.
Ctrl+C khi đang chạy vẫn in/ghi kết quả của phần đã duyệt.

Định dạng file --out (--format):
    chatml   (mặc định) giống opencode_hq/chatml.jsonl của prepare_opencode_hq_10k.ipynb: đã ghép sẵn ChatML của Qwen
             {"text": "<|im_start|>user\\n<input><|im_end|>\\n<|im_start|>assistant\\n<output><|im_end|>"}
    messages chưa áp chat template, lúc train dùng tokenizer.apply_chat_template:
             {"messages": [{"role": "user", "content": "<input>"}, {"role": "assistant", "content": "<output>"}]}
Mặc định KHÔNG có system prompt. Thêm --system-prompt để thêm system prompt mặc định của Qwen
(hoặc --system-prompt "nội dung khác").
"""
import argparse
import json
import re
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_KEYWORDS = ROOT / "data" / "base_humaneval_fewshot_failed_keywords.md"
LOCAL_RAW = ROOT / "opencode_hq" / "raw"
NVIDIA_ID = "nvidia/OpenCodeInstruct"
SYSTEM_PROMPT = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."   # như prepare_opencode_hq_10k.ipynb

JUDGE_KEYS = ("requirement_conformance", "logical_correctness", "edge_case_consideration")
MIN_TEST_SCORE, MIN_JUDGE_SCORE = 0.8, 4

LINE_RE = re.compile(r"^-\s+((?:HumanEval|Mbpp)/\d+)\s+`([^`]+)`:\s*(.+?)\s*$")
# tag cuối dòng cho biết bộ test sai, vd " [HE, HE+]" hay " [MBPP+]" (không phải keyword)
TAG_RE = re.compile(r"\s+\[(?:HE\+?|MBPP\+?)(?:,\s*(?:HE\+?|MBPP\+?))*\]$")


def split_keywords(s):
    """Tách theo dấu phẩy, bỏ qua dấu phẩy nằm trong (), [] hoặc "..." (vd `range [x, y]`, `a(n, m)`)."""
    parts, buf, depth, in_quote = [], [], 0, False
    for ch in s:
        if ch == '"':
            in_quote = not in_quote
        elif not in_quote and ch in "([":
            depth += 1
        elif not in_quote and ch in ")]":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0 and not in_quote:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    return [p.strip() for p in parts if p.strip()]


def parse_keywords(path):
    """{task_id: (task_name, [keyword, ...])} theo thứ tự trong file (HumanEval/N và Mbpp/N)."""
    cases = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = LINE_RE.match(line)
        if not m:
            continue
        task_id, name, kws = m.groups()
        kws = TAG_RE.sub("", kws).replace("\\*", "*")   # markdown escape `\*` -> `*`
        cases[task_id] = (name, split_keywords(kws))
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


def record_text(record):
    """Văn bản của một dòng xuất (chatml hoặc messages) để đếm token."""
    if "text" in record:
        return record["text"]
    return "\n".join(m["content"] for m in record["messages"])


def _is_word_char(c):
    return c.isalnum() or c == "_"


def _bounded(text, start, end, kw):
    """Keyword nằm ở text[start:end] có đứng riêng (không dính chữ/số/_ ở hai đầu) không."""
    left_ok = not _is_word_char(kw[0]) or start == 0 or not _is_word_char(text[start - 1])
    right_ok = not _is_word_char(kw[-1]) or end == len(text) or not _is_word_char(text[end])
    return left_ok and right_ok


def build_matcher(keywords, whole_word):
    """Trả về (find, fast): find(text_lower) -> set các keyword (đã lower) xuất hiện trong text."""
    try:
        import ahocorasick
    except ImportError:
        ahocorasick = None

    if ahocorasick:
        automaton = ahocorasick.Automaton()
        for k in keywords:
            automaton.add_word(k, k)
        automaton.make_automaton()

        def find(low):
            found = set()
            for end, k in automaton.iter(low):
                if k in found:
                    continue
                if not whole_word or _bounded(low, end - len(k) + 1, end + 1, k):
                    found.add(k)
            return found
    else:
        def find(low):
            found = set()
            for k in keywords:
                i = low.find(k)
                while i != -1:
                    if not whole_word or _bounded(low, i, i + len(k), k):
                        found.add(k)
                        break
                    i = low.find(k, i + 1)
            return found

    return find, bool(ahocorasick)


def count_related(cases, texts, keep=None, whole_word=False, progress_every=100_000):
    """Một lượt duyệt: trả về (số bài đã xét, số bài khớp mỗi keyword, [(record, tập keyword khớp)]).
    keep(record) -> bool lọc bài trước khi so khớp (vd bộ lọc chất lượng); bài không qua không được tính vào total.
    Keyword chỉ thuộc case của chính bài đó (nguồn humaneval) không được tính; bài không khớp keyword nào thì không có trong danh sách."""
    kw2cases = {}
    for tid, (_, kws) in cases.items():
        for k in kws:
            kw2cases.setdefault(k.lower(), set()).add(tid)
    find, fast = build_matcher(list(kw2cases), whole_word)
    print(f"Matcher: {'pyahocorasick' if fast else 'vòng lặp Python (chậm hơn; pip install pyahocorasick để nhanh hơn)'}")

    kw_count, matches, total, seen = Counter(), [], 0, 0
    t0 = time.time()
    try:
        for own_id, text, record in texts:
            seen += 1
            if keep is None or keep(record):
                total += 1
                hits = {k for k in find(text.lower()) if kw2cases[k] - {own_id}}
                kw_count.update(hits)
                if hits:
                    matches.append((record, hits))
            if progress_every and seen % progress_every == 0:
                print(f"  đã duyệt {seen:,} bài, giữ {total:,}, khớp {len(matches):,} ({time.time() - t0:.0f}s)", flush=True)
    except KeyboardInterrupt:
        print(f"\nDừng sớm sau {seen:,} bài, in kết quả phần đã duyệt.")
    return total, kw_count, matches


def select_samples(cases, matches, kw_count, to_record, system_prompt, max_tokens, tokenizer_name, max_per_keyword):
    """Lọc độ dài token rồi giới hạn số bài mỗi keyword (ưu tiên keyword hiếm). Một bài được giữ nếu có ít nhất
    một keyword khớp còn chỗ; nó được tính vào các keyword còn chỗ đó.
    Trả về (case_count, số bài giữ mỗi keyword, [record xuất], skipped); case_count đếm bài giữ theo mọi keyword khớp."""
    skipped = Counter()
    tok = None
    if max_tokens:
        try:
            from transformers import AutoTokenizer
        except ImportError:
            raise SystemExit("Thiếu thư viện `transformers` cho --max-tokens. Cài bằng: python3 -m pip install transformers")
        tok = AutoTokenizer.from_pretrained(tokenizer_name)
    kw2cases = {}
    for tid, (_, kws) in cases.items():
        for k in kws:
            kw2cases.setdefault(k.lower(), set()).add(tid)

    taken, case_count, records = Counter(), Counter(), []
    for ex, hits in sorted(matches, key=lambda m: min(kw_count[k] for k in m[1])):   # bài khớp keyword hiếm đi trước
        open_kws = [k for k in hits if not max_per_keyword or taken[k] < max_per_keyword]
        if not open_kws:
            skipped[f"mọi keyword khớp đã đủ {max_per_keyword} bài"] += 1
            continue
        record = to_record(ex, system_prompt)
        if record is None:
            skipped["input/output rỗng"] += 1
            continue
        if tok and len(tok(record_text(record), add_special_tokens=False)["input_ids"]) >= max_tokens:
            skipped[f"từ {max_tokens} token trở lên"] += 1
            continue
        taken.update(open_kws)
        case_count.update(set().union(*(kw2cases[k] for k in hits)))
        records.append(record)
    return case_count, taken, records, skipped


def render(cases, total, case_count, kw_count, taken, source, exported, filters, whole_word):
    mode = "nguyên từ" if whole_word else "substring"
    lines = [f"# Số bài liên quan với từng case fail (nguồn: {source}, đã xét {total:,} bài, khớp {mode})", ""]
    lines.append("Bài liên quan = đề chứa ít nhất 1 keyword của case (không phân biệt hoa/thường), tính trên các bài được giữ.")
    if filters:
        lines.append("Bộ lọc: " + ", ".join(filters) + ".")
    lines.append("")
    for tid, (name, kws) in cases.items():
        n = case_count[tid]
        lines.append(f"- {tid} `{name}`: **{n:,}** bài liên quan ({n / total:.2%})")
    lines += ["", "## Số bài giữ / số bài khớp từng keyword", ""]
    for tid, (name, kws) in cases.items():
        parts = ", ".join(f"{k} ({taken[k.lower()]:,}/{kw_count[k.lower()]:,})" for k in kws)
        lines.append(f"- {tid} `{name}`: {parts}")
    uniq = {k.lower() for _, kws in cases.values() for k in kws}
    zero = sorted(k for k in uniq if not kw_count[k])
    counts = [case_count[t] for t in cases]
    lines += ["", f"Tổng {len(cases)} case, {len(uniq)} keyword khác nhau; {len(zero)} keyword không khớp bài nào.",
              f"Trung bình {sum(counts) / len(counts):,.0f} bài liên quan/case, ít nhất {min(counts):,}, nhiều nhất {max(counts):,}."]
    if zero:
        lines.append("Không khớp bài nào: " + ", ".join(zero))
    top = kw_count.most_common(10)
    if top:
        lines.append("Khớp nhiều nhất: " + ", ".join(f"{k} ({n:,})" for k, n in top))
    lines.append(f"Tổng data khi gộp tất cả keyword: {exported:,} bài khác nhau ({exported / total:.2%} của {total:,} bài đã xét).")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--keywords", type=Path, default=DEFAULT_KEYWORDS)
    ap.add_argument("--source", choices=["nvidia", "local", "humaneval"], default="nvidia")
    ap.add_argument("--limit", type=int, default=0, help="chỉ duyệt N bài đầu (0 = tất cả)")
    ap.add_argument("--whole-word", action="store_true", help="chỉ khớp nguyên từ thay vì substring")
    ap.add_argument("--hq", action="store_true", help="chỉ xét bài qua bộ lọc chất lượng (test score/LLM judge)")
    ap.add_argument("--max-tokens", type=int, default=0, help="bỏ bài có từ N token trở lên (0 = không lọc), vd 1024")
    ap.add_argument("--tokenizer", default="Qwen/Qwen2.5-Coder-7B", help="tokenizer để đếm token cho --max-tokens")
    ap.add_argument("--max-per-keyword", type=int, default=0, help="mỗi keyword giữ tối đa N bài (0 = không giới hạn), vd 500")
    ap.add_argument("--out", type=Path, help="xuất các bài được giữ (input+output) ra file JSONL; không có thì chỉ in kết quả")
    ap.add_argument("--format", choices=["chatml", "messages"], default="chatml", help="định dạng mỗi dòng của --out")
    ap.add_argument("--system-prompt", nargs="?", const=SYSTEM_PROMPT, default=None,
                    help="thêm system prompt vào mỗi mẫu (không kèm nội dung = system prompt mặc định của Qwen); mặc định không thêm")
    args = ap.parse_args()
    to_record = to_chatml if args.format == "chatml" else to_messages

    cases = parse_keywords(args.keywords)
    print(f"{len(cases)} case, {len({k.lower() for _, kws in cases.values() for k in kws})} keyword; nguồn: {args.source}")
    total, kw_count, matches = count_related(cases, iter_texts(args.source, args.limit),
                                             keep=is_high_quality if args.hq else None, whole_word=args.whole_word)
    if not total:
        raise SystemExit("Không đọc được bài nào.")
    print(f"Khớp ít nhất 1 keyword: {len(matches):,}/{total:,} bài; đang lọc độ dài token và giới hạn số bài mỗi keyword...")
    case_count, taken, records, skipped = select_samples(
        cases, matches, kw_count, to_record, args.system_prompt, args.max_tokens, args.tokenizer, args.max_per_keyword)

    filters = []
    if args.hq:
        filters.append("chỉ bài qua bộ lọc chất lượng")
    if args.max_tokens:
        filters.append(f"< {args.max_tokens} token")
    if args.max_per_keyword:
        filters.append(f"mỗi keyword tối đa {args.max_per_keyword:,} bài")
    print("\n" + render(cases, total, case_count, kw_count, taken, args.source, len(records), filters, args.whole_word))
    if skipped:
        print("\nBỏ qua: " + ", ".join(f"{k}: {n:,}" for k, n in skipped.items() if n))
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", encoding="utf-8") as sink:
            for record in records:
                sink.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"\nĐã ghi {len(records):,} mẫu {args.format} -> {args.out}")


if __name__ == "__main__":
    main()
