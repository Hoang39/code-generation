# Báo cáo benchmark: Qwen2.5-Coder-7B (base) vs bản fine-tune v3 (LoRA)

## 1. Thiết lập thí nghiệm

| Mục | Nội dung |
|---|---|
| Model gốc | `Qwen/Qwen2.5-Coder-7B` (base) |
| Model fine-tune | `hoangnh39/qwen2.5-coder-7b-opencode-hq10k-v3-merged` (LoRA đã merge vào base; dữ liệu OpenCodeInstruct, tập con chất lượng cao 10k) |
| Bộ đánh giá | EvalPlus: **HumanEval** (HE, 164 bài), **HumanEval+** (HE+, test mở rộng), **MBPP** (378 bài, MbppPlus v0.2.0), **MBPP+** |
| Backend / giải mã | EvalPlus + vLLM 0.32.0, **greedy**, **pass@1**, 1 mẫu/bài |
| Phần cứng / dtype | Kaggle 2× Tesla T4, `--tp 2`, `--dtype float16` (T4 không hỗ trợ bf16) |
| Prompt | Base: `--force-base-prompt` (completion thuần). v3: chat template mặc định của tokenizer (có system prompt mặc định của Qwen) |
| Notebook chạy | `run-evalplus-kaggle.ipynb` (HumanEval) và `run-evalplus-mbpp.ipynb` (MBPP): hai notebook chạy riêng, cùng cấu hình (vLLM, greedy, `--tp 2`, float16, base dùng `--force-base-prompt`, v3 dùng chat template). Kết quả chạy trực tiếp khớp với 8 file dữ liệu. |
| File kết quả | `qwen2.5-coder-7b-base-{eval,mbpp}-results.json(l)`, `hoangnh39-v3-merged-{eval,mbpp}-results.json(l)` |

Cách tính điểm: một bài chỉ được tính đúng ở bản "+" khi vượt qua **cả** test gốc lẫn test mở rộng (đúng quy ước EvalPlus). Điểm trong report khớp log của notebook (MBPP 0.786 / 0.802, MBPP+ 0.640 / 0.680).

## 2. Kết quả tổng hợp

| Benchmark | Base | v3 | Δ (điểm %) | Δ tương đối | Số bài đúng (base → v3) |
|---|---|---|---|---|---|
| HumanEval (HE) | 61.6% | **87.2%** | **+25.6** | +41.6% | 101 → 143 / 164 |
| HumanEval+ (HE+) | 53.0% | **80.5%** | **+27.4** | +51.7% | 87 → 132 / 164 |
| MBPP | 78.6% | **80.2%** | +1.6 | +2.0% | 297 → 303 / 378 |
| MBPP+ | 64.0% | **68.0%** | +4.0 | +6.2% | 242 → 257 / 378 |

Khoảng tin cậy 95% (Wilson):

| Benchmark | Base | v3 |
|---|---|---|
| HE | 54.0 – 68.7 | 81.2 – 91.5 |
| HE+ | 45.4 – 60.5 | 73.8 – 85.8 |
| MBPP | 74.2 – 82.4 | 75.8 – 83.9 |
| MBPP+ | 59.1 – 68.7 | 63.1 – 72.5 |

Độ tụt khi chuyển từ test gốc sang test mở rộng (độ "chịu" edge case):

| | Base | v3 |
|---|---|---|
| HE → HE+ | −8.5 điểm (14 bài qua HE nhưng rớt HE+) | −6.7 điểm (11 bài) |
| MBPP → MBPP+ | −14.6 điểm (55 bài) | −12.2 điểm (46 bài) |

## 3. So sánh theo từng bài (paired)

Số bài mà chỉ một trong hai model làm đúng, kèm kiểm định McNemar:

