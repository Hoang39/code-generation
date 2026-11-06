# parents: HumanEval/100 (make_a_pile), /108 (count_nums), /118 (get_closest_vowel), /120 (maximum), /124 (valid_date)
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------------------------------------------------------- HumanEval/100
add(100, '''def make_a_pyramid(n):
    """
    Given a positive integer n, you have to make a pyramid of stones.
    The first (bottom) level has n stones.
    Every next level has 2 stones less than the previous one, and the pyramid
    ends with the last level that has at least 1 stone.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pyramid(5)
    [5, 3, 1]
    >>> make_a_pyramid(6)
    [6, 4, 2]
    """
''', '''
    return list(range(n, 0, -2))
''', '''
assert make_a_pyramid(1) == [1]
assert make_a_pyramid(2) == [2]
assert make_a_pyramid(3) == [3, 1]
assert make_a_pyramid(4) == [4, 2]
assert make_a_pyramid(5) == [5, 3, 1]
assert make_a_pyramid(6) == [6, 4, 2]
assert make_a_pyramid(7) == [7, 5, 3, 1]
assert make_a_pyramid(10) == [10, 8, 6, 4, 2]
assert make_a_pyramid(11) == [11, 9, 7, 5, 3, 1]
for n in range(1, 300):
    r = make_a_pyramid(n)
    assert len(r) == (n + 1) // 2
    assert r[0] == n and r[-1] in (1, 2)
    assert all(a - b == 2 for a, b in zip(r, r[1:]))
    assert all(x >= 1 for x in r)
big = make_a_pyramid(10 ** 6)
assert len(big) == 500000 and big[-1] == 2 and big[1] == 10 ** 6 - 2
assert make_a_pyramid(10 ** 6 + 1)[-1] == 1
''')

add(100, '''def make_a_pile_alternating(n):
    """
    Given a positive integer n, make a pile of n levels of stones.
    The first level has n stones and the number of stones grows alternately by 1 and by 2:
    the second level has 1 stone more than the first, the third has 2 more than the second,
    the fourth has 1 more than the third, and so on.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile_alternating(3)
    [3, 4, 6]
    >>> make_a_pile_alternating(5)
    [5, 6, 8, 9, 11]
    """
''', '''
    ans, num = [], n
    for i in range(n):
        ans.append(num)
        num += 1 if i % 2 == 0 else 2
    return ans
''', '''
assert make_a_pile_alternating(1) == [1]
assert make_a_pile_alternating(2) == [2, 3]
assert make_a_pile_alternating(3) == [3, 4, 6]
assert make_a_pile_alternating(4) == [4, 5, 7, 8]
assert make_a_pile_alternating(5) == [5, 6, 8, 9, 11]
assert make_a_pile_alternating(6) == [6, 7, 9, 10, 12, 13]
assert make_a_pile_alternating(8) == [8, 9, 11, 12, 14, 15, 17, 18]
for n in range(1, 200):
    r = make_a_pile_alternating(n)
    assert len(r) == n and r[0] == n
    assert [b - a for a, b in zip(r, r[1:])] == [1 if i % 2 == 0 else 2 for i in range(n - 1)]
big = make_a_pile_alternating(10 ** 6)
assert len(big) == 10 ** 6
assert big[2] == 10 ** 6 + 3
assert big[-1] - big[0] == 3 * ((10 ** 6 - 1) // 2) + ((10 ** 6 - 1) % 2)
''')

add(100, '''def total_stones(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the total number of stones in the whole pile.

    Examples:
    >>> total_stones(1)
    1
    >>> total_stones(3)
    15
    """
''', '''
    return 2 * n * n - n
''', '''
def ref(n):
    return sum(n + 2 * i for i in range(n))
assert total_stones(1) == 1
assert total_stones(2) == 6
assert total_stones(3) == 15
assert total_stones(4) == 28
assert total_stones(5) == 45
assert total_stones(10) == 190
assert total_stones(100) == 19900
assert total_stones(10 ** 6) == 2 * 10 ** 12 - 10 ** 6
assert total_stones(10 ** 12) == 2 * 10 ** 24 - 10 ** 12
assert total_stones(10 ** 18) == 2 * 10 ** 36 - 10 ** 18
for n in range(1, 500):
    assert total_stones(n) == ref(n), n
assert isinstance(total_stones(7), int)
assert total_stones(7) == 91
''')

add(100, '''def make_a_triangle_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has 1 stone, the second level has 3 stones, the third level has 6 stones,
    and so on: level i has 1 + 2 + ... + i stones.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_triangle_pile(3)
    [1, 3, 6]
    >>> make_a_triangle_pile(5)
    [1, 3, 6, 10, 15]
    """
''', '''
    ans, num = [], 0
    for i in range(1, n + 1):
        num += i
        ans.append(num)
    return ans
''', '''
assert make_a_triangle_pile(1) == [1]
assert make_a_triangle_pile(2) == [1, 3]
assert make_a_triangle_pile(3) == [1, 3, 6]
assert make_a_triangle_pile(4) == [1, 3, 6, 10]
assert make_a_triangle_pile(5) == [1, 3, 6, 10, 15]
assert make_a_triangle_pile(7) == [1, 3, 6, 10, 15, 21, 28]
assert make_a_triangle_pile(6) == [1, 3, 6, 10, 15, 21]
assert make_a_triangle_pile(8)[-1] == 36
assert make_a_triangle_pile(10)[-1] == 55
for n in range(1, 300):
    r = make_a_triangle_pile(n)
    assert r == [i * (i + 1) // 2 for i in range(1, n + 1)]
    assert len(r) == n
big = make_a_triangle_pile(10 ** 6)
assert big[-1] == 10 ** 6 * (10 ** 6 + 1) // 2 and len(big) == 10 ** 6
assert big[0] == 1 and big[1] == 3
''')

