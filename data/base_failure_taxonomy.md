# Phân loại các bài sai của Qwen2.5-Coder-7B (base) trên HumanEval, HumanEval+, MBPP, MBPP+

Nguồn: kết quả EvalPlus greedy pass@1 của base (`--force-base-prompt`), 213 bài sai trong tổng 164 + 378 bài.

## Cách đọc

- Cột **HE** và **MBPP**: bài sai ngay ở test gốc.
- Cột **HE+** và **MBPP+**: bài đã qua test gốc nhưng sai ở test mở rộng ("chỉ sai bản +"). Số bài sai của HumanEval+ đầy đủ là HE + HE+ (63 + 14 = 77), của MBPP+ là MBPP + MBPP+ (81 + 55 = 136).
- Số trong các cột là số thứ tự bài (HE/HE+ là `HumanEval/N`, MBPP/MBPP+ là `Mbpp/N`).
- Mỗi bài thuộc đúng một nhóm lỗi.

## Cách phân loại

1. Chạy lại lời giải sai của base trên input lỗi đầu tiên mà EvalPlus ghi lại (input được đưa về đúng kiểu như EvalPlus: tuple, set, complex với MBPP). Nếu input ghi lại không tái hiện được lỗi thì quét toàn bộ input của bài.
2. Loại lỗi lấy từ kết quả chạy: exception thì theo tên exception, chạy quá 25 giây thì là Timeout, chạy xong nhưng sai kết quả thì là AssertionError.
3. AssertionError được chia nhỏ theo nguyên nhân bằng cách đọc code và so với đề (cột mô tả lý do), nên phần chia nhỏ này là đánh giá thủ công.
4. Những bài EvalPlus báo sai nhưng chạy lại trên máy không thấy lỗi (HE/15, MBPP/160, MBPP/566) được xếp theo nguyên nhân hợp lý nhất: HE/15 và MBPP/160 là chạy chậm vượt giới hạn thời gian, MBPP/566 là số 1e100.

## Tổng hợp theo loại lỗi

| Loại lỗi | HE | HE+ | MBPP | MBPP+ | Tổng | Tỉ lệ |
|---|---|---|---|---|---|---|
| AssertionError | 47 | 7 | 68 | 36 | 158 | 74.2% |
| Timeout | 2 | 3 | 1 | 8 | 14 | 6.6% |
| IndexError | 4 | 1 | 1 | 7 | 13 | 6.1% |
| ValueError | 2 | 1 | 0 | 3 | 6 | 2.8% |
| NameError | 2 | 0 | 4 | 0 | 6 | 2.8% |
| TypeError | 0 | 0 | 5 | 0 | 5 | 2.3% |
| SyntaxError | 3 | 0 | 0 | 0 | 3 | 1.4% |
| RecursionError | 1 | 1 | 1 | 0 | 3 | 1.4% |
| AttributeError | 1 | 0 | 1 | 0 | 2 | 0.9% |
| UnboundLocalError | 1 | 0 | 0 | 1 | 2 | 0.9% |
| ZeroDivisionError | 0 | 1 | 0 | 0 | 1 | 0.5% |
| **Tổng** | **63** | **14** | **81** | **55** | **213** | 100% |

## Bảng chi tiết

