# Các bài sai của 2 model (EvalPlus, greedy pass@1)

Ký hiệu: `HE` = HumanEval (test gốc), `HE+` = HumanEval+; ✅ pass, ❌ fail. `Input lỗi` là input đầu tiên làm test fail (cắt ngắn).

- Base: sai **77** bài (HE sai 63, HE+ sai 76)
- v3: sai **32** bài (HE sai 21, HE+ sai 32)
- Hợp: **82** bài — cả hai sai: **27**, chỉ base sai: **50**, chỉ v3 sai: **5**


## 1. Cả hai model đều sai (27 bài)

| Task | Hàm | Base HE/HE+ | v3 HE/HE+ | Input lỗi (base) | Input lỗi (v3) |
|---|---|---|---|---|---|
| HumanEval/15 | `string_sequence` | ✅/❌ | ✅/❌ | [1000000] | [1000000] |
| HumanEval/22 | `filter_integers` | ✅/❌ | ✅/❌ | [[True, False, None, 0, -10, 'test', [], {}, 3.14]] | [[True, False, None, 0, -10, 'test', [], {}, 3.14]] |
| HumanEval/26 | `remove_duplicates` | ❌/❌ | ❌/❌ | [[1, 2, 3, 2, 4, 3, 5]] | [[1, 2, 3, 2, 4, 3, 5]] |
| HumanEval/32 | `find_zero` | ❌/❌ | ❌/❌ | [[-10, -2]] | [[-10, -2]] |
| HumanEval/54 | `same_chars` | ❌/❌ | ❌/❌ | ['eabcdzzzz', 'dddzzzzzzzddeddabc'] | ['eabcdzzzz', 'dddzzzzzzzddeddabc'] |
| HumanEval/75 | `is_multiply_prime` | ❌/❌ | ✅/❌ | [5] | [0] |
| HumanEval/76 | `is_simple_power` | ✅/❌ | ✅/❌ | [-1, 0] | [-2, -2] |
| HumanEval/86 | `anti_shuffle` | ✅/❌ | ✅/❌ | ['\n\n123 456\n789\n'] | ['\n\n123 456\n789\n'] |
| HumanEval/90 | `next_smallest` | ❌/❌ | ✅/❌ | [[1, 1]] | [[2, 2, 2, 2, 2, 2, 3, 3, 3, 3]] |
| HumanEval/91 | `is_bored` | ❌/❌ | ❌/❌ | ['Is the sky blue?'] | ['Is the sky blue?'] |
| HumanEval/93 | `encode` | ❌/❌ | ❌/❌ | ['Mudasir'] | ['TEST'] |
| HumanEval/96 | `count_up_to` | ✅/❌ | ❌/❌ | [2] | [5] |
| HumanEval/100 | `make_a_pile` | ❌/❌ | ❌/❌ | [3] | [3] |
| HumanEval/101 † | `words_string` | ❌/❌ | ❌/❌ | ['Hi, my name is John'] | ['Hi, my name is John'] |
| HumanEval/106 | `f` | ❌/❌ | ✅/❌ | [5] | [100] |
| HumanEval/108 | `count_nums` | ❌/❌ | ❌/❌ | [[-1, -2, 0]] | [[12, 23, 34, -45, -56, 0]] |
| HumanEval/120 | `maximum` | ❌/❌ | ❌/❌ | [[-3, -4, 5], 3] | [[-3, -4, 5], 3] |
| HumanEval/124 | `valid_date` | ❌/❌ | ✅/❌ | ['04122003'] | ['06-04-202'] |
| HumanEval/127 | `intersection` | ❌/❌ | ❌/❌ | [[-1, 1], [0, 4]] | [[-1, 1], [0, 4]] |
| HumanEval/129 | `minPath` | ❌/❌ | ❌/❌ | [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3] | [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3] |
| HumanEval/130 | `tri` | ❌/❌ | ❌/❌ | [3] | [3] |
| HumanEval/132 | `is_nested` | ❌/❌ | ❌/❌ | ['[[]]'] | ['[[]'] |
| HumanEval/133 | `sum_squares` | ❌/❌ | ❌/❌ | [[1.4, 4.2, 0]] | [[1.4, 4.2, 0]] |
| HumanEval/134 | `check_if_last_char_is_a_letter` | ❌/❌ | ✅/❌ | ['A'] | ['apple pi\ne'] |
| HumanEval/139 | `special_factorial` | ❌/❌ | ✅/❌ | [4] | [95] |
| HumanEval/145 | `order_by_points` | ❌/❌ | ❌/❌ | [[1, 11, -1, -11, -12]] | [[1, 11, -1, -11, -12]] |
| HumanEval/163 | `generate_integers` | ❌/❌ | ❌/❌ | [2, 10] | [2, 10] |