add(100, '''def max_pile_levels(stones):
    """
    You have a non-negative integer number of stones and you want to build a pile where
    the first level has 1 stone, the second level has 3 stones, the third level has 5 stones,
    and so on (every next level has 2 stones more than the previous one).
    Return the maximal number of levels that can be completely built.

    Examples:
    >>> max_pile_levels(0)
    0
    >>> max_pile_levels(9)
    3
    >>> max_pile_levels(10)
    3
    """
''', '''
    levels = 0
    while (levels + 1) * (levels + 1) <= stones:
        levels += 1
    return levels
''', '''
import math
assert max_pile_levels(0) == 0
assert max_pile_levels(1) == 1
assert max_pile_levels(2) == 1
assert max_pile_levels(3) == 1
assert max_pile_levels(4) == 2
assert max_pile_levels(8) == 2
assert max_pile_levels(9) == 3
assert max_pile_levels(10) == 3
assert max_pile_levels(15) == 3
assert max_pile_levels(16) == 4
assert max_pile_levels(99) == 9
assert max_pile_levels(100) == 10
assert max_pile_levels(10 ** 6) == 1000
assert max_pile_levels(10 ** 6 - 1) == 999
assert max_pile_levels(10 ** 10) == 10 ** 5
assert max_pile_levels(10 ** 10 - 1) == 10 ** 5 - 1
assert max_pile_levels(10 ** 11) == 316227
for s in range(0, 2000):
    assert max_pile_levels(s) == math.isqrt(s), s
''')

# ---------------------------------------------------------------- HumanEval/108
add(108, '''def count_nums_negative(arr):
    """
    Write a function count_nums_negative which takes an array of integers and returns
    the number of elements which has a sum of digits < 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums_negative([]) == 0
    >>> count_nums_negative([-1, 11, -11]) == 1
    >>> count_nums_negative([-12, -3, 5]) == 1
    """
''', '''
    def signed_sum(x):
        digits = [int(c) for c in str(abs(x))]
        if x < 0:
            digits[0] = -digits[0]
        return sum(digits)
    return sum(1 for x in arr if signed_sum(x) < 0)
''', '''
def ref(x):
    s = str(x)
    if s[0] == "-":
        d = [int(c) for c in s[1:]]
        d[0] = -d[0]
    else:
        d = [int(c) for c in s]
    return sum(d)
assert count_nums_negative([]) == 0
assert count_nums_negative([0]) == 0
assert count_nums_negative([-1]) == 1
assert count_nums_negative([-1, 11, -11]) == 1
assert count_nums_negative([-12, -3, 5]) == 1
assert count_nums_negative([-11]) == 0
assert count_nums_negative([-10]) == 1
assert count_nums_negative([-19]) == 0
assert count_nums_negative([-18, -17]) == 0
assert count_nums_negative([-100, -101]) == 1
assert count_nums_negative([-91, -90]) == 2
assert count_nums_negative([1, 2, 3, 99]) == 0
assert count_nums_negative([-5, -5, -5]) == 3
assert count_nums_negative([-1000000000]) == 1
assert count_nums_negative([-999999999]) == 0
assert count_nums_negative([-1, -2, 5, 0, -90, 123]) == 3
for x in range(-3000, 3000):
    assert count_nums_negative([x]) == (1 if ref(x) < 0 else 0), x
assert count_nums_negative(list(range(-3000, 3000))) == sum(1 for x in range(-3000, 3000) if ref(x) < 0)
assert count_nums_negative([-1] * 100000) == 100000
''')

add(108, '''def count_nums_zero(arr):
    """
    Write a function count_nums_zero which takes an array of integers and returns
    the number of elements which has a sum of digits equal to 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    The number 0 has the sum of digits 0.
    >>> count_nums_zero([]) == 0
    >>> count_nums_zero([-1, 11, -11]) == 1
    >>> count_nums_zero([0, 10, -10]) == 1
    """
''', '''
    def signed_sum(x):
        digits = [int(c) for c in str(abs(x))]
        if x < 0:
            digits[0] = -digits[0]
        return sum(digits)
    return sum(1 for x in arr if signed_sum(x) == 0)
''', '''
def ref(x):
    s = str(x)
    if s[0] == "-":
        d = [int(c) for c in s[1:]]
        d[0] = -d[0]
    else:
        d = [int(c) for c in s]
    return sum(d)
assert count_nums_zero([]) == 0
assert count_nums_zero([0]) == 1
assert count_nums_zero([0, 0, 0]) == 3
assert count_nums_zero([-1, 11, -11]) == 1
assert count_nums_zero([0, 10, -10]) == 1
assert count_nums_zero([-10]) == 0
assert count_nums_zero([-11]) == 1
assert count_nums_zero([-22, -21, -23]) == 1
assert count_nums_zero([-101, -110]) == 2
assert count_nums_zero([-1, 1]) == 0
assert count_nums_zero([100, 1000]) == 0
assert count_nums_zero([-9000000000, -1000000001]) == 1
assert count_nums_zero([-1000000001]) == 1
assert count_nums_zero([-9000000000]) == 0
assert count_nums_zero([-1100000000]) == 1
for x in range(-3000, 3000):
    assert count_nums_zero([x]) == (1 if ref(x) == 0 else 0), x
assert count_nums_zero(list(range(-3000, 3000))) == sum(1 for x in range(-3000, 3000) if ref(x) == 0)
assert count_nums_zero([0] * 100000) == 100000
''')

