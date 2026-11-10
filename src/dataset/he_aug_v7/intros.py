"""Natural-language openings of the user turn, keyed by function name.
`{f}` is replaced by the signature, e.g. count_ending_with_one(n)."""

HELPER_PAL = (
    "\n\nThe helper function `is_palindrome(string)`, which tests whether a string is a palindrome, "
    "is already provided as part of the solution."
)

INTRO = {
    # ---- 10 (HumanEval/10 make_palindrome)
    "palindrome_by_prepending": (
        "You are given a string. Your task is to implement a function `{f}` that returns the shortest "
        "palindrome that ends with the given string, by prepending characters to its beginning. "
        "The idea is simple: find the longest prefix of the string that is a palindrome, then prepend to "
        "the beginning of the string the reverse of the suffix that comes after that palindromic prefix."
    ) + HELPER_PAL,
    "longest_palindromic_suffix": (
        "You are given a string. Your task is to implement a function `{f}` that finds and returns the "
        "longest suffix (postfix) of the string that is a palindrome. The empty string counts as a "
        "palindrome, so a result always exists."
    ) + HELPER_PAL,
    "min_appends_for_palindrome": (
        "You are given a string. Your task is to implement a function `{f}` that returns the minimal "
        "number of characters that have to be appended to the end of the string so that the result "
        "is a palindrome."
    ) + HELPER_PAL,
    "make_palindrome_nocase": (
        "You are given a string. Your task is to implement a function `{f}` that returns the shortest "
        "palindrome that begins with the given string, where palindromes are checked ignoring letter "
        "case (for example, 'Aba' is a palindrome). The given string itself is kept unchanged. "
        "To build the answer, find the longest suffix of the string that is a palindrome ignoring case, "
        "and append to the end of the string the reverse of the prefix that comes before that suffix."
    ) + HELPER_PAL,
    "count_palindromic_suffixes": (
        "You are given a string. Your task is to implement a function `{f}` that counts how many "
        "non-empty suffixes of the string are palindromes. Suffixes that start at different positions "
        "are counted separately, even if they are equal as strings."
    ) + HELPER_PAL,
    # ---- 12 (longest)
    "shortest": (
        "You are given a list of strings. Your task is to implement a function `{f}` that returns the "
        "shortest string in the list. If several strings share the shortest length, return the first "
        "one. If the list is empty, return `None`."
    ),
    "longest_last": (
        "You are given a list of strings. Your task is to implement a function `{f}` that returns the "
        "longest string in the list. If several strings share the longest length, return the last "
        "one. If the list is empty, return `None`."
    ),
    "longest_word": (
        "You are given a sentence whose words are separated by one or more spaces. Your task is to "
        "implement a function `{f}` that returns the longest word of the sentence, or the first one "
        "if several words have the same maximal length. If the sentence contains no words, return an "
        "empty string."
    ),
    "index_of_longest": (
        "You are given a list of strings. Your task is to implement a function `{f}` that returns the "
        "index of the longest string in the list. If several strings share the longest length, return "
        "the index of the first one. If the list is empty, return -1."
    ),
    "longest_common_prefix": (
        "You are given a list of strings. Your task is to implement a function `{f}` that returns the "
        "longest string that is a prefix of every string in the list. Return an empty string if the "
        "list is empty or the strings have no common prefix."
    ),
    # ---- 15 (string_sequence)
    "count_down_string": (
        "You are given a non-negative integer `n`. Your task is to implement a function `{f}` that "
        "returns a string of space-delimited numbers counting down from `n` to 0 inclusive."
    ),
    "string_sequence_step": (
        "You are given a non-negative integer `n` and a positive integer `step`. Your task is to "
        "implement a function `{f}` that returns a string of space-delimited numbers starting from 0 "
        "up to `n` inclusive, increasing by `step` each time."
    ),
    "even_sequence": (
        "You are given a non-negative integer `n`. Your task is to implement a function `{f}` that "
        "returns a string containing the space-delimited even numbers from 0 up to `n` inclusive."
    ),
    "string_range": (
        "You are given two integers `a` and `b`. Your task is to implement a function `{f}` that "
        "returns a string of comma-delimited numbers going from `a` to `b` inclusive. If `a` is "
        "greater than `b`, the numbers go down from `a` to `b`."
    ),
    "squares_sequence": (
        "You are given a non-negative integer `n`. Your task is to implement a function `{f}` that "
        "returns a string of space-delimited squares of the numbers from 0 up to `n` inclusive."
    ),
    # ---- 22 (filter_integers)
    "filter_strings": (
        "You are given a list containing values of any Python type. Your task is to implement a "
        "function `{f}` that returns a list with only the values that are strings, keeping their order."
    ),
    "filter_floats": (
        "You are given a list containing values of any Python type. Your task is to implement a "
        "function `{f}` that returns a list with only the floating point numbers, keeping their order. "
        "Integers and booleans are not floats."
    ),
    "filter_lists": (
        "You are given a list containing values of any Python type. Your task is to implement a "
        "function `{f}` that returns a list with only the values that are lists, keeping their order. "
        "Tuples and other containers are not lists."
    ),
    "filter_dicts": (
        "You are given a list containing values of any Python type. Your task is to implement a "
        "function `{f}` that returns a list with only the values that are dictionaries, keeping their order."
    ),
    "squares_of_integers": (
        "You are given a list containing values of any Python type. Your task is to implement a "
        "function `{f}` that keeps only the integers and returns their squares in the original order. "
        "Note that in Python a boolean is also an integer (`True` is 1, `False` is 0)."
    ),
    # ---- 25 (factorize)
    "distinct_prime_factors": (
        "You are given an integer `n`. Your task is to implement a function `{f}` that returns the "
        "list of distinct prime factors of `n` from smallest to largest. Each prime factor is listed "
        "only once, no matter how many times it divides `n`. For `n = 1` the list is empty."
    ),
    "count_prime_factors": (
        "You are given an integer `n`. Your task is to implement a function `{f}` that returns the "
        "number of prime factors of `n`, counted with multiplicity (the product of all of them equals "
        "`n`). For `n = 1` the answer is 0."
    ),
    "factorize_with_exponents": (
        "You are given an integer `n`. Your task is to implement a function `{f}` that returns the "
        "prime factorization of `n` as a list of `(prime, exponent)` pairs, ordered by prime from "
        "smallest to largest, so that `n` equals the product of `prime ** exponent` over all pairs. "
        "For `n = 1` the list is empty."
    ),
    "largest_prime_factor": (
        "You are given an integer `n` greater than 1. Your task is to implement a function `{f}` that "
        "returns the largest prime factor of `n`."
    ),
    "sum_of_prime_factors": (
        "You are given an integer `n`. Your task is to implement a function `{f}` that returns the sum "
        "of the prime factors of `n`, where each factor is added as many times as it appears in the "
        "factorization. For `n = 1` the sum is 0."
    ),
    # ---- 26 (remove_duplicates)
    "keep_duplicates": (
        "You are given a list of integers. Your task is to implement a function `{f}` that keeps only "
        "the elements that occur more than once in the list (all of their occurrences), preserving the "
        "original order."
    ),
    "unique_in_order": (
        "You are given a list of integers. Your task is to implement a function `{f}` that removes "
        "repeated elements so that every value stays only once, at the position of its first occurrence."
    ),
    "remove_adjacent_duplicates": (
        "You are given a list of integers. Your task is to implement a function `{f}` that collapses "
        "every run of equal neighbouring elements into a single element. Equal elements that are not "
        "neighbours are kept."
    ),
    "first_unique": (
        "You are given a list of integers. Your task is to implement a function `{f}` that returns the "
        "first element that occurs exactly once in the list, or `None` if there is no such element."
    ),
    "remove_repeated_words": (
        "You are given a list of words. Your task is to implement a function `{f}` that removes all "
        "words that occur more than once, ignoring letter case ('Cat' and 'cat' are the same word). "
        "The remaining words keep their order and original spelling."
    ),
    # ---- 29 (filter_by_prefix)
    "filter_by_suffix": (
        "You are given a list of strings and a suffix. Your task is to implement a function `{f}` that "
        "returns only the strings that end with the given suffix."
    ),
    "filter_longer_than": (
        "You are given a list of strings and an integer `length`. Your task is to implement a function "
        "`{f}` that returns only the strings that are strictly longer than `length`."
    ),
    "filter_by_prefix_nocase": (
        "You are given a list of strings and a prefix. Your task is to implement a function `{f}` that "
        "returns only the strings that start with the given prefix, ignoring letter case. The returned "
        "strings are unchanged."
    ),
    "reject_prefix": (
        "You are given a list of strings and a prefix. Your task is to implement a function `{f}` that "
        "returns only the strings that do NOT start with the given prefix."
    ),
    "filter_by_prefixes": (
        "You are given a list of strings and a list of prefixes. Your task is to implement a function "
        "`{f}` that returns only the strings that start with at least one of the given prefixes."
    ),
    # ---- 32 (find_zero)
    "find_root_bisection": (
        "You are given the coefficients `xs` of a polynomial `xs[0] + xs[1] * x + ... + xs[n] * x^n` "
        "and an interval `[lo, hi]` on which the polynomial changes sign. Your task is to implement a "
        "function `{f}` that returns a point `x` from `[lo, hi]` where the polynomial is (almost) 0."
    ),
    "horner": (
        "You are given the integer coefficients `xs` of a polynomial, where `xs[0]` is the constant "
        "term, and an integer `x`. Your task is to implement a function `{f}` that evaluates "
        "`xs[0] + xs[1] * x + ... + xs[n] * x^n` using exact integer arithmetic. The value of an empty "
        "polynomial is 0."
    ),
    "poly_multiply": (
        "You are given the coefficients `xs` and `ys` of two polynomials, where the first element is "
        "the constant term. Your task is to implement a function `{f}` that returns the coefficients "
        "of their product in the same form. The product with an empty polynomial is an empty list."
    ),
    "poly_slope": (
        "You are given the coefficients `xs` of a polynomial `xs[0] + xs[1] * x + ... + xs[n] * x^n` "
        "and a point `x`. Your task is to implement a function `{f}` that returns the value of the "
        "derivative of the polynomial at `x`, as a float."
    ),
    "find_zero_odd_degree": (
        "You are given the coefficients `xs` of a polynomial `xs[0] + xs[1] * x + ... + xs[n] * x^n`. "
        "Your task is to implement a function `{f}` that returns one `x` at which the polynomial is 0. "
        "`xs` has an even number of coefficients and a non-zero last coefficient, so a solution is "
        "guaranteed."
    ),
    # ---- 39 (prime_fib)
    "prime_fib_count": (
        "You are given an integer `limit`. Your task is to implement a function `{f}` that returns how "
        "many different Fibonacci numbers not greater than `limit` are also prime."
    ),
    "prime_lucas": (
        "You are given a positive integer `n`. Your task is to implement a function `{f}` that returns "
        "the n-th number that is both a Lucas number and a prime. The Lucas numbers start with "
        "2, 1, 3, 4, 7, 11, 18, 29, ... and every next one is the sum of the previous two."
    ),
    "is_fibonacci_prime": (
        "You are given an integer `n`. Your task is to implement a function `{f}` that returns `True` "
        "if `n` is a Fibonacci number that is also prime, and `False` otherwise."
    ),
    "sum_prime_fib": (
        "You are given a non-negative integer `n`. Your task is to implement a function `{f}` that "
        "returns the sum of the first `n` numbers that are both Fibonacci numbers and prime. The sum "
        "of zero numbers is 0."
    ),
    "largest_prime_fib_at_most": (
        "You are given an integer `limit` (0 ≤ limit ≤ 10^12). Your task is to implement a "
        "function `{f}` that returns the largest number that is a Fibonacci number, is prime, and is "
        "not greater than `limit`. If there is no such number, return `None`."
    ),
    # ---- 76 (is_simple_power)
    "is_perfect_cube": (
        "You are given an integer `x`. Your task is to implement a function `{f}` that returns `True` "
        "if `x` is a perfect cube (the cube of some integer, which may be negative or zero) and "
        "`False` otherwise."
    ),
    "power_exponent": (
        "You are given two positive integers `x` and `n`. Your task is to implement a function `{f}` "
        "that returns the non-negative integer `k` such that `n**k = x`, or -1 if there is no such `k`. "
        "If `n` is 1, then only `x = 1` is a power of `n` (with `k = 0`)."
    ),
    "nearest_power_above": (
        "You are given a positive integer `x` and an integer `n` greater than 1. Your task is to "
        "implement a function `{f}` that returns the smallest power of `n` that is greater than or "
        "equal to `x`. A power of `n` is `n**k` for a non-negative integer `k`."
    ),
    "count_powers_in_range": (
        "You are given an integer `n` greater than 1 and two integers `lo` and `hi` with "
        "`1 <= lo <= hi`. Your task is to implement a function `{f}` that counts how many powers of `n` "
        "lie in the closed range `[lo, hi]`. A power of `n` is `n**k` for a non-negative integer `k` "
        "(so 1 is always a power of `n`)."
    ),
    "is_signed_power": (
        "You are given two integers `x` and `n`, where `n` may be negative or zero. Your task is to "
        "implement a function `{f}` that returns `True` if `x` is a power of `n` and `False` otherwise. "
        "`x` is a power of `n` if `n**k = x` for some non-negative integer `k` (with `n**0 = 1` for "
        "any `n`, including 0)."
    ),
    # ---- 83 (starts_one_ends)
    "starts_and_ends_one": (
        "You are given a positive integer `n`. Your task is to implement a function `{f}` that returns "
        "the number of positive integers with exactly `n` digits that both start and end with the digit 1."
    ),
    "neither_starts_nor_ends_one": (
        "You are given a positive integer `n`. Your task is to implement a function `{f}` that returns "
        "the number of positive integers with exactly `n` digits that neither start nor end with the "
        "digit 1."
    ),
    "count_ending_with_one": (
        "You are given a positive integer `n`. Your task is to implement a function `{f}` that returns "
        "the number of positive integers with exactly `n` digits that end with the digit 1."
    ),
    "starts_or_ends_with_digit": (
        "You are given a positive integer `n` and a digit `d` (0 ≤ d ≤ 9). Your task is to "
        "implement a function `{f}` that returns the number of positive integers with exactly `n` "
        "digits that start or end with the digit `d`. A positive integer never starts with 0."
    ),
    "count_n_digit_palindromes": (
        "You are given a positive integer `n`. Your task is to implement a function `{f}` that returns "
        "the number of positive integers with exactly `n` digits that read the same from left to right "
        "and from right to left."
    ),
    # ---- 86 (anti_shuffle)
    "sort_words_desc": (
        "You are given a string `s` made of words separated by spaces. Your task is to implement a "
        "function `{f}` that replaces every word with a new word whose characters are arranged in "
        "descending order of ASCII value. The order of the words and the blank spaces in the sentence "
        "must be kept."
    ),
    "reverse_each_word": (
        "You are given a string `s` made of words separated by spaces. Your task is to implement a "
        "function `{f}` that writes every word backwards. The order of the words and the blank spaces "
        "in the sentence must be kept."
    ),
    "sort_chars_keep_spaces": (
        "You are given a string `s`. Your task is to implement a function `{f}` that rearranges all "
        "non-space characters in ascending order of ASCII value, while every space stays at its "
        "original position."
    ),
    "capitalize_words": (
        "You are given a string `s` made of words separated by spaces. Your task is to implement a "
        "function `{f}` that makes every word start with an upper case letter, with all its other "
        "letters in lower case. The order of the words and the blank spaces must be kept, and "
        "characters that are not letters stay unchanged."
    ),
    "sort_words_alphabetically": (
        "You are given a string `s` made of words separated by spaces. Your task is to implement a "
        "function `{f}` that rearranges the words in ascending order of ASCII value, while the blank "
        "spaces stay exactly where they were."
    ),
    # ---- 91 (is_bored)
    "count_sentences": (
        "You are given a string `S` of words. Your task is to implement a function `{f}` that counts "
        "the sentences in it. Sentences are delimited by '.', '?' or '!'. A sentence that is empty or "
        "contains only spaces is not counted."
    ),
    "count_exclamations": (
        "You are given a string `S` of words. Your task is to implement a function `{f}` that counts "
        "the sentences that end with '!'. Sentences are delimited by '.', '?' or '!'. A sentence that "
        "is empty or contains only spaces is not counted, so in \"Hi!!\" only the first '!' ends a "
        "sentence. Text after the last delimiter does not end with anything."
    ),
    "count_sentences_starting_with": (
        "You are given a string `S` of words and a word `word`. Your task is to implement a function "
        "`{f}` that counts the sentences whose first word is exactly `word` (case sensitive; a longer "
        "word that only starts with the same letters does not count). Sentences are delimited by "
        "'.', '?' or '!', and words are separated by whitespace."
    ),
    "longest_sentence": (
        "You are given a string `S` of words. Your task is to implement a function `{f}` that finds "
        "the sentence with the most words and returns it without the delimiter and without spaces "
        "around it. Sentences are delimited by '.', '?' or '!', and words are separated by whitespace. "
        "If several sentences have the same number of words, return the first one. Return an empty "
        "string if there are no words."
    ),
    "count_sentences_with_word": (
        "You are given a string `S` of words and a word `word`. Your task is to implement a function "
        "`{f}` that counts the sentences that contain `word` at least once (case sensitive, only whole "
        "words count, so \"I\" is not found inside \"It\"). Sentences are delimited by '.', '?' or "
        "'!', and words are separated by whitespace."
    ),
    # ---- 93 (encode)
    "encode_vowels_back": (
        "You are given a message that contains only letters. Your task is to implement a function "
        "`{f}` that encodes it as follows: swap the case of all letters, and replace every vowel with "
        "the letter that appears 2 places before it in the English alphabet (the alphabet is cyclic, "
        "so 'a' goes to 'y')."
    ),
    "encode_caesar": (
        "You are given a message and an integer `shift`. Your task is to implement a function `{f}` "
        "that replaces every letter with the letter that appears `shift` places after it in the "
        "English alphabet. The alphabet is cyclic, the case of letters is kept, `shift` may be "
        "negative or larger than 26, and characters that are not letters stay unchanged."
    ),
    "mask_vowels": (
        "You are given a message. Your task is to implement a function `{f}` that swaps the case of "
        "all letters and replaces all vowels (a, e, i, o, u in any case) with the character '*'. "
        "Characters that are not letters stay unchanged."
    ),
    "rotate_vowels": (
        "You are given a message. Your task is to implement a function `{f}` that replaces every "
        "vowel with the next vowel in the cycle a -> e -> i -> o -> u -> a. The case of every letter "
        "is kept and all other characters stay unchanged."
    ),
    "swap_and_reverse_words": (
        "You are given a message whose words are separated by single spaces. Your task is to implement "
        "a function `{f}` that swaps the case of all letters and writes every word backwards, keeping "
        "the order of the words. Characters that are not letters stay unchanged."
    ),
    # ---- 96 (count_up_to)
    "count_primes_below": (
        "You are given a non-negative integer `n`. Your task is to implement a function `{f}` that "
        "returns the number of prime numbers that are less than `n`."
    ),
    "primes_between": (
        "You are given two non-negative integers `a` and `b`. Your task is to implement a function "
        "`{f}` that returns an array of all prime numbers `p` with `a <= p <= b` in ascending order. "
        "If `a` is greater than `b`, return an empty array."
    ),
    "largest_prime_below": (
        "You are given a non-negative integer `n`. Your task is to implement a function `{f}` that "
        "returns the largest prime number that is strictly less than `n`. If there is no such prime, "
        "return -1."
    ),
    "twin_primes_below": (
        "You are given a non-negative integer `n`. Your task is to implement a function `{f}` that "
        "returns an array of the pairs `(p, p+2)` where both `p` and `p+2` are prime and `p+2` is "
        "less than `n`. The pairs are listed in ascending order."
    ),
    "sum_primes_below": (
        "You are given a non-negative integer `n`. Your task is to implement a function `{f}` that "
        "returns the sum of all prime numbers that are less than `n`."
    ),
    # ---- 100 (make_a_pile)
    "make_a_pyramid": (
        "You are given a positive integer `n` and you have to build a pyramid of stones. The first "
        "(bottom) level has `n` stones and every next level has 2 stones less than the previous one; "
        "the pyramid ends with the last level that has at least 1 stone. Your task is to implement a "
        "function `{f}` that returns the number of stones in each level as a list, where the element "
        "at index `i` is the number of stones in level `i+1`."
    ),
    "make_a_pile_alternating": (
        "You are given a positive integer `n` and you have to build a pile of `n` levels of stones. "
        "The first level has `n` stones and the number grows alternately by 1 and by 2: the second "
        "level has 1 stone more than the first, the third has 2 more than the second, the fourth has "
        "1 more than the third, and so on. Your task is to implement a function `{f}` that returns the "
        "number of stones in each level as a list, where the element at index `i` is the number of "
        "stones in level `i+1`."
    ),
    "total_stones": (
        "You are given a positive integer `n` and you have to build a pile of `n` levels of stones. "
        "The first level has `n` stones, and each next level has the next odd number of stones if `n` "
        "is odd, or the next even number if `n` is even. Your task is to implement a function `{f}` "
        "that returns the total number of stones in the whole pile."
    ),
    "make_a_triangle_pile": (
        "You are given a positive integer `n` and you have to build a pile of `n` levels of stones. "
        "The first level has 1 stone, the second has 3, the third has 6, and so on: level `i` has "
        "`1 + 2 + ... + i` stones. Your task is to implement a function `{f}` that returns the number "
        "of stones in each level as a list, where the element at index `i` is the number of stones in "
        "level `i+1`."
    ),
    "max_pile_levels": (
        "You have a non-negative integer number of `stones` and want to build a pile where the first "
        "level has 1 stone, the second has 3, the third has 5, and so on (every next level has 2 "
        "stones more than the previous one). Your task is to implement a function `{f}` that returns "
        "the maximal number of levels that can be completely built."
    ),
    # ---- 108 (count_nums)
    "count_nums_negative": (
        "You are given an array of integers. Your task is to implement a function `{f}` that returns "
        "the number of elements whose sum of digits is less than 0. If a number is negative, its "
        "first signed digit is negative: for example, -123 has signed digits -1, 2 and 3."
    ),
    "count_nums_zero": (
        "You are given an array of integers. Your task is to implement a function `{f}` that returns "
        "the number of elements whose sum of digits is equal to 0. If a number is negative, its first "
        "signed digit is negative: for example, -123 has signed digits -1, 2 and 3. The number 0 has "
        "the sum of digits 0."
    ),
    "signed_digit_sums": (
        "You are given an array of integers. Your task is to implement a function `{f}` that returns "
        "the array of the sums of digits of its elements, in the same order. If a number is negative, "
        "its first signed digit is negative: for example, -123 has signed digits -1, 2 and 3, so its "
        "sum is 4."
    ),
    "count_even_digit_sum": (
        "You are given an array of integers. Your task is to implement a function `{f}` that returns "
        "the number of elements whose sum of digits is even. The sign of a number is ignored, e.g. "
        "-123 has digits 1, 2 and 3 with the sum 6. The number 0 has the sum of digits 0."
    ),
    "count_nums_greater": (
        "You are given an array of integers and an integer `k`. Your task is to implement a function "
        "`{f}` that returns the number of elements whose sum of digits is greater than `k`. If a "
        "number is negative, its first signed digit is negative: for example, -123 has signed digits "
        "-1, 2 and 3."
    ),
    # ---- 118 (get_closest_vowel)
    "get_first_vowel_between_consonants": (
        "You are given a word. Your task is to implement a function `{f}` that finds the closest vowel "
        "that stands between two consonants, looking from the left side of the word (case sensitive). "
        "Vowels in the beginning and at the end of the word don't count. Return an empty string if no "
        "vowel meets this condition. You may assume that the word contains English letters only."
    ),
    "count_vowels_between_consonants": (
        "You are given a word. Your task is to implement a function `{f}` that counts the vowels that "
        "stand between two consonants (case sensitive). Vowels in the beginning and at the end of the "
        "word don't count, and a vowel next to another vowel doesn't count either, because it doesn't "
        "have a consonant on both sides. You may assume that the word contains English letters only."
    ),
    "get_closest_consonant": (
        "You are given a word. Your task is to implement a function `{f}` that finds the closest "
        "consonant that stands between two vowels, looking from the right side of the word (case "
        "sensitive). Consonants in the beginning and at the end of the word don't count. Return an "
        "empty string if no consonant meets this condition. You may assume that the word contains "
        "English letters only."
    ),
    "last_vowel_run": (
        "You are given a word. Your task is to implement a function `{f}` that finds the last group of "
        "consecutive vowels that stands between two consonants (case sensitive), looking from the right "
        "side of the word. Groups in the beginning and at the end of the word don't count. Return an "
        "empty string if no group meets this condition. You may assume that the word contains English "
        "letters only."
    ),
    "closest_vowel_index": (
        "You are given a word. Your task is to implement a function `{f}` that finds the position "
        "(0-based index, counted from the left) of the closest vowel that stands between two "
        "consonants, looking from the right side of the word (case sensitive). Vowels in the beginning "
        "and at the end of the word don't count. Return -1 if no vowel meets this condition. You may "
        "assume that the word contains English letters only."
    ),
    # ---- 120 (maximum)
    "minimum": (
        "You are given an array `arr` of integers and a positive integer `k`. Your task is to implement "
        "a function `{f}` that returns a sorted list of length `k` with the `k` smallest numbers in `arr`."
    ),
    "top_k_descending": (
        "You are given an array `arr` of integers and a positive integer `k`. Your task is to implement "
        "a function `{f}` that returns a list of length `k` with the `k` largest numbers in `arr`, "
        "sorted from the largest to the smallest."
    ),
    "kth_largest": (
        "You are given an array `arr` of integers and a positive integer `k`. Your task is to implement "
        "a function `{f}` that returns the `k`-th largest number in `arr`. Equal numbers are counted "
        "separately."
    ),
    "maximum_distinct": (
        "You are given an array `arr` of integers and a positive integer `k`. Your task is to implement "
        "a function `{f}` that returns a sorted list with the `k` largest distinct numbers in `arr`. "
        "If `arr` contains fewer than `k` distinct numbers, return all of them."
    ),
    "sum_of_k_largest": (
        "You are given an array `arr` of integers and a non-negative integer `k`. Your task is to "
        "implement a function `{f}` that returns the sum of the `k` largest numbers in `arr`. The sum "
        "of zero numbers is 0."
    ),
    # ---- 124 (valid_date)
    "valid_date_ymd": (
        "You are given a date string. Your task is to implement a function `{f}` that returns `True` "
        "if it is a valid date in the format yyyy-mm-dd, and `False` otherwise. The year, month and "
        "day have exactly 4, 2 and 2 digits. February has 29 days in a leap year (divisible by 4, "
        "except centuries not divisible by 400), otherwise 28."
    ),
    "valid_time": (
        "You are given a time string. Your task is to implement a function `{f}` that returns `True` "
        "if it is a valid time and `False` otherwise. The time should be in the format hh:mm:ss with "
        "exactly two digits for each part; the hours should be between 00 and 23, and the minutes and "
        "the seconds between 00 and 59."
    ),
    "valid_date_dmy": (
        "You are given a date string. Your task is to implement a function `{f}` that returns `True` "
        "if it is a valid date in the format dd/mm/yyyy (exactly 2, 2 and 4 digits), else `False`. "
        "The month is 1-12; the day is 1-31 for months 1, 3, 5, 7, 8, 10, 12, 1-30 for months "
        "4, 6, 9, 11, and 1-29 for month 2."
    ),
    "valid_ipv4": (
        "You are given an IPv4 address string. Your task is to implement a function `{f}` that returns "
        "`True` if the address is valid and `False` otherwise. The address consists of exactly four "
        "parts separated by single dots. Every part contains only decimal digits, is a number between "
        "0 and 255 inclusive, and is written without leading zeros (the number 0 itself is written "
        "as a single '0')."
    ),
    "valid_hex_color": (
        "You are given a color code string. Your task is to implement a function `{f}` that returns "
        "`True` if the code is valid and `False` otherwise. The code is valid if it starts with the "
        "character '#', is followed by exactly 3 or exactly 6 characters, and all these characters "
        "are hexadecimal digits (0-9, a-f or A-F)."
    ),
    # ---- 126 (is_sorted)
    "is_sorted_desc": (
        "You are given a list of non-negative integers. Your task is to implement a function `{f}` "
        "that returns whether or not they are sorted in descending order. If the list has more than 2 "
        "duplicates of the same number, return `False`."
    ),
    "is_strictly_sorted": (
        "You are given a list of integers, which may be negative. Your task is to implement a function "
        "`{f}` that returns whether or not they are sorted in strictly ascending order. If the list "
        "has any duplicate numbers, return `False`."
    ),
    "is_sorted_limit": (
        "You are given a list of integers, which may be negative, and a positive integer `limit`. Your "
        "task is to implement a function `{f}` that returns whether or not the numbers are sorted in "
        "ascending order (equal neighbours are allowed). If some number appears in the list more than "
        "`limit` times, return `False`."
    ),
    "is_sorted_with_negatives": (
        "You are given a list of integers, which may be negative. Your task is to implement a function "
        "`{f}` that returns whether or not they are sorted in ascending order. If the list has more "
        "than 2 duplicates of the same number, return `False`."
    ),
    "is_sorted_words": (
        "You are given a list of lowercase words. Your task is to implement a function `{f}` that "
        "returns whether or not they are sorted in ascending alphabetical (lexicographic) order. If "
        "some word appears in the list more than 2 times, return `False`."
    ),
    # ---- 129 (minPath)
    "max_path": (
        "You are given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly "
        "once, and an integer `k`. A path starts at any cell and each step moves to an edge-adjacent "
        "cell (cells may repeat). Your task is to implement a function `{f}` that returns the "
        "lexicographically largest list of values collected by a path of `k` cells."
    ),
    "min_path_from": (
        "You are given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly "
        "once, an integer `k`, and a start cell `(row, col)`. Each step of a path moves to an "
        "edge-adjacent cell (cells may repeat). Your task is to implement `{f}`, returning the "
        "lexicographically smallest list of values collected by a path of `k` cells that starts at "
        "the start cell."
    ),
    "min_path_sum": (
        "You are given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly "
        "once, and an integer `k`. A path starts at any cell and each step moves to an edge-adjacent "
        "cell (cells may repeat). Your task is to implement a function `{f}` that finds the "
        "lexicographically smallest list of values collected by a path of `k` cells and returns the "
        "sum of that list."
    ),
    "grid_neighbors": (
        "You are given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly "
        "once, and an integer `value`. Your task is to implement `{f}`, returning the sorted list of "
        "values on the cells sharing an edge with the cell that contains `value` (an empty list if "
        "`value` is not in the grid)."
    ),
    "find_cell": (
        "You are given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly "
        "once, and an integer `value`. Your task is to implement a function `{f}` that returns a "
        "tuple `(row, col)` with the 0-indexed position of the cell containing `value`, or `(-1, -1)` "
        "if `value` is not in the grid."
    ),
    # ---- 130 (tri)
    "pell": (
        "Pell numbers are a sequence every mathematician has met in Diophantine equations. The "
        "sequence is defined by the recurrence: pell(0) = 0, pell(1) = 1, and "
        "pell(n) = 2 * pell(n - 1) + pell(n - 2) for n >= 2. Your task is to implement a function "
        "`{f}` that returns the n-th Pell number."
    ),
    "padovan": (
        "The Padovan sequence is defined by the recurrence: padovan(0) = padovan(1) = padovan(2) = 1, "
        "and padovan(n) = padovan(n - 2) + padovan(n - 3) for n >= 3. Your task is to implement a "
        "function `{f}` that returns the n-th Padovan number."
    ),
    "look_ahead_seq": (
        "Consider a sequence whose elements depend on their neighbours: seq(0) = 1; "
        "seq(n) = 1 + n / 2 if n is even; and seq(n) = seq(n - 1) + seq(n + 1) if n is odd. "
        "Given a non-negative integer `n`, your task is to implement a function `{f}` that returns "
        "a list of the first `n + 1` numbers of the sequence."
    ),
    "tribonacci": (
        "The Tribonacci sequence is defined by the recurrence: tribonacci(0) = 0, tribonacci(1) = 0, "
        "tribonacci(2) = 1, and tribonacci(n) = tribonacci(n - 1) + tribonacci(n - 2) + "
        "tribonacci(n - 3) for n >= 3. Your task is to implement a function `{f}` that returns the "
        "n-th Tribonacci number."
    ),
    "jacobsthal": (
        "The Jacobsthal sequence is defined by the recurrence: jacobsthal(0) = 0, jacobsthal(1) = 1, "
        "and jacobsthal(n) = jacobsthal(n - 1) + 2 * jacobsthal(n - 2) for n >= 2. Your task is to "
        "implement a function `{f}` that returns the n-th Jacobsthal number."
    ),
    # ---- 132 (is_nested)
    "max_nesting_depth": (
        "You are given a string that contains only square brackets. Your task is to implement a "
        "function `{f}` that returns the maximal nesting depth of the brackets, where every '[' "
        "increases the depth by one and every ']' decreases it by one, but the depth never goes below "
        "zero (a ']' without a matching '[' before it is ignored)."
    ),
    "is_balanced": (
        "You are given a string that contains only square brackets. Your task is to implement a "
        "function `{f}` that returns `True` if and only if the brackets form a valid sequence: every "
        "'[' is closed by a later ']' and every ']' closes an earlier '['. The empty string is valid."
    ),
    "has_nesting_depth": (
        "You are given a string of square brackets and a positive integer `k`. Your task is to "
        "implement a function `{f}` that returns `True` if and only if the string contains a "
        "subsequence (skipping characters is allowed) equal to '[' * k + ']' * k."
    ),
    "longest_balanced_subsequence": (
        "You are given a string that contains only square brackets. Your task is to implement a "
        "function `{f}` that returns the length of the longest subsequence of the string (some "
        "characters may be skipped, the order is kept) that is a valid sequence of brackets: every "
        "'[' is closed by a later ']' and every ']' closes an earlier '['."
    ),
    "first_unbalanced_index": (
        "You are given a string that contains only square brackets. Your task is to implement a "
        "function `{f}` that returns -1 if the brackets form a valid sequence (every '[' is closed by "
        "a later ']' and every ']' closes an earlier '['). Otherwise it returns the index of the first "
        "']' that has no matching '[' before it; if there is no such ']' but some '[' stay unclosed at "
        "the end, it returns the length of the string."
    ),
    # ---- 139 (special_factorial)
    "factorial_sum": (
        "The factorial sum is defined as factorial_sum(n) = n! + (n-1)! + (n-2)! + ... + 1!, where "
        "n > 0. Your task is to implement a function `{f}` that computes it for a given integer `n`."
    ),
    "double_factorial": (
        "The double factorial is defined as double_factorial(n) = n * (n-2) * (n-4) * ... down to 2 "
        "(if n is even) or down to 1 (if n is odd), where n >= 0 and the double factorial of 0 is 1. "
        "Your task is to implement a function `{f}` that computes it for a given integer `n`."
    ),
    "special_factorial_mod": (
        "The Brazilian factorial is defined as brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!, "
        "where n > 0. You are given two integers `n > 0` and `m > 0`. Your task is to implement a "
        "function `{f}` that returns the remainder of the division of the Brazilian factorial of `n` "
        "by `m`."
    ),
    "primorial": (
        "The primorial is defined as the product of all prime numbers that are not greater than `n`: "
        "primorial(n) = 2 * 3 * 5 * 7 * ..., where n >= 0 and the product of no numbers is 1. Your "
        "task is to implement a function `{f}` that computes it for a given integer `n`."
    ),
    "hyperfactorial": (
        "The hyperfactorial is defined as hyperfactorial(n) = 1^1 * 2^2 * 3^3 * ... * n^n, where "
        "n > 0. Your task is to implement a function `{f}` that computes it for a given integer `n`."
    ),
    # ---- 144 (simplify)
    "simplify_sum": (
        "You are given two fractions `x` and `n`, each a string of the form <numerator>/<denominator> "
        "where both parts are positive whole numbers (no zero denominators). Your task is to implement "
        "a function `{f}` that returns `True` if the expression `x + n` evaluates to a whole number "
        "and `False` otherwise."
    ),
    "simplify_quotient": (
        "You are given two fractions `x` and `n`, each a string of the form <numerator>/<denominator> "
        "where both parts are positive whole numbers (no zero denominators). Your task is to implement "
        "a function `{f}` that returns `True` if the expression `x / n` evaluates to a whole number "
        "and `False` otherwise."
    ),
    "product_fraction": (
        "You are given two fractions `x` and `n`, each a string of the form <numerator>/<denominator> "
        "with positive whole numbers and no zero denominator. Your task is to implement a function "
        "`{f}` that multiplies them and returns the result in lowest terms as a string "
        "<numerator>/<denominator> (a whole number has denominator 1)."
    ),
    "fraction_less": (
        "You are given two fractions `x` and `n`, each a string of the form <numerator>/<denominator> "
        "where both parts are positive whole numbers. You can assume that they are valid and do not "
        "have zero as denominator. Your task is to implement a function `{f}` that returns `True` if "
        "`x` is strictly less than `n` and `False` otherwise."
    ),
    "is_reducible": (
        "You are given a fraction `x` as a string of the form <numerator>/<denominator> where both "
        "parts are positive whole numbers. You can assume that it is valid and does not have zero as "
        "denominator. Your task is to implement a function `{f}` that returns `True` if the numerator "
        "and the denominator have a common divisor greater than 1 (that is, the fraction can be "
        "reduced), and `False` otherwise."
    ),
    # ---- 145 (order_by_points)
    "order_by_digit_count": (
        "You are given a list of integers. Your task is to implement a function `{f}` that sorts it in "
        "ascending order according to the number of digits of each number (the sign is not a digit, "
        "and 0 has one digit). If several items have the same number of digits, order them based on "
        "their index in the original list."
    ),
    "order_by_last_digit": (
        "You are given a list of integers. Your task is to implement a function `{f}` that sorts it in "
        "ascending order according to the last digit of the absolute value of each number. If several "
        "items have the same last digit, order them based on their index in the original list."
    ),
    "order_by_points_desc": (
        "You are given a list of integers. Your task is to implement a function `{f}` that sorts it in "
        "descending order according to the sum of the digits of each number. If several items have "
        "the same sum of digits, order them based on their index in the original list. If a number is "
        "negative, its first signed digit is negative: for example, -123 has signed digits -1, 2 and 3."
    ),
    "order_by_abs_digit_sum": (
        "You are given a list of integers. Your task is to implement a function `{f}` that sorts it in "
        "ascending order according to the sum of the digits of the absolute value of each number (the "
        "sign is ignored, so -12 has the sum 3). If several items have the same sum of digits, order "
        "them based on their index in the original list."
    ),
    "rank_by_points": (
        "You are given a list of integers. Your task is to implement a function `{f}` that returns the "
        "list of indexes of the given list arranged in ascending order according to the sum of the "
        "digits of the numbers at these indexes. If several items have the same sum of digits, order "
        "their indexes in ascending order. If a number is negative, its first signed digit is "
        "negative: for example, -123 has signed digits -1, 2 and 3."
    ),
    # ---- 156 (int_to_mini_roman)
    "roman_to_int": (
        "You are given a roman numeral as a lowercase string, which is valid and has a value between "
        "1 and 3999. Your task is to implement a function `{f}` that returns its integer equivalent."
    ),
    "int_to_roman_upper": (
        "You are given a positive integer `number` with 1 <= number <= 3999. Your task is to implement "
        "a function `{f}` that returns its roman numeral equivalent as a string, in uppercase."
    ),
    "roman_length": (
        "You are given a positive integer `number` with 1 <= number <= 3999. Your task is to implement "
        "a function `{f}` that returns the number of characters in its roman numeral equivalent."
    ),
    "int_to_additive_roman": (
        "You are given a positive integer `number` with 1 <= number <= 3999. Your task is to implement "
        "a function `{f}` that returns its roman numeral equivalent as a lowercase string written "
        "without the subtractive notation (so 4 is 'iiii' and 9 is 'viiii'). The greatest possible "
        "symbols are used first (m = 1000, d = 500, c = 100, l = 50, x = 10, v = 5, i = 1)."
    ),
    "is_valid_roman": (
        "You are given a string `s`. Your task is to implement a function `{f}` that returns `True` if "
        "it is a roman numeral written in the standard (shortest) form in lowercase, with a value "
        "between 1 and 3999, and `False` otherwise."
    ),
    # ---- 163 (generate_integers)
    "generate_odd_digits": (
        "You are given two positive integers `a` and `b`. Your task is to implement a function `{f}` "
        "that returns the odd digits between `a` and `b`, in ascending order."
    ),
    "generate_even_digits_desc": (
        "You are given two positive integers `a` and `b`. Your task is to implement a function `{f}` "
        "that returns the even digits between `a` and `b`, in descending order."
    ),
    "count_even_digits": (
        "You are given two positive integers `a` and `b`. Your task is to implement a function `{f}` "
        "that returns how many even digits there are between `a` and `b` inclusive. Only the digits "
        "2, 4, 6 and 8 are counted."
    ),
    "generate_prime_digits": (
        "You are given two positive integers `a` and `b`. Your task is to implement a function `{f}` "
        "that returns the prime digits between `a` and `b`, in ascending order."
    ),
    "sum_even_digits": (
        "You are given two positive integers `a` and `b`. Your task is to implement a function `{f}` "
        "that returns the sum of the even digits between `a` and `b`. Only the digits 2, 4, 6 and 8 "
        "are summed, and the sum of no digits is 0."
    ),
}
