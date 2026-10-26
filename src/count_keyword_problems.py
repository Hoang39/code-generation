"""Đếm mỗi keyword trong data/base_humaneval_fewshot_failed_keywords.md có bao nhiêu bài trong nguồn dữ liệu.

Một bài được tính cho keyword khi đề (cột `input` của nvidia/OpenCodeInstruct) chứa keyword đó,
không phân biệt hoa/thường, khớp substring (nên "bore" khớp cả "bored"); mỗi bài chỉ tính một lần cho mỗi keyword.
Thêm --whole-word để chỉ khớp nguyên từ ("set" không khớp "dataset").

Nguồn (--source):
    nvidia  (mặc định) toàn bộ nvidia/OpenCodeInstruct (~5M mẫu), duyệt streaming, cần mạng
    local   10K mẫu high-quality đã lọc sẵn trong opencode_hq/raw (chạy nhanh, không cần mạng)

Chạy:
    python3 src/count_keyword_problems.py --source local
    python3 src/count_keyword_problems.py --limit 100000
    python3 src/count_keyword_problems.py --out data/keyword_problem_counts.md

Cài thêm `pyahocorasick` (pip install pyahocorasick) để quét nhanh hơn nhiều khi duyệt cả 5M mẫu;
không có thư viện này script vẫn chạy bằng vòng lặp thuần Python (chậm hơn).
Ctrl+C khi đang chạy vẫn in/ghi kết quả của phần đã duyệt.
"""
import argparse
import time
from collections import Counter
from pathlib import Path

from count_related_problems import DEFAULT_KEYWORDS, iter_texts, parse_keywords


def _is_word_char(c):
    return c.isalnum() or c == "_"


def _bounded(text, start, end, kw):
    """Keyword nằm ở text[start:end] có đứng riêng (không dính chữ/số/_ ở hai đầu) không."""
    left_ok = not _is_word_char(kw[0]) or start == 0 or not _is_word_char(text[start - 1])
    right_ok = not _is_word_char(kw[-1]) or end == len(text) or not _is_word_char(text[end])
    return left_ok and right_ok


def build_matcher(keywords, whole_word):
    """Trả về hàm find(text_lower) -> set các keyword (đã lower) xuất hiện trong text."""
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


def count_keywords(keywords, texts, whole_word, progress_every=100_000):
    """Một lượt duyệt: {keyword (lower): số bài chứa keyword}, tổng số bài đã duyệt."""
    find, fast = build_matcher(keywords, whole_word)
    print(f"Matcher: {'pyahocorasick' if fast else 'vòng lặp Python (chậm hơn; pip install pyahocorasick để nhanh hơn)'}")
    counts, total, t0 = Counter(), 0, time.time()
    try:
        for _, text, _ in texts:
            total += 1
            counts.update(find(text.lower()))
            if progress_every and total % progress_every == 0:
                print(f"  đã duyệt {total:,} bài ({time.time() - t0:.0f}s)", flush=True)
    except KeyboardInterrupt:
        print(f"\nDừng sớm sau {total:,} bài, in kết quả phần đã duyệt.")
    return counts, total


def render(cases, counts, total, source, whole_word):
    mode = "nguyên từ" if whole_word else "substring"
    lines = [f"# Số bài khớp từng keyword (nguồn: {source}, đã duyệt {total:,} bài, khớp {mode})", ""]
    for tid, (name, kws) in cases.items():
        parts = ", ".join(f"{k} ({counts[k.lower()]:,})" for k in kws)
        lines.append(f"- {tid} `{name}`: {parts}")
    uniq = {k.lower() for _, kws in cases.values() for k in kws}
    zero = sorted(k for k in uniq if not counts[k])
    lines += ["", f"Tổng {len(cases)} case, {len(uniq)} keyword khác nhau; {len(zero)} keyword không khớp bài nào."]
    if zero:
        lines.append("Không khớp bài nào: " + ", ".join(zero))
    top = counts.most_common(10)
    if top:
        lines.append("Khớp nhiều nhất: " + ", ".join(f"{k} ({n:,})" for k, n in top))
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--keywords", type=Path, default=DEFAULT_KEYWORDS)
    ap.add_argument("--source", choices=["nvidia", "local"], default="nvidia")
    ap.add_argument("--limit", type=int, default=0, help="chỉ duyệt N bài đầu (0 = tất cả)")
    ap.add_argument("--whole-word", action="store_true", help="chỉ khớp nguyên từ thay vì substring")
    ap.add_argument("--out", type=Path, help="ghi thêm kết quả ra file Markdown")
    args = ap.parse_args()

    cases = parse_keywords(args.keywords)
    keywords = sorted({k.lower() for _, kws in cases.values() for k in kws})
    print(f"{len(cases)} case, {len(keywords)} keyword khác nhau; nguồn: {args.source}")

    counts, total = count_keywords(keywords, iter_texts(args.source, args.limit), args.whole_word)
    if not total:
        raise SystemExit("Không đọc được bài nào.")

    text = render(cases, counts, total, args.source, args.whole_word)
    print("\n" + text)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"\nĐã ghi {args.out}")


if __name__ == "__main__":
    main()