add(108, '''def signed_digit_sums(arr):
    """
    Write a function signed_digit_sums which takes an array of integers and returns
    the array of the sums of digits of its elements, in the same order.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3, so its sum is 4.
    >>> signed_digit_sums([]) == []
    >>> signed_digit_sums([-1, 11, -11]) == [-1, 2, 0]
    >>> signed_digit_sums([123, -123, 0]) == [6, 4, 0]
    """
''', '''
    def signed_sum(x):
        digits = [int(c) for c in str(abs(x))]
        if x < 0:
            digits[0] = -digits[0]
        return sum(digits)
    return [signed_sum(x) for x in arr]
''', '''
assert signed_digit_sums([]) == []
assert signed_digit_sums([0]) == [0]
assert signed_digit_sums([-1, 11, -11]) == [-1, 2, 0]
assert signed_digit_sums([123, -123, 0]) == [6, 4, 0]
assert signed_digit_sums([-5]) == [-5]
assert signed_digit_sums([-10]) == [-1]
assert signed_digit_sums([-99]) == [0]
assert signed_digit_sums([-100, 100]) == [-1, 1]
assert signed_digit_sums([9, 99, 999]) == [9, 18, 27]
assert signed_digit_sums([-909]) == [0]
assert signed_digit_sums([-1000000007]) == [6]
assert signed_digit_sums([10 ** 18 - 1]) == [162]
assert signed_digit_sums([-(10 ** 18 - 1)]) == [144]
x = [-1, 2]
signed_digit_sums(x)
assert x == [-1, 2]
for v in range(-3000, 3000):
    d = [int(c) for c in str(abs(v))]
    if v < 0:
        d[0] = -d[0]
    assert signed_digit_sums([v]) == [sum(d)], v
assert len(signed_digit_sums(list(range(100000)))) == 100000
''')

add(108, '''def count_even_digit_sum(arr):
    """
    Write a function count_even_digit_sum which takes an array of integers and returns
    the number of elements whose sum of digits is even. The sign of a number is ignored,
    e.g. -123 has digits 1, 2 and 3 with the sum 6. The number 0 has the sum of digits 0.
    >>> count_even_digit_sum([]) == 0
    >>> count_even_digit_sum([-1, 11, -11]) == 2
    >>> count_even_digit_sum([0, 12, 13]) == 2
    """
''', '''
    return sum(1 for x in arr if sum(int(c) for c in str(abs(x))) % 2 == 0)
''', '''
assert count_even_digit_sum([]) == 0
assert count_even_digit_sum([0]) == 1
assert count_even_digit_sum([1]) == 0
assert count_even_digit_sum([-1, 11, -11]) == 2
assert count_even_digit_sum([0, 12, 13]) == 2
assert count_even_digit_sum([-2, -3]) == 1
assert count_even_digit_sum([10, 100, 1000]) == 0
assert count_even_digit_sum([11, 101, 110]) == 3
assert count_even_digit_sum([-123]) == 1
assert count_even_digit_sum([99, -99]) == 2
assert count_even_digit_sum([-20, 20]) == 2
assert count_even_digit_sum([123456789]) == 0
assert count_even_digit_sum([10 ** 18]) == 0
assert count_even_digit_sum([10 ** 18 + 1]) == 1
for v in range(-2000, 2000):
    assert count_even_digit_sum([v]) == (1 if sum(map(int, str(abs(v)))) % 2 == 0 else 0), v
assert count_even_digit_sum(list(range(1000))) == 500
assert count_even_digit_sum([0] * 100000) == 100000
''')

add(108, '''def count_nums_greater(arr, k):
    """
    Write a function count_nums_greater which takes an array of integers and an integer k,
    and returns the number of elements which has a sum of digits > k.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums_greater([], 0) == 0
    >>> count_nums_greater([-1, 11, -11], 1) == 1
    >>> count_nums_greater([5, 15, 25, -35], 6) == 1
    """
''', '''
    def signed_sum(x):
        digits = [int(c) for c in str(abs(x))]
        if x < 0:
            digits[0] = -digits[0]
        return sum(digits)
    return sum(1 for x in arr if signed_sum(x) > k)
''', '''
def ref(x):
    s = str(x)
    if s[0] == "-":
        d = [int(c) for c in s[1:]]
        d[0] = -d[0]
    else:
        d = [int(c) for c in s]
    return sum(d)
assert count_nums_greater([], 0) == 0
assert count_nums_greater([-1, 11, -11], 1) == 1
assert count_nums_greater([-1, 11, -11], 0) == 1
assert count_nums_greater([-1, 11, -11], -1) == 2
assert count_nums_greater([-1, 11, -11], -2) == 3
assert count_nums_greater([5, 15, 25, -35], 6) == 1
assert count_nums_greater([5, 15, 25, -35], 100) == 0
assert count_nums_greater([5, 15, 25, -35], -100) == 4
assert count_nums_greater([0], 0) == 0
assert count_nums_greater([0], -1) == 1
assert count_nums_greater([99, 999], 17) == 2
assert count_nums_greater([99, 999], 18) == 1
assert count_nums_greater([-99, -999], 0) == 1
assert count_nums_greater([-99, -999], -1) == 2
assert count_nums_greater([-99, -999], 9) == 0
assert count_nums_greater([-99, -999], 8) == 1
assert count_nums_greater([-100], -2) == 1
for v in range(-1500, 1500, 7):
    for k in range(-12, 28, 3):
        assert count_nums_greater([v], k) == (1 if ref(v) > k else 0), (v, k)
assert count_nums_greater(list(range(-3000, 3000)), 10) == sum(1 for x in range(-3000, 3000) if ref(x) > 10)
assert count_nums_greater([7] * 100000, 6) == 100000
''')

# ---------------------------------------------------------------- HumanEval/118
add(118, '''def get_first_vowel_between_consonants(word):
    """You are given a word. Your task is to find the closest vowel that stands between
    two consonants from the left side of the word (case sensitive).

    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition.

    You may assume that the given string contains English letter only.

    Example:
    get_first_vowel_between_consonants("yogurt") ==> "o"
    get_first_vowel_between_consonants("FULL") ==> "U"
    get_first_vowel_between_consonants("quick") ==> ""
    get_first_vowel_between_consonants("ab") ==> ""
    """
''', '''
    vowels = "aeiouAEIOU"
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i]
    return ""
''', '''
V = "aeiouAEIOU"
def ref(w):
    for i in range(len(w)):
        if 0 < i < len(w) - 1 and w[i] in V and w[i - 1] not in V and w[i + 1] not in V:
            return w[i]
    return ""
assert get_first_vowel_between_consonants("yogurt") == "o"
assert get_first_vowel_between_consonants("FULL") == "U"
assert get_first_vowel_between_consonants("quick") == ""
assert get_first_vowel_between_consonants("ab") == ""
assert get_first_vowel_between_consonants("") == ""
assert get_first_vowel_between_consonants("a") == ""
assert get_first_vowel_between_consonants("bab") == "a"
assert get_first_vowel_between_consonants("bad") == "a"
assert get_first_vowel_between_consonants("abe") == ""
assert get_first_vowel_between_consonants("Bed") == "e"
assert get_first_vowel_between_consonants("beat") == ""
assert get_first_vowel_between_consonants("banana") == "a"
assert get_first_vowel_between_consonants("eat") == ""
assert get_first_vowel_between_consonants("bEd") == "E"
assert get_first_vowel_between_consonants("beautiful") == "i"
assert get_first_vowel_between_consonants("aeiou") == ""
assert get_first_vowel_between_consonants("bcd") == ""
assert get_first_vowel_between_consonants("sky") == ""
import itertools
for n in range(0, 7):
    for t in itertools.product("aBb", repeat=n):
        w = "".join(t)
        assert get_first_vowel_between_consonants(w) == ref(w), w
assert get_first_vowel_between_consonants("a" * 100000 + "bab") == "a"
assert get_first_vowel_between_consonants("b" * 100000) == ""
''')