| Nhóm lỗi | HE | HE+ | MBPP | MBPP+ | Mô tả lý do | Số bài |
|---|---|---|---|---|---|---|
| AssertionError – hiểu sai yêu cầu đề | 26, 33, 37, 40, 54, 69, 75, 91, 93, 102, 106, 108, 110, 111, 127, 132, 133, 139, 144, 145, 157, 161, 163 | – | 63, 79, 102, 109, 120, 137, 138, 235, 237, 255, 259, 267, 286, 287, 299, 305, 306, 310, 398, 420, 429, 433, 472, 473, 572, 573, 615, 631, 732, 765, 769, 772, 777, 780 | 16, 440, 446, 602, 759, 790, 792, 809 | Code chạy được nhưng làm khác đề: nhầm toán tử (trừ thay vì AND, round thay vì ceil), nhầm even/odd hoặc natural/odd, trả tất cả thay vì chỉ phần tử thỏa điều kiện (xuất hiện 1 lần, đếm lớn nhất), bỏ sót một bước của đề (HE/93 quên thay nguyên âm), đảo ngược điều kiện (MBPP/79, 433, 809), regex quá chặt hoặc quá lỏng, dùng product thay cho combinations_with_replacement (MBPP/255). | 65 |
| AssertionError – sai công thức / thuật toán | 83, 115, 150 | 82 | 20, 56, 103, 125, 245, 260, 279, 300, 311, 432, 448, 468, 581, 589, 592, 603, 622, 626, 721, 735 | 620 | Công thức toán hoặc thuật toán cài sai: số Woodall, Eulerian, Newman prime, decagonal, Perrin, diện tích/bề mặt hình học, DP (bitonic, increasing subsequence, largest subset, maxAverageOfPath), kiểm tra số nguyên tố, ludic, median hai mảng, max_fill (cần ceil theo từng hàng). | 25 |
| AssertionError – off-by-one / sai biên | 6, 121, 125, 135, 148 | 96 | 101, 244, 268, 301, 610, 739 | – | Sai chỉ số hoặc biên khoảng: dùng chỉ số 0-based thay vì 1-based (kth_element, remove_kth_element), vị trí chẵn tính theo 1-based (HE/121), đếm thiếu/thừa một phần tử (HE/6 độ sâu ngoặc, HE/96 primes < n, find_Index, star number, dict_depth, next_Perfect_Square). | 12 |
| AssertionError – thiếu xử lý edge case | 74, 90, 126, 131, 146 | 22, 49, 86, 97, 151 | – | 6, 72, 92, 99, 113, 227, 232, 278, 397, 427, 435, 576, 597, 598, 607, 741, 771, 805 | Đúng với ví dụ trong đề nhưng sai với input biên của test "+": danh sách/chuỗi rỗng, 1 phần tử, số 0 hoặc 1, số âm, phần tử trùng hoặc bằng nhau, bool/float lẫn trong list số nguyên (HE/22, HE/151), xuống dòng trong chuỗi (HE/86), toàn số âm (MBPP/805), độ dài chuỗi = 2 (MBPP/92). | 28 |
| AssertionError – sai định dạng / kiểu / thứ tự đầu ra | 120 | – | 415, 454, 462, 749, 794 | – | Giá trị đúng ý nhưng khác dạng: trả str thay vì bool ("Found a match!" thay cho True, MBPP/454, 794), trả str thay vì int (MBPP/749), sai thứ tự phần tử (HE/120 thiếu sort tăng dần, MBPP/415 cặp (8,7) thay vì (7,8), MBPP/462 thứ tự subset). | 6 |
| AssertionError – hàm kết thúc không return (trả None) | 77, 94, 101, 105, 107, 119, 122, 129, 143, 160 | – | – | 577 | Có nhánh/đường thực thi không có return, hoặc code dừng giữa chừng (sinh dở), nên hàm trả None. Thường ở bài đề dài, nhiều bước (HE/101, 105, 107, 119, 122, 129, 143, 160) và MBPP/577 (n lớn). | 11 |
| AssertionError – đề hoặc đáp án chuẩn mơ hồ (quirk MBPP) | – | – | 264, 430, 590 | 74, 459, 593, 639, 786, 806 | Đề MBPP mô tả mơ hồ, đáp án chuẩn có hành vi riêng mà đề không nói rõ: công thức tuổi chó (264), directrix parabol (430), polar_rect trả cặp lồng nhau (590), remove_uppercase (459), removezero_ip (593), sample_nam (639), max_run_uppercase (806), is_samepatterns (74), right_insertion trên list không sort (786). | 9 |
| AssertionError – sai số học (float / số rất lớn) | – | – | – | 274, 566 | Dùng float hoặc phép chia thực cho số rất lớn nên mất độ chính xác (MBPP/274 tổng hệ số nhị thức n=101) hoặc xử lý sai số 1e100 (MBPP/566 sum_digits). | 2 |
| IndexError – input rỗng / quá ngắn | 9, 134, 141 | 64 | 755 | 119, 223 | Truy cập phần tử đầu/cuối hoặc theo chỉ số cố định khi list/chuỗi rỗng hoặc quá ngắn (vd. HE/9 rolling_max([]), HE/64 vowels_count(''), HE/134 với chuỗi 'A', MBPP/119 và 223 với list rỗng). | 7 |
| IndexError – giả định độ dài / cấu trúc input | 130 | – | – | 142, 272, 391, 445, 754 | Lặp theo độ dài của một list rồi truy cập list khác (độ dài khác nhau, thiếu zip), hard-code chỉ số 2 cho tuple, hoặc bảng DP khởi tạo thiếu phần tử (HE/130 tri). | 6 |
| ValueError | 19, 124 | 89 | – | 77, 630, 785 | Giả định định dạng input cố định rồi int()/index()/unpack bị lỗi: int("three") (HE/19 không tra bảng từ), str.index với ký tự ngoài bảng chữ cái (HE/89), unpack sai số phần tử (HE/124, MBPP/630), int("-") với số âm (MBPP/77), chuỗi tuple sai định dạng (MBPP/785). | 6 |
| TypeError – kiểu dữ liệu không đồng nhất / không hỗ trợ | – | – | 124, 294, 410 | – | So sánh hoặc tính toán trên kiểu không tương thích: so sánh int với str trong list hỗn hợp (MBPP/294, 410), math.atan2 nhận số phức (MBPP/124). | 3 |
| TypeError – ghi đè tên hàm / builtin bằng biến | – | – | 64, 782 | – | Đặt biến trùng tên hàm hoặc builtin: sum = 0 rồi gọi sum(...) (MBPP/782); chỉ gán subject_marks = [...] thay vì định nghĩa hàm nên bị gọi như list (MBPP/64). | 2 |
| AttributeError | 137 | – | 763 | – | Giả định kiểu input: gọi .replace trên int (HE/137 compare_one nhận int/float/str), gọi .sort() trên tuple (MBPP/763, EvalPlus truyền tuple). | 2 |
| NameError – thiếu import / hàm phụ / thụt lề sai | 79, 140 | – | 388, 635 | – | Dùng re, math, heapify mà không import hoặc không định nghĩa (HE/140, MBPP/388, 635); phần thân hàm bị thụt lề ra ngoài hàm nên tham số chưa định nghĩa (HE/79). | 4 |
| NameError – không có hàm đúng tên (entry point) | – | – | 239, 629 | – | File chỉ có hàm tên khác hoặc output bị cắt: MBPP/239 chỉ còn dòng import lru_cache, MBPP/629 đặt tên even_numbers thay vì Split (kèm code test thừa). | 2 |
| SyntaxError | 95, 138, 162 | – | – | – | "return outside function": thân hàm thụt lề sai hoặc sinh code lẫn docstring/doctest, không biên dịch được. | 3 |
| UnboundLocalError | 59 | – | – | 418 | Biến cục bộ dùng trước khi gán: gọi is_prime trước khi định nghĩa hàm con (HE/59), max_list chưa gán khi mọi list rỗng (MBPP/418). | 2 |
| ZeroDivisionError | – | 76 | – | – | Chia cho 0 khi n = 0 (HE/76 is_simple_power với input [-1, 0]). | 1 |
| RecursionError | 31 | 13 | 162 | – | Đệ quy tuyến tính quá sâu hoặc thiếu base case: gcd bằng phép trừ (HE/13), is_prime đệ quy từng số (HE/31), sum_series thiếu điều kiện dừng khi n lẻ (MBPP/162). | 3 |
| Timeout – đệ quy không memo (độ phức tạp mũ) | – | 55, 63 | – | 84, 392, 752 | Fibonacci, FibFib, Newman-Conway, Jacobsthal, get_max_sum cài đệ quy thuần, test "+" dùng n lớn nên vượt giới hạn thời gian. | 5 |
| Timeout – vòng lặp O(n) / O(n²) với n lớn | – | 15 | 123 | 126, 160, 599, 605, 781 | Duyệt tuyến tính hoặc lồng nhau thay vì công thức/căn bậc hai: find_solution (n²), sum_average, prime_num, count_divisors, tổng ước, amicable; HE/15 (n = 10^6) sát giới hạn thời gian, chưa tái hiện được hoàn toàn. | 7 |
| Timeout – vòng lặp vô hạn / không hội tụ | 32, 100 | – | – | – | while True không có điều kiện dừng hợp lệ: HE/32 find_zero chỉ thử x nguyên tăng dần, HE/100 make_a_pile tăng current_stones mãi. | 2 |
| **Tổng** | **63** | **14** | **81** | **55** | | **213** |