| Benchmark | Cả hai đúng | Chỉ base đúng | Chỉ v3 đúng | Cả hai sai | p-value |
|---|---|---|---|---|---|
| HE | 96 | 5 | **47** | 16 | < 0.001 |
| HE+ | 82 | 5 | **50** | 27 | < 0.001 |
| MBPP | 266 | 31 | 37 | 44 | 0.54 (không có ý nghĩa) |
| MBPP+ | 216 | 26 | 41 | 95 | 0.09 (không có ý nghĩa ở mức 5%) |

## 4. Nhận xét

### 4.1 HumanEval / HumanEval+: cải thiện rất lớn và có ý nghĩa thống kê
- v3 tăng khoảng 26–27 điểm. Trong 164 bài, v3 sửa được 47–50 bài mà base sai, và chỉ làm hỏng 5 bài (HE/10, 96, 142, 154, 155; ở HE+ là HE/10, 39, 142, 154, 155). Khoảng tin cậy của hai model không chồng lấn, p < 0.001.
- Các bài v3 sửa được thuộc nhóm ID 69–162, tức nhóm bài khó hơn, đề dài, nhiều điều kiện (xử lý chuỗi, ngày tháng, quy tắc đặc biệt, v.v.).
- v3 đạt 87.2% / 80.5%, tương đương nhóm Qwen2.5-Coder-7B-**Instruct**. Điều này gợi ý LoRA trên dữ liệu instruction đã chuyển model từ kiểu "completion" sang kiểu "làm theo chỉ dẫn" khá hiệu quả.

### 4.2 MBPP / MBPP+: cải thiện nhỏ, chưa đủ để kết luận
- Chênh lệch chỉ +1.6 (MBPP) và +4.0 (MBPP+). Hai khoảng tin cậy chồng lấn nhiều và McNemar không có ý nghĩa (MBPP+ p = 0.09, sát ngưỡng). Số bài v3 sửa (37–41) không hơn nhiều số bài v3 làm hỏng (31 và 26).
- Nguyên nhân khiến v3 không vượt trội ở MBPP:
  - **Đổi tên hàm.** Đề MBPP chỉ nêu tên hàm qua ví dụ assert. v3 hay tự đặt tên "đẹp" hơn, nên bài chạy lỗi `NameError` dù logic đúng. Ví dụ: `test_duplicate` → `has_duplicates`, `count_Substrings` → `count_substrings`, `is_upper` → `to_uppercase`, `count_Pairs` → `count_pairs`. Có 16/378 bài hai model không dùng chung tên hàm nào, trong đó 10 bài base đúng nhưng v3 sai.
  - **Sinh văn bản suy biến.** 3 bài (Mbpp/11, 565, 631) v3 xuất ra chuỗi `assistant\nassistant\n...` lặp vô hạn thay vì code. Base không bị lỗi này. Đây là dấu hiệu lỗi dừng sinh (EOS / `<|im_end|>`) hoặc chat template khi chạy bản merge trên vLLM. Các nguyên nhân có thể (chưa kiểm chứng): chat template tự thêm system prompt mặc định trong khi lúc train không có (chính notebook cũng ghi nhận khả năng này), hoặc chạy float16 trên T4 trong khi trọng số merge là bf16.
  - **Chạy chậm hơn nhiều.** Sinh code cho MBPP mất 21 phút với base nhưng 3 giờ 13 phút với v3 (khoảng 9 lần). Điều này khớp với việc v3 sinh dài hơn (docstring, giải thích, test) và các chuỗi lặp chạy tới giới hạn token. Cần tính chi phí suy luận nếu triển khai.
  - **Lời giải dài hơn.** Code v3 trung bình 435 ký tự so với 156 của base. 374/378 bài có docstring (base chỉ 5/378), và đôi khi kèm cả dòng `# Test cases` / `assert`. Đây là phong cách học từ OpenCodeInstruct. Nó không làm tăng độ đúng, và assert thừa có thể gây lỗi.
- MBPP+ gặp nhiều bài "qua test gốc nhưng rớt test mở rộng" ở cả hai model (55 và 46 bài), nghĩa là phần lớn lỗi nằm ở edge case (số âm, rỗng, kiểu dữ liệu lạ). Fine-tune giảm nhẹ nhưng chưa giải quyết được.