add(118, '''def count_vowels_between_consonants(word):
    """You are given a word. Your task is to count the vowels that stand between
    two consonants (case sensitive).

    Vowels in the beginning and ending doesn't count. A vowel next to another vowel
    doesn't count either, because it doesn't have a consonant on both sides.

    You may assume that the given string contains English letter only.

    Example:
    count_vowels_between_consonants("yogurt") ==> 2
    count_vowels_between_consonants("FULL") ==> 1
    count_vowels_between_consonants("quick") ==> 0
    count_vowels_between_consonants("ab") ==> 0
    """
''', '''
    vowels = "aeiouAEIOU"
    count = 0
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            count += 1
    return count
''', '''
V = "aeiouAEIOU"
def ref(w):
    return sum(1 for i in range(len(w)) if 0 < i < len(w) - 1 and w[i] in V and w[i - 1] not in V and w[i + 1] not in V)
assert count_vowels_between_consonants("yogurt") == 2
assert count_vowels_between_consonants("FULL") == 1
assert count_vowels_between_consonants("quick") == 0
assert count_vowels_between_consonants("ab") == 0
assert count_vowels_between_consonants("") == 0
assert count_vowels_between_consonants("a") == 0
assert count_vowels_between_consonants("bab") == 1
assert count_vowels_between_consonants("banana") == 2
assert count_vowels_between_consonants("bababab") == 3
assert count_vowels_between_consonants("beautiful") == 2
assert count_vowels_between_consonants("aaa") == 0
assert count_vowels_between_consonants("bAb") == 1
assert count_vowels_between_consonants("sky") == 0
assert count_vowels_between_consonants("strength") == 1
assert count_vowels_between_consonants("Education") == 2
assert count_vowels_between_consonants("queue") == 0
import itertools
for n in range(0, 8):
    for t in itertools.product("aBb", repeat=n):
        w = "".join(t)
        assert count_vowels_between_consonants(w) == ref(w), w
assert count_vowels_between_consonants("ba" * 50000 + "b") == 50000
assert count_vowels_between_consonants("b" * 100000) == 0
''')

add(118, '''def get_closest_consonant(word):
    """You are given a word. Your task is to find the closest consonant that stands between
    two vowels from the right side of the word (case sensitive).

    Consonants in the beginning and ending doesn't count. Return empty string if you didn't
    find any consonant met the above condition.

    You may assume that the given string contains English letter only.

    Example:
    get_closest_consonant("banana") ==> "n"
    get_closest_consonant("FULL") ==> ""
    get_closest_consonant("Apple") ==> ""
    get_closest_consonant("area") ==> "r"
    """
''', '''
    vowels = "aeiouAEIOU"
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and word[i - 1] in vowels and word[i + 1] in vowels:
            return word[i]
    return ""
''', '''
V = "aeiouAEIOU"
def ref(w):
    for i in range(len(w) - 2, 0, -1):
        if w[i] not in V and w[i - 1] in V and w[i + 1] in V:
            return w[i]
    return ""
assert get_closest_consonant("banana") == "n"
assert get_closest_consonant("FULL") == ""
assert get_closest_consonant("area") == "r"
assert get_closest_consonant("") == ""
assert get_closest_consonant("a") == ""
assert get_closest_consonant("ab") == ""
assert get_closest_consonant("aba") == "b"
assert get_closest_consonant("ABA") == "B"
assert get_closest_consonant("abe") == "b"
assert get_closest_consonant("abacada") == "d"
assert get_closest_consonant("abacadb") == "c"
assert get_closest_consonant("abcde") == ""
assert get_closest_consonant("education") == "t"
assert get_closest_consonant("beautiful") == "f"
assert get_closest_consonant("eau") == ""
assert get_closest_consonant("aXe") == "X"
assert get_closest_consonant("Apple") == ""
import itertools
for n in range(0, 8):
    for t in itertools.product("aEbC", repeat=n):
        w = "".join(t)
        assert get_closest_consonant(w) == ref(w), w
assert get_closest_consonant("ab" * 100000 + "a") == "b"
assert get_closest_consonant("b" * 100000) == ""
''')