## 2. Chỉ v3 sai (base đúng cả HE và HE+) — v3 tệ hơn base (5 bài)

| Task | Hàm | Base HE/HE+ | v3 HE/HE+ | Input lỗi (base) | Input lỗi (v3) |
|---|---|---|---|---|---|
| HumanEval/10 | `make_palindrome` | ✅/✅ | ❌/❌ | - | ['x'] |
| HumanEval/39 | `prime_fib` | ✅/✅ | ✅/❌ | - | [12] |
| HumanEval/142 | `sum_squares` | ✅/✅ | ❌/❌ | - | [[1, 2, 3]] |
| HumanEval/154 | `cycpattern_check` | ✅/✅ | ❌/❌ | - | ['xyzw', 'xyw'] |
| HumanEval/155 | `even_odd_count` | ✅/✅ | ❌/❌ | - | [0] |

## 3. Chỉ base sai (v3 đúng cả HE và HE+) — v3 sửa được (50 bài)

| Task | Hàm | Base HE/HE+ | v3 HE/HE+ | Input lỗi (base) | Input lỗi (v3) |
|---|---|---|---|---|---|
| HumanEval/6 | `parse_nested_parens` | ❌/❌ | ✅/✅ | ['(()()) ((())) () ((())()())'] | - |
| HumanEval/9 | `rolling_max` | ❌/✅ | ✅/✅ | [[]] | - |
| HumanEval/13 | `greatest_common_divisor` | ✅/❌ | ✅/✅ | [540, 541] | - |
| HumanEval/19 | `sort_numbers` | ❌/❌ | ✅/✅ | ['three'] | - |
| HumanEval/31 | `is_prime` | ❌/❌ | ✅/✅ | [101] | - |
| HumanEval/33 | `sort_third` | ❌/❌ | ✅/✅ | [[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]] | - |
| HumanEval/37 | `sort_even` | ❌/❌ | ✅/✅ | [[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]] | - |
| HumanEval/40 | `triples_sum_to_zero` | ❌/❌ | ✅/✅ | [[1, 3, -2, 1]] | - |
| HumanEval/49 | `modp` | ✅/❌ | ✅/✅ | [0, 1] | - |
| HumanEval/55 | `fib` | ✅/❌ | ✅/✅ | [63] | - |
| HumanEval/59 | `largest_prime_factor` | ❌/❌ | ✅/✅ | [15] | - |
| HumanEval/63 | `fibfib` | ✅/❌ | ✅/✅ | [57] | - |
| HumanEval/64 | `vowels_count` | ✅/❌ | ✅/✅ | [''] | - |
| HumanEval/69 | `search` | ❌/❌ | ✅/✅ | [[5, 5, 5, 5, 1]] | - |
| HumanEval/74 | `total_match` | ❌/❌ | ✅/✅ | [[], []] | - |
| HumanEval/77 | `iscube` | ❌/❌ | ✅/✅ | [1] | - |
| HumanEval/79 † | `decimal_to_binary` | ❌/❌ | ✅/✅ | - | - |
| HumanEval/82 | `prime_length` | ✅/❌ | ✅/✅ | ['ThiMsYJFEtsgcehuqTkrPdog.xBantidisestablishmentarilaniismL… | - |
| HumanEval/83 | `starts_one_ends` | ❌/❌ | ✅/✅ | [2] | - |
| HumanEval/89 | `encrypt` | ✅/❌ | ✅/✅ | ['test123'] | - |
| HumanEval/94 | `skjkasdkd` | ❌/❌ | ✅/✅ | [[0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, … | - |
| HumanEval/95 † | `check_dict_case` | ❌/❌ | ✅/✅ | - | - |
| HumanEval/97 | `multiply` | ✅/❌ | ✅/✅ | [-6, -9] | - |
| HumanEval/102 | `choose_num` | ❌/❌ | ✅/✅ | [12, 15] | - |
| HumanEval/105 | `by_length` | ❌/❌ | ✅/✅ | [[2, 1, 1, 4, 5, 8, 2, 3]] | - |
| HumanEval/107 | `even_odd_palindrome` | ❌/❌ | ✅/✅ | [123] | - |
| HumanEval/110 | `exchange` | ❌/❌ | ✅/✅ | [[5, 7, 3], [2, 6, 4]] | - |
| HumanEval/111 | `histogram` | ❌/❌ | ✅/✅ | ['a b c a b'] | - |
| HumanEval/115 | `max_fill` | ❌/❌ | ✅/✅ | [[[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1] | - |
| HumanEval/119 | `match_parens` | ❌/❌ | ✅/✅ | [['()(', ')']] | - |
| HumanEval/121 | `solution` | ❌/❌ | ✅/✅ | [[3, 3, 3, 3, 3]] | - |
| HumanEval/122 | `add_elements` | ❌/❌ | ✅/✅ | [[1, -2, -3, 41, 57, 76, 87, 88, 99], 3] | - |
| HumanEval/125 | `split_words` | ❌/❌ | ✅/✅ | ['aaabb'] | - |
| HumanEval/126 | `is_sorted` | ❌/❌ | ✅/✅ | [[5]] | - |
| HumanEval/131 | `digits` | ❌/❌ | ✅/✅ | [2468] | - |
| HumanEval/135 | `can_arrange` | ❌/❌ | ✅/✅ | [[1, 2, 4, 3, 5]] | - |
| HumanEval/137 | `compare_one` | ❌/❌ | ✅/✅ | [1, 2.5] | - |
| HumanEval/138 † | `is_equal_to_sum_even` | ❌/❌ | ✅/✅ | - | - |
| HumanEval/140 | `fix_spaces` | ❌/❌ | ✅/✅ | ['Example'] | - |
| HumanEval/141 | `file_name_check` | ❌/❌ | ✅/✅ | ['.txt'] | - |
| HumanEval/143 | `words_in_sentence` | ❌/❌ | ✅/✅ | ['This is a test'] | - |
| HumanEval/144 | `simplify` | ❌/❌ | ✅/✅ | ['1/6', '2/1'] | - |
| HumanEval/146 | `specialFilter` | ❌/❌ | ✅/✅ | [[33, -2, -3, 45, 21, 109]] | - |
| HumanEval/148 | `bf` | ❌/❌ | ✅/✅ | ['Earth', 'Mercury'] | - |
| HumanEval/150 | `x_or_y` | ❌/❌ | ✅/✅ | [15, 8, 5] | - |
| HumanEval/151 | `double_the_difference` | ✅/❌ | ✅/✅ | [[1, 3.5, -4.6]] | - |
| HumanEval/157 | `right_angle_triangle` | ❌/❌ | ✅/✅ | [3, 4, 5] | - |
| HumanEval/160 | `do_algebra` | ❌/❌ | ✅/✅ | [['**', '*', '+'], [2, 3, 4, 5]] | - |
| HumanEval/161 | `solve` | ❌/❌ | ✅/✅ | ['AsDf'] | - |
| HumanEval/162 † | `string_to_md5` | ❌/❌ | ✅/✅ | - | - |

† Base: thân hàm rỗng (chỉ có docstring), code sinh ra bị lệch thụt lề/cụt nên fail do lỗi định dạng, không phải sai thuật toán. Thuộc 5 trong 63 bài HumanEval base sai (HumanEval/79, 95, 101, 138, 162). v3 không có trường hợp nào.