### 4.3 Điểm mạnh và điểm yếu còn lại của v3
- Mạnh: hiểu đề dài và các điều kiện phức tạp (HE); 0 lỗi cú pháp trên cả 4 bộ; ít bài rớt HE+ hơn base (11 so với 14); số bài sai trên HE giảm từ 63 xuống 21.
- Yếu:
  - Edge case: 27 bài HE+ cả hai model đều sai, có nhiều bài trùng lỗi input (ví dụ HE/15, 22, 76, 86 qua test gốc nhưng rớt test mở rộng).
  - Bài thuật toán/toán học khó (HE/32, 129, 130, 145…).
  - Tuân thủ tên hàm trong MBPP và độ ổn định khi sinh.

## 5. Lưu ý khi diễn giải (nên nói rõ khi báo cáo)

1. **Mức tăng của HE bị khuếch đại bởi cách chạy base.** Base chạy với `--force-base-prompt`, còn v3 chạy với chat template. Điểm base 61.6% / 53.0% trùng với số công bố của Qwen2.5-Coder-7B base (theo trí nhớ của tôi là 61.6 / 53.0, nên đối chiếu lại nguồn trước khi trích dẫn), cho thấy cách chạy base là chuẩn nhưng cũng là cấu hình "khó" nhất cho base. Trong các lần benchmark trước của bạn (harness tự viết, prompt few-shot, 4-bit), base đạt 76.8% / 69.5% và LoRA epoch-1 đạt 78.7% / 73.5%, tức chỉ chênh +1.8 / +4.0. Vì vậy cần ghi rõ đây là **so sánh theo từng cấu hình prompt**, không nên kết luận "fine-tune tăng 26 điểm năng lực" một cách tuyệt đối.
2. **Chưa kiểm tra rò rỉ dữ liệu (contamination).** Dữ liệu OpenCodeInstruct chưa được lọc trùng với HumanEval/MBPP trong phạm vi các file này. Mức 87.2% vượt xa kết quả harness cũ nên cần kiểm tra thêm.
3. **Chỉ 1 lần chạy greedy.** Không có phương sai giữa các seed. Với MBPP, chênh lệch nhỏ nằm trong nhiễu.
4. **Không rõ v3 tương ứng epoch nào** trong 3 epoch đã train (adapter epoch-1/2/3 trong `summary_qwen_ft_opencode_hq10k_3ep_n5.json`). Nên ghi chú khi báo cáo.

## 6. Kết luận và đề xuất

- **Kết luận:** v3 cải thiện rõ rệt trên HumanEval/HumanEval+ (+26–27 điểm, có ý nghĩa thống kê) và cải thiện nhẹ, chưa có ý nghĩa thống kê, trên MBPP/MBPP+ (+1.6 / +4.0 điểm). Không có dấu hiệu suy giảm tổng thể so với base.
- **Đề xuất cải thiện:**
  1. Sửa lỗi sinh lặp `assistant`: kiểm tra stop token `<|im_end|>` / `generation_config` của bản merge; thử chạy lại với `--dtype bfloat16` (GPU hỗ trợ bf16) hoặc chat template không có system prompt.
  2. Thêm dữ liệu huấn luyện kiểu MBPP (giữ nguyên tên hàm theo ví dụ assert, không in test, không docstring thừa), hoặc nhắc rõ tên hàm trong prompt.
  3. Chạy lại base với chat template (bản Instruct hoặc base + ChatML) để có so sánh công bằng cùng prompt.
  4. Chạy nhiều seed / sampling n≥5 cho MBPP, và lọc trùng dữ liệu train với các bộ benchmark.
  5. Bổ sung dữ liệu có edge case (input rỗng, số âm, kiểu bất thường) để giảm khoảng cách giữa điểm gốc và điểm "+".