add(118, '''def last_vowel_run(word):
    """You are given a word. Your task is to find the last group of consecutive vowels
    that stands between two consonants (case sensitive), looking from the right side of the word.

    Groups in the beginning and ending of the word don't count. Return empty string if you
    didn't find any group met the above condition.

    You may assume that the given string contains English letter only.

    Example:
    last_vowel_run("yogurt") ==> "u"
    last_vowel_run("beautiful") ==> "u"
    last_vowel_run("queue") ==> ""
    last_vowel_run("moon") ==> "oo"
    last_vowel_run("ab") ==> ""
    """
''', '''
    vowels = "aeiouAEIOU"
    i = len(word) - 1
    while i > 0:
        if word[i] in vowels:
            j = i
            while j > 0 and word[j - 1] in vowels:
                j -= 1
            if j > 0 and i < len(word) - 1:
                return word[j:i + 1]
            i = j - 1
        else:
            i -= 1
    return ""
''', '''
import re
V = "aeiouAEIOU"
def ref(w):
    found = [m.group(1) for m in re.finditer(r"(?<=[^aeiouAEIOU])([aeiouAEIOU]+)(?=[^aeiouAEIOU])", w)]
    return found[-1] if found else ""
assert last_vowel_run("yogurt") == "u"
assert last_vowel_run("beautiful") == "u"
assert last_vowel_run("queue") == ""
assert last_vowel_run("moon") == "oo"
assert last_vowel_run("ab") == ""
assert last_vowel_run("") == ""
assert last_vowel_run("a") == ""
assert last_vowel_run("bab") == "a"
assert last_vowel_run("baab") == "aa"
assert last_vowel_run("baabab") == "a"
assert last_vowel_run("baabaa") == "aa"
assert last_vowel_run("aab") == ""
assert last_vowel_run("bAEb") == "AE"
assert last_vowel_run("bcdfg") == ""
assert last_vowel_run("aeiou") == ""
assert last_vowel_run("rhythm") == ""
assert last_vowel_run("Education") == "io"
assert last_vowel_run("bookkeeper") == "e"
import itertools
for n in range(0, 9):
    for t in itertools.product("aEbC", repeat=n):
        w = "".join(t)
        assert last_vowel_run(w) == ref(w), w
assert last_vowel_run("b" + "a" * 100000 + "b") == "a" * 100000
assert last_vowel_run("ba" * 50000) == "a"
''')

add(118, '''def closest_vowel_index(word):
    """You are given a word. Your task is to find the position (0-based index counted from the
    left side) of the closest vowel that stands between two consonants from the right side
    of the word (case sensitive).

    Vowels in the beginning and ending doesn't count. Return -1 if you didn't
    find any vowel met the above condition.

    You may assume that the given string contains English letter only.

    Example:
    closest_vowel_index("yogurt") ==> 3
    closest_vowel_index("FULL") ==> 1
    closest_vowel_index("quick") ==> -1
    closest_vowel_index("ab") ==> -1
    """
''', '''
    vowels = "aeiouAEIOU"
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return i
    return -1
''', '''
V = "aeiouAEIOU"
def ref(w):
    best = -1
    for i in range(1, len(w) - 1):
        if w[i] in V and w[i - 1] not in V and w[i + 1] not in V:
            best = i
    return best
assert closest_vowel_index("yogurt") == 3
assert closest_vowel_index("FULL") == 1
assert closest_vowel_index("quick") == -1
assert closest_vowel_index("ab") == -1
assert closest_vowel_index("") == -1
assert closest_vowel_index("a") == -1
assert closest_vowel_index("bab") == 1
assert closest_vowel_index("babab") == 3
assert closest_vowel_index("banana") == 3
assert closest_vowel_index("abe") == -1
assert closest_vowel_index("bae") == -1
assert closest_vowel_index("Bed") == 1
assert closest_vowel_index("beautiful") == 7
assert closest_vowel_index("aeiou") == -1
assert closest_vowel_index("bcdf") == -1
assert closest_vowel_index("bobbed") == 4
import itertools
for n in range(0, 8):
    for t in itertools.product("aBb", repeat=n):
        w = "".join(t)
        assert closest_vowel_index(w) == ref(w), w
assert closest_vowel_index("b" * 100000 + "a" + "b" * 100000) == 100000
assert closest_vowel_index("b" * 100000) == -1
''')

# ---------------------------------------------------------------- HumanEval/120
add(120, '''def minimum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list
    of length k with the minimum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 2
        Output: [-4, -3]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [-4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [-3]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
''', '''
    return sorted(arr)[:k]
''', '''
import random
assert minimum([-3, -4, 5], 2) == [-4, -3]
assert minimum([4, -4, 4], 2) == [-4, 4]
assert minimum([-3, 2, 1, 2, -1, -2, 1], 1) == [-3]
assert minimum([1, 2, 3], 0) == []
assert minimum([1, 2, 3], 3) == [1, 2, 3]
assert minimum([3, 2, 1], 3) == [1, 2, 3]
assert minimum([5], 1) == [5]
assert minimum([5, 5, 5], 2) == [5, 5]
assert minimum([0, 0, -1, 0], 2) == [-1, 0]
assert minimum([1000, -1000], 1) == [-1000]
assert minimum([-1000, 1000], 2) == [-1000, 1000]
assert minimum([2, 2, 1, 1], 3) == [1, 1, 2]
a = [3, 1, 2]
minimum(a, 2)
assert a == [3, 1, 2]
random.seed(71)
for _ in range(300):
    L = [random.randint(-1000, 1000) for _ in range(random.randint(1, 30))]
    k = random.randint(0, len(L))
    r = minimum(L, k)
    assert len(r) == k and r == sorted(r) and r == sorted(L)[:k]
big = [random.randint(-1000, 1000) for _ in range(200000)]
assert minimum(big, 5) == sorted(big)[:5]
''')

add(120, '''def top_k_descending(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a list
    of length k with the maximum k numbers in arr, sorted from the largest to the smallest.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [5, -3, -4]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. 0 <= k <= len(arr)
    """
''', '''
    return sorted(arr, reverse=True)[:k]
''', '''
import random
assert top_k_descending([-3, -4, 5], 3) == [5, -3, -4]
assert top_k_descending([4, -4, 4], 2) == [4, 4]
assert top_k_descending([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
assert top_k_descending([1, 2, 3], 0) == []
assert top_k_descending([1, 2, 3], 3) == [3, 2, 1]
assert top_k_descending([3, 2, 1], 2) == [3, 2]
assert top_k_descending([7], 1) == [7]
assert top_k_descending([0, 0, 0], 3) == [0, 0, 0]
assert top_k_descending([-1, -1, -2], 2) == [-1, -1]
assert top_k_descending([1000, -1000, 0], 2) == [1000, 0]
assert top_k_descending([2, 1, 2, 1], 3) == [2, 2, 1]
a = [1, 3, 2]
top_k_descending(a, 2)
assert a == [1, 3, 2]
random.seed(72)
for _ in range(300):
    L = [random.randint(-1000, 1000) for _ in range(random.randint(1, 30))]
    k = random.randint(0, len(L))
    r = top_k_descending(L, k)
    assert len(r) == k and r == sorted(L)[::-1][:k]
big = [random.randint(-1000, 1000) for _ in range(200000)]
assert top_k_descending(big, 3) == sorted(big)[::-1][:3]
''')

add(120, '''def kth_largest(arr, k):
    """
    Given an array arr of integers and a positive integer k, return the k-th largest
    number in arr. Equal numbers are counted separately.

    Example 1:

        Input: arr = [3, 2, 1, 5, 6, 4], k = 2
        Output: 5

    Example 2:

        Input: arr = [5, 5, 3], k = 2
        Output: 5

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. 1 <= k <= len(arr)
    """
''', '''
    return sorted(arr, reverse=True)[k - 1]
''', '''
import random
assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert kth_largest([5, 5, 3], 2) == 5
assert kth_largest([5, 5, 3], 3) == 3
assert kth_largest([1], 1) == 1
assert kth_largest([-1, -2, -3], 1) == -1
assert kth_largest([-1, -2, -3], 3) == -3
assert kth_largest([0, 0, 0], 2) == 0
assert kth_largest([1000, -1000], 2) == -1000
assert kth_largest([1, 2, 3, 4, 5], 5) == 1
assert kth_largest([2, 2, 2, 1], 4) == 1
assert kth_largest([7, 7, 7, 7], 3) == 7
a = [3, 1, 2]
kth_largest(a, 1)
assert a == [3, 1, 2]
random.seed(73)
for _ in range(300):
    L = [random.randint(-50, 50) for _ in range(random.randint(1, 30))]
    k = random.randint(1, len(L))
    assert kth_largest(L, k) == sorted(L, reverse=True)[k - 1]
big = [random.randint(-1000, 1000) for _ in range(200000)]
assert kth_largest(big, 100000) == sorted(big, reverse=True)[99999]
''')

add(120, '''def maximum_distinct(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list
    with the k largest distinct numbers in arr. If arr contains fewer than k distinct
    numbers, return all of them.

    Example 1:

        Input: arr = [4, -4, 4], k = 2
        Output: [-4, 4]

    Example 2:

        Input: arr = [1, 2, 2, 3, 3, 3], k = 2
        Output: [2, 3]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. 0 <= k
    """
''', '''
    if k <= 0:
        return []
    return sorted(set(arr))[-k:]
''', '''
import random
assert maximum_distinct([-3, -4, 5], 3) == [-4, -3, 5]
assert maximum_distinct([4, -4, 4], 2) == [-4, 4]
assert maximum_distinct([1, 2, 2, 3, 3, 3], 2) == [2, 3]
assert maximum_distinct([1, 2, 2, 3, 3, 3], 1) == [3]
assert maximum_distinct([1, 2, 2, 3, 3, 3], 3) == [1, 2, 3]
assert maximum_distinct([1, 2, 2, 3, 3, 3], 10) == [1, 2, 3]
assert maximum_distinct([1, 2, 3], 0) == []
assert maximum_distinct([5], 1) == [5]
assert maximum_distinct([5, 5, 5], 3) == [5]
assert maximum_distinct([0, 0], 1) == [0]
assert maximum_distinct([-1, -1, -2], 2) == [-2, -1]
assert maximum_distinct([1000, -1000, 1000], 2) == [-1000, 1000]
a = [3, 3, 1]
maximum_distinct(a, 1)
assert a == [3, 3, 1]
random.seed(74)
for _ in range(300):
    L = [random.randint(-10, 10) for _ in range(random.randint(1, 30))]
    k = random.randint(0, 25)
    d = sorted(set(L))
    exp = d[len(d) - k:] if 0 < k < len(d) else (d if k > 0 else [])
    assert maximum_distinct(L, k) == exp
assert maximum_distinct(list(range(100000)) * 2, 3) == [99997, 99998, 99999]
''')

add(120, '''def sum_of_k_largest(arr, k):
    """
    Given an array arr of integers and a non-negative integer k, return the sum
    of the k largest numbers in arr. The sum of zero numbers is 0.

    Example 1:

        Input: arr = [-3, -4, 5], k = 2
        Output: 2

    Example 2:

        Input: arr = [4, -4, 4], k = 3
        Output: 4

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 0
        Output: 0

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
''', '''
    return sum(sorted(arr, reverse=True)[:k])
''', '''
import random
assert sum_of_k_largest([-3, -4, 5], 2) == 2
assert sum_of_k_largest([4, -4, 4], 3) == 4
assert sum_of_k_largest([-3, 2, 1, 2, -1, -2, 1], 0) == 0
assert sum_of_k_largest([-3, 2, 1, 2, -1, -2, 1], 1) == 2
assert sum_of_k_largest([-3, 2, 1, 2, -1, -2, 1], 3) == 5
assert sum_of_k_largest([1, 2, 3], 3) == 6
assert sum_of_k_largest([1, 2, 3], 2) == 5
assert sum_of_k_largest([-5, -6], 1) == -5
assert sum_of_k_largest([-5, -6], 2) == -11
assert sum_of_k_largest([0], 1) == 0
assert sum_of_k_largest([1000] * 1000, 1000) == 1000000
assert sum_of_k_largest([-1000] * 5, 5) == -5000
a = [1, 5, 3]
sum_of_k_largest(a, 2)
assert a == [1, 5, 3]
random.seed(75)
for _ in range(300):
    L = [random.randint(-1000, 1000) for _ in range(random.randint(1, 30))]
    k = random.randint(0, len(L))
    assert sum_of_k_largest(L, k) == sum(sorted(L)[::-1][:k])
big = [random.randint(-1000, 1000) for _ in range(200000)]
assert sum_of_k_largest(big, len(big)) == sum(big)
''')

# ---------------------------------------------------------------- HumanEval/124
add(124, '''def valid_date_ymd(date):
    """Return True if date is a valid date string of the format yyyy-mm-dd, otherwise False.
    The year, month and day have exactly 4, 2 and 2 digits. February has 29 days in a leap year
    (divisible by 4, except centuries not divisible by 400), otherwise 28.

    for example:
    valid_date_ymd('2000-03-11') => True

    valid_date_ymd('2021-02-29') => False
    """
''', '''
    import calendar
    import re

    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", date):
        return False
    y, m, d = int(date[:4]), int(date[5:7]), int(date[8:])
    return 1 <= m <= 12 and 1 <= d <= calendar.monthrange(y, m)[1]
''', '''
import datetime
def ref(s):
    try:
        if len(s) != 10 or s[4] != "-" or s[7] != "-":
            return False
        if not all(c in "0123456789" for c in s[:4] + s[5:7] + s[8:]):
            return False
        datetime.date(int(s[:4]), int(s[5:7]), int(s[8:]))
        return True
    except ValueError:
        return False
assert valid_date_ymd("2000-03-11") is True
assert valid_date_ymd("2012-15-01") is False
assert valid_date_ymd("2021-02-29") is False
assert valid_date_ymd("2020-02-29") is True
assert valid_date_ymd("2020/04/06") is False
assert valid_date_ymd("") is False
assert valid_date_ymd("2020-02-30") is False
assert valid_date_ymd("1900-02-29") is False
assert valid_date_ymd("2000-02-29") is True
assert valid_date_ymd("2100-02-29") is False
assert valid_date_ymd("2024-02-29") is True
assert valid_date_ymd("2023-02-28") is True
assert valid_date_ymd("2023-04-31") is False
assert valid_date_ymd("2023-04-30") is True
assert valid_date_ymd("2023-12-31") is True
assert valid_date_ymd("2023-12-32") is False
assert valid_date_ymd("2023-00-10") is False
assert valid_date_ymd("2023-01-00") is False
assert valid_date_ymd("2023-13-01") is False
assert valid_date_ymd("2023-1-01") is False
assert valid_date_ymd("23-01-01") is False
assert valid_date_ymd("20230-1-01") is False
assert valid_date_ymd("2023-01-1") is False
assert valid_date_ymd("2023-01-011") is False
assert valid_date_ymd("2023_01_01") is False
assert valid_date_ymd("abcd-01-01") is False
assert valid_date_ymd("2023-0a-01") is False
assert valid_date_ymd("2023-01-0 ") is False
assert valid_date_ymd(" 2023-01-0") is False
assert valid_date_ymd("2023-+1-01") is False
assert valid_date_ymd("2023-01-\\u0661\\u0662") is False
assert valid_date_ymd("0001-01-01") is True
assert valid_date_ymd("9999-12-31") is True
for y in (1999, 2000, 2001, 2004, 1900, 2100, 2400):
    for m in range(0, 14):
        for d in range(0, 34):
            s = "%04d-%02d-%02d" % (y, m, d)
            assert valid_date_ymd(s) == ref(s), s
''')

add(124, '''def valid_time(time):
    """You have to write a function which validates a given time string and
    returns True if the time is valid otherwise False.
    The time should be in the format hh:mm:ss with exactly two digits for each part, the hours
    should be between 00 and 23, the minutes and the seconds should be between 00 and 59.

    for example:
    valid_time('12:30:45') => True

    valid_time('24:00:00') => False

    valid_time('9:30:00') => False

    valid_time('12-30-45') => False
    """
''', '''
    import re

    if not re.fullmatch(r"[0-9]{2}:[0-9]{2}:[0-9]{2}", time):
        return False
    return int(time[:2]) <= 23 and int(time[3:5]) <= 59 and int(time[6:]) <= 59
''', '''
assert valid_time("12:30:45") is True
assert valid_time("24:00:00") is False
assert valid_time("23:59:59") is True
assert valid_time("9:30:00") is False
assert valid_time("12-30-45") is False
assert valid_time("") is False
assert valid_time("00:00:00") is True
assert valid_time("23:60:00") is False
assert valid_time("23:00:60") is False
assert valid_time("12:30") is False
assert valid_time("12:30:45:") is False
assert valid_time("12:30:455") is False
assert valid_time("1:2:3") is False
assert valid_time("ab:cd:ef") is False
assert valid_time("12:3a:45") is False
assert valid_time(" 2:30:45") is False
assert valid_time("12:30:4 ") is False
assert valid_time("-1:30:45") is False
assert valid_time("+1:30:45") is False
assert valid_time("12:30:45 ") is False
assert valid_time("12:30:\\u0664\\u0665") is False
assert valid_time("19:59:59") is True
assert valid_time("20:00:00") is True
assert valid_time("99:99:99") is False
for h in range(0, 100):
    for m in (0, 1, 59, 60, 99):
        for s in (0, 59, 60, 99):
            t = "%02d:%02d:%02d" % (h, m, s)
            assert valid_time(t) == (h <= 23 and m <= 59 and s <= 59), t
''')

add(124, '''def valid_date_dmy(date):
    """Return True if date is a valid date string dd/mm/yyyy (exactly 2, 2 and 4 digits), otherwise False.
    The month is 1-12 and the day is 1-31 for months 1,3,5,7,8,10,12, 1-30 for months 4,6,9,11
    and 1-29 for month 2.

    for example:
    valid_date_dmy('11/03/2000') => True

    valid_date_dmy('01/15/2012') => False
    """
''', '''
    import re

    if not re.fullmatch(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", date):
        return False
    d, m = int(date[:2]), int(date[3:5])
    limit = 29 if m == 2 else 30 if m in (4, 6, 9, 11) else 31
    return 1 <= m <= 12 and 1 <= d <= limit
''', '''
assert valid_date_dmy("11/03/2000") is True
assert valid_date_dmy("01/15/2012") is False
assert valid_date_dmy("0/04/2040") is False
assert valid_date_dmy("04/06/2020") is True
assert valid_date_dmy("06-04-2020") is False
assert valid_date_dmy("") is False
assert valid_date_dmy("29/02/2021") is True
assert valid_date_dmy("30/02/2020") is False
assert valid_date_dmy("31/04/2020") is False
assert valid_date_dmy("30/04/2020") is True
assert valid_date_dmy("31/12/1999") is True
assert valid_date_dmy("32/01/2000") is False
assert valid_date_dmy("00/01/2000") is False
assert valid_date_dmy("01/00/2000") is False
assert valid_date_dmy("01/13/2000") is False
assert valid_date_dmy("1/01/2000") is False
assert valid_date_dmy("01/1/2000") is False
assert valid_date_dmy("01/01/200") is False
assert valid_date_dmy("01/01/20000") is False
assert valid_date_dmy("aa/01/2000") is False
assert valid_date_dmy("01/01/20a0") is False
assert valid_date_dmy("01.01.2000") is False
assert valid_date_dmy("01/01/2000 ") is False
assert valid_date_dmy(" 1/01/2000") is False
assert valid_date_dmy("-1/01/2000") is False
assert valid_date_dmy("01/01/-200") is False
assert valid_date_dmy("01/01/\\u0662\\u0660\\u0660\\u0660") is False
dm = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for m in range(0, 15):
    for d in range(0, 35):
        s = "%02d/%02d/2001" % (d, m)
        assert valid_date_dmy(s) == (1 <= m <= 12 and 1 <= d <= dm[m - 1]), s
''')

add(124, '''def valid_ipv4(address):
    """You have to write a function which validates a given IPv4 address string and
    returns True if the address is valid otherwise False.
    The address consists of exactly four parts separated by single dots. Every part contains
    only decimal digits, is a number between 0 and 255 inclusive and is written without
    leading zeros (the number 0 itself is written as a single '0').

    for example:
    valid_ipv4('192.168.1.1') => True

    valid_ipv4('256.1.1.1') => False

    valid_ipv4('01.2.3.4') => False

    valid_ipv4('1.2.3') => False
    """
''', '''
    parts = address.split(".")
    return len(parts) == 4 and all(
        p.isascii() and p.isdigit() and (p == "0" or p[0] != "0") and int(p) <= 255 for p in parts
    )
''', '''
assert valid_ipv4("192.168.1.1") is True
assert valid_ipv4("256.1.1.1") is False
assert valid_ipv4("0.0.0.0") is True
assert valid_ipv4("01.2.3.4") is False
assert valid_ipv4("1.2.3") is False
assert valid_ipv4("") is False
assert valid_ipv4("255.255.255.255") is True
assert valid_ipv4("255.255.255.256") is False
assert valid_ipv4("1.2.3.4.5") is False
assert valid_ipv4("1.2.3.") is False
assert valid_ipv4(".1.2.3") is False
assert valid_ipv4("1..2.3") is False
assert valid_ipv4("1.2.3.a") is False
assert valid_ipv4("1.2.3.-4") is False
assert valid_ipv4("1.2.3.+4") is False
assert valid_ipv4("1.2.3. 4") is False
assert valid_ipv4("1.2.3.4 ") is False
assert valid_ipv4("00.0.0.0") is False
assert valid_ipv4("0.00.0.0") is False
assert valid_ipv4("0.0.0.000") is False
assert valid_ipv4("10.20.30.40") is True
assert valid_ipv4("1.1.1.1000") is False
assert valid_ipv4("1,2,3,4") is False
assert valid_ipv4("1.2.3.\\u0664") is False
assert valid_ipv4("1.2.3.0") is True
assert valid_ipv4("99999999999999999999.1.1.1") is False
for a in (0, 1, 9, 10, 99, 100, 199, 200, 249, 250, 255, 256, 300, 999):
    s = "%d.1.2.3" % a
    assert valid_ipv4(s) == (a <= 255), s
    assert valid_ipv4("0%d.1.2.3" % a) is False
''')

add(124, '''def valid_hex_color(code):
    """You have to write a function which validates a given color code string and
    returns True if the code is valid otherwise False.
    The code is valid if all of the following rules are satisfied:
    1. The code starts with the character '#'.
    2. After '#' there are exactly 3 or exactly 6 characters.
    3. All these characters are hexadecimal digits: 0-9, a-f or A-F.

    for example:
    valid_hex_color('#fff') => True

    valid_hex_color('#A1b2C3') => True

    valid_hex_color('#abcd') => False

    valid_hex_color('123456') => False

    valid_hex_color('#ggg') => False
    """
''', '''
    if not code or code[0] != "#":
        return False
    body = code[1:]
    if len(body) not in (3, 6):
        return False
    return all(c in "0123456789abcdefABCDEF" for c in body)
''', '''
assert valid_hex_color("#fff") is True
assert valid_hex_color("#A1b2C3") is True
assert valid_hex_color("#abcd") is False
assert valid_hex_color("123456") is False
assert valid_hex_color("#ggg") is False
assert valid_hex_color("") is False
assert valid_hex_color("#") is False
assert valid_hex_color("#a") is False
assert valid_hex_color("#ab") is False
assert valid_hex_color("#abcde") is False
assert valid_hex_color("#abcdefa") is False
assert valid_hex_color("#000") is True
assert valid_hex_color("#FFFFFF") is True
assert valid_hex_color("#GGGGGG") is False
assert valid_hex_color("##fff") is False
assert valid_hex_color("#ff f") is False
assert valid_hex_color("#fff ") is False
assert valid_hex_color(" #fff") is False
assert valid_hex_color("fff#") is False
assert valid_hex_color("#12345g") is False
assert valid_hex_color("#-12") is False
assert valid_hex_color("#0x1") is False
assert valid_hex_color("#\\u0661\\u0662\\u0663") is False
assert valid_hex_color("#abcdef") is True
assert valid_hex_color("#ABCDEF") is True
import itertools
for n in range(0, 8):
    for t in itertools.product("0aFg#", repeat=min(n, 4)):
        s = "#" + "".join(t) + "0" * max(0, n - 4)
        ok = len(s) - 1 in (3, 6) and all(c in "0123456789abcdefABCDEF" for c in s[1:])
        assert valid_hex_color(s) == ok, s
''')
