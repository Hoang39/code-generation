# parents: HumanEval/26 (remove_duplicates), /29 (filter_by_prefix), /32 (find_zero), /39 (prime_fib), /76 (is_simple_power)
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------------------------------------------------------- HumanEval/26
add(26, '''from typing import List


def keep_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, keep only the elements that occur more than once
    (all of their occurrences). Keep order of elements left the same as in the input.
    >>> keep_duplicates([1, 2, 3, 2, 4])
    [2, 2]
    >>> keep_duplicates([1, 2, 3])
    []
    """
''', '''
    num_cnt = dict()
    for number in numbers:
        num_cnt[number] = num_cnt.get(number, 0) + 1
    return [number for number in numbers if num_cnt[number] > 1]
''', '''
from collections import Counter
assert keep_duplicates([]) == []
assert keep_duplicates([1]) == []
assert keep_duplicates([1, 1]) == [1, 1]
assert keep_duplicates([1, 2, 3, 2, 4]) == [2, 2]
assert keep_duplicates([1, 2, 3]) == []
assert keep_duplicates([3, 1, 3, 1, 3]) == [3, 1, 3, 1, 3]
assert keep_duplicates([5, 4, 5, 6, 4, 7]) == [5, 4, 5, 4]
assert keep_duplicates([0, 0, -1, -1, 2]) == [0, 0, -1, -1]
assert keep_duplicates([7] * 5) == [7] * 5
assert keep_duplicates([-5, 5, -5]) == [-5, -5]
assert keep_duplicates([10 ** 18, 1, 10 ** 18]) == [10 ** 18, 10 ** 18]
x = [2, 2, 3]
keep_duplicates(x)
assert x == [2, 2, 3]
import random
random.seed(11)
for _ in range(300):
    L = [random.randint(-4, 4) for _ in range(random.randint(0, 14))]
    c = Counter(L)
    assert keep_duplicates(L) == [v for v in L if c[v] > 1]
assert keep_duplicates(list(range(100000)) + list(range(50000))) == list(range(50000)) + list(range(50000))
''')

add(26, '''from typing import List


def unique_in_order(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove repeated elements so that every value stays only once,
    at the position of its first occurrence.
    >>> unique_in_order([1, 2, 3, 2, 4])
    [1, 2, 3, 4]
    >>> unique_in_order([])
    []
    """
''', '''
    seen = set()
    res = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            res.append(number)
    return res
''', '''
assert unique_in_order([]) == []
assert unique_in_order([1]) == [1]
assert unique_in_order([1, 1, 1]) == [1]
assert unique_in_order([1, 2, 3, 2, 4]) == [1, 2, 3, 4]
assert unique_in_order([4, 3, 2, 1]) == [4, 3, 2, 1]
assert unique_in_order([2, 1, 2, 1, 2, 1]) == [2, 1]
assert unique_in_order([0, -0, 0]) == [0]
assert unique_in_order([-1, 1, -1, 1]) == [-1, 1]
assert unique_in_order([5, 5, 6, 5, 7, 6]) == [5, 6, 7]
assert unique_in_order([10 ** 15, 10 ** 15, 3]) == [10 ** 15, 3]
x = [1, 1, 2]
unique_in_order(x)
assert x == [1, 1, 2]
import random
random.seed(12)
for _ in range(300):
    L = [random.randint(-5, 5) for _ in range(random.randint(0, 20))]
    exp = []
    for v in L:
        if v not in exp:
            exp.append(v)
    assert unique_in_order(L) == exp
assert unique_in_order(list(range(100000)) * 3) == list(range(100000))
''')

add(26, '''from typing import List


def remove_adjacent_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, collapse every run of equal neighbouring elements into a single element.
    Elements that are equal but not neighbours are kept.
    >>> remove_adjacent_duplicates([1, 1, 2, 2, 2, 1])
    [1, 2, 1]
    >>> remove_adjacent_duplicates([])
    []
    """
''', '''
    res = []
    for number in numbers:
        if not res or res[-1] != number:
            res.append(number)
    return res
''', '''
from itertools import groupby
assert remove_adjacent_duplicates([]) == []
assert remove_adjacent_duplicates([1]) == [1]
assert remove_adjacent_duplicates([1, 1]) == [1]
assert remove_adjacent_duplicates([1, 1, 2, 2, 2, 1]) == [1, 2, 1]
assert remove_adjacent_duplicates([1, 2, 1, 2]) == [1, 2, 1, 2]
assert remove_adjacent_duplicates([0, 0, 0, 0]) == [0]
assert remove_adjacent_duplicates([-1, -1, 1, 1, -1]) == [-1, 1, -1]
assert remove_adjacent_duplicates([3, 3, 4, 4, 3, 3]) == [3, 4, 3]
assert remove_adjacent_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_adjacent_duplicates([5] * 100000) == [5]
x = [1, 1, 2]
remove_adjacent_duplicates(x)
assert x == [1, 1, 2]
import random
random.seed(13)
for _ in range(300):
    L = [random.randint(0, 2) for _ in range(random.randint(0, 20))]
    assert remove_adjacent_duplicates(L) == [k for k, _ in groupby(L)]
assert remove_adjacent_duplicates([1, 2] * 50000) == [1, 2] * 50000
''')

add(26, '''from typing import List, Optional


def first_unique(numbers: List[int]) -> Optional[int]:
    """ From a list of integers, return the first element that occurs exactly once in the list.
    Return None if there is no such element.
    >>> first_unique([1, 2, 3, 2, 1, 4])
    3
    >>> first_unique([1, 1])

    >>> first_unique([])

    """
''', '''
    cnt = dict()
    for number in numbers:
        cnt[number] = cnt.get(number, 0) + 1
    for number in numbers:
        if cnt[number] == 1:
            return number
    return None
''', '''
assert first_unique([]) is None
assert first_unique([1]) == 1
assert first_unique([0]) == 0
assert first_unique([1, 1]) is None
assert first_unique([1, 2, 3, 2, 1, 4]) == 3
assert first_unique([2, 2, 3, 3, 4]) == 4
assert first_unique([5, 5, 5, 6]) == 6
assert first_unique([-1, -1, -2]) == -2
assert first_unique([7, 8, 7, 8]) is None
assert first_unique([0, 0, 1, 0]) == 1
assert first_unique([9, 1, 9, 2, 1]) == 2
assert first_unique([-3, 3, -3]) == 3
import random
random.seed(14)
for _ in range(300):
    L = [random.randint(0, 5) for _ in range(random.randint(0, 12))]
    exp = next((v for v in L if L.count(v) == 1), None)
    assert first_unique(L) == exp
assert first_unique(list(range(100000)) * 2 + [-1]) == -1
assert first_unique(list(range(100000)) + list(range(1, 100000))) == 0
''')

add(26, '''from typing import List


def remove_repeated_words(words: List[str]) -> List[str]:
    """ From a list of words, remove all words that occur more than once, ignoring letter case
    ('Cat' and 'cat' are the same word). Keep order and spelling of the words left the same as in the input.
    >>> remove_repeated_words(['Cat', 'dog', 'cat', 'Bird'])
    ['dog', 'Bird']
    >>> remove_repeated_words([])
    []
    """
''', '''
    cnt = dict()
    for w in words:
        key = w.lower()
        cnt[key] = cnt.get(key, 0) + 1
    return [w for w in words if cnt[w.lower()] == 1]
''', '''
assert remove_repeated_words([]) == []
assert remove_repeated_words(["a"]) == ["a"]
assert remove_repeated_words(["a", "A"]) == []
assert remove_repeated_words(["Cat", "dog", "cat", "Bird"]) == ["dog", "Bird"]
assert remove_repeated_words(["x", "y", "z"]) == ["x", "y", "z"]
assert remove_repeated_words(["Ab", "aB", "AB", "c"]) == ["c"]
assert remove_repeated_words(["", "", "a"]) == ["a"]
assert remove_repeated_words(["Hello", "World", "hello"]) == ["World"]
assert remove_repeated_words(["a b", "A B", "ab"]) == ["ab"]
assert remove_repeated_words(["Z", "z", "Z", "q"]) == ["q"]
assert remove_repeated_words(["Straße", "x"]) == ["Straße", "x"]
w = ["b", "B", "c"]
remove_repeated_words(w)
assert w == ["b", "B", "c"]
import random
random.seed(15)
for _ in range(300):
    L = ["".join(random.choice("aAbB") for _ in range(random.randint(0, 2))) for _ in range(random.randint(0, 12))]
    exp = [v for v in L if sum(1 for u in L if u.lower() == v.lower()) == 1]
    assert remove_repeated_words(L) == exp
assert remove_repeated_words(["a%d" % i for i in range(50000)] + ["A%d" % i for i in range(0, 50000, 2)]) == ["a%d" % i for i in range(1, 50000, 2)]
''')

# ---------------------------------------------------------------- HumanEval/29
add(29, '''from typing import List


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'e')
    ['cde']
    """
''', '''
    return [s for s in strings if s.endswith(suffix)]
''', '''
assert filter_by_suffix([], "a") == []
assert filter_by_suffix(["abc", "bcd", "cde", "array"], "e") == ["cde"]
assert filter_by_suffix(["abc", "bcd", "cde", "array"], "c") == ["abc"]
assert filter_by_suffix(["abc", "bc", "c", ""], "bc") == ["abc", "bc"]
assert filter_by_suffix(["abc", "bc", "c", ""], "") == ["abc", "bc", "c", ""]
assert filter_by_suffix(["a", "aa", "aaa"], "aa") == ["aa", "aaa"]
assert filter_by_suffix(["abc"], "abcd") == []
assert filter_by_suffix(["Abc", "abC"], "c") == ["Abc"]
assert filter_by_suffix(["xyz", "xyz"], "z") == ["xyz", "xyz"]
assert filter_by_suffix(["ab", "ba"], "a") == ["ba"]
assert filter_by_suffix(["a.txt", "b.py", "c.txt"], ".txt") == ["a.txt", "c.txt"]
assert filter_by_suffix(["abca", "abc"], "a") == ["abca"]
assert filter_by_suffix(["" ], "a") == []
assert filter_by_suffix(["é", "ée"], "e") == ["ée"]
big = ["x" * 100 + "ab" for _ in range(50000)] + ["ba"] * 50000
assert filter_by_suffix(big, "ab") == big[:50000]
''')

add(29, '''from typing import List


def filter_longer_than(strings: List[str], length: int) -> List[str]:
    """ Filter an input list of strings only for ones that are strictly longer than a given length.
    >>> filter_longer_than([], 2)
    []
    >>> filter_longer_than(['a', 'abc', 'ab', 'abcd'], 2)
    ['abc', 'abcd']
    """
''', '''
    return [s for s in strings if len(s) > length]
''', '''
assert filter_longer_than([], 2) == []
assert filter_longer_than(["a", "abc", "ab", "abcd"], 2) == ["abc", "abcd"]
assert filter_longer_than(["a", "", "ab"], 0) == ["a", "ab"]
assert filter_longer_than(["a", "", "ab"], 1) == ["ab"]
assert filter_longer_than(["a", "", "ab"], 2) == []
assert filter_longer_than(["a", "", "ab"], -1) == ["a", "", "ab"]
assert filter_longer_than(["abc", "abc"], 3) == []
assert filter_longer_than(["abc", "abc"], 2) == ["abc", "abc"]
assert filter_longer_than(["   ", " "], 1) == ["   "]
assert filter_longer_than(["日本語", "日"], 2) == ["日本語"]
assert filter_longer_than(["abcd", "abc", "ab"], 100) == []
assert filter_longer_than(["a" * 10, "b" * 11], 10) == ["b" * 11]
assert filter_longer_than(["x"] * 3, 0) == ["x", "x", "x"]
import random
random.seed(21)
for _ in range(200):
    L = ["a" * random.randint(0, 6) for _ in range(random.randint(0, 10))]
    k = random.randint(-1, 7)
    assert filter_longer_than(L, k) == [s for s in L if len(s) > k]
big = ["a" * (i % 10) for i in range(100000)]
assert filter_longer_than(big, 8) == ["a" * 9] * 10000
''')

add(29, '''from typing import List


def filter_by_prefix_nocase(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix,
    ignoring letter case. The strings are returned unchanged.
    >>> filter_by_prefix_nocase([], 'a')
    []
    >>> filter_by_prefix_nocase(['Abc', 'bcd', 'cde', 'ARRAY'], 'a')
    ['Abc', 'ARRAY']
    """
''', '''
    p = prefix.lower()
    return [s for s in strings if s.lower().startswith(p)]
''', '''
assert filter_by_prefix_nocase([], "a") == []
assert filter_by_prefix_nocase(["Abc", "bcd", "cde", "ARRAY"], "a") == ["Abc", "ARRAY"]
assert filter_by_prefix_nocase(["Abc", "bcd", "cde", "ARRAY"], "A") == ["Abc", "ARRAY"]
assert filter_by_prefix_nocase(["Abc", "aBc", "abC"], "AB") == ["Abc", "aBc", "abC"]
assert filter_by_prefix_nocase(["Abc", "aBc", "abC"], "abcd") == []
assert filter_by_prefix_nocase(["x", "X", "y"], "") == ["x", "X", "y"]
assert filter_by_prefix_nocase(["xyz"], "XYZ") == ["xyz"]
assert filter_by_prefix_nocase(["xy"], "xyz") == []
assert filter_by_prefix_nocase(["1a", "A1"], "a") == ["A1"]
assert filter_by_prefix_nocase(["Hello", "help", "HELLO!"], "hel") == ["Hello", "help", "HELLO!"]
assert filter_by_prefix_nocase(["Hello", "help", "HELLO!"], "hell") == ["Hello", "HELLO!"]
assert filter_by_prefix_nocase(["ab", "AB"], "b") == []
assert filter_by_prefix_nocase([""], "a") == []
assert filter_by_prefix_nocase([""], "") == [""]
x = ["Ab"]
assert filter_by_prefix_nocase(x, "a") == ["Ab"] and x == ["Ab"]
big = ["Ab" * 50 for _ in range(100000)]
assert len(filter_by_prefix_nocase(big, "aB")) == 100000
''')

add(29, '''from typing import List


def reject_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that do NOT start with a given prefix.
    >>> reject_prefix([], 'a')
    []
    >>> reject_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['bcd', 'cde']
    """
''', '''
    return [s for s in strings if not s.startswith(prefix)]
''', '''
assert reject_prefix([], "a") == []
assert reject_prefix(["abc", "bcd", "cde", "array"], "a") == ["bcd", "cde"]
assert reject_prefix(["abc", "bcd", "cde", "array"], "ab") == ["bcd", "cde", "array"]
assert reject_prefix(["abc", "bcd"], "") == []
assert reject_prefix(["abc", "bcd"], "abcd") == ["abc", "bcd"]
assert reject_prefix(["", "a"], "a") == [""]
assert reject_prefix(["", "a"], "") == []
assert reject_prefix(["Abc", "abc"], "a") == ["Abc"]
assert reject_prefix(["aaa", "aab", "baa"], "aa") == ["baa"]
assert reject_prefix(["a"], "a") == []
assert reject_prefix(["ba", "ca"], "a") == ["ba", "ca"]
assert reject_prefix(["abc"] * 3, "x") == ["abc"] * 3
import random
random.seed(22)
for _ in range(200):
    L = ["".join(random.choice("ab") for _ in range(random.randint(0, 4))) for _ in range(random.randint(0, 10))]
    p = "".join(random.choice("ab") for _ in range(random.randint(0, 3)))
    exp = [s for s in L if s[:len(p)] != p or len(s) < len(p)]
    assert reject_prefix(L, p) == exp
big = ["a" + "b" * 10] * 50000 + ["b" * 11] * 50000
assert reject_prefix(big, "a") == ["b" * 11] * 50000
''')

add(29, '''from typing import List


def filter_by_prefixes(strings: List[str], prefixes: List[str]) -> List[str]:
    """ Filter an input list of strings only for ones that start with at least one of the given prefixes.
    >>> filter_by_prefixes([], ['a'])
    []
    >>> filter_by_prefixes(['abc', 'bcd', 'cde', 'array'], ['b', 'ar'])
    ['bcd', 'array']
    >>> filter_by_prefixes(['abc', 'bcd'], [])
    []
    """
''', '''
    return [s for s in strings if any(s.startswith(p) for p in prefixes)]
''', '''
assert filter_by_prefixes([], ["a"]) == []
assert filter_by_prefixes(["abc", "bcd", "cde", "array"], ["b", "ar"]) == ["bcd", "array"]
assert filter_by_prefixes(["abc", "bcd"], []) == []
assert filter_by_prefixes(["abc", "bcd"], [""]) == ["abc", "bcd"]
assert filter_by_prefixes(["abc", "bcd"], ["a", "ab", "abc"]) == ["abc"]
assert filter_by_prefixes(["abc", "bcd", "abd"], ["ab", "bc"]) == ["abc", "bcd", "abd"]
assert filter_by_prefixes(["abc", "bcd"], ["c"]) == []
assert filter_by_prefixes(["abc", "bcd"], ["abcd"]) == []
assert filter_by_prefixes(["Abc", "abc"], ["a"]) == ["abc"]
assert filter_by_prefixes(["", "a"], ["a"]) == ["a"]
assert filter_by_prefixes([""], [""]) == [""]
assert filter_by_prefixes(["aa", "ab", "ba"], ["a", "a"]) == ["aa", "ab"]
assert filter_by_prefixes(["x1", "x2", "y1"], ["x", "y1"]) == ["x1", "x2", "y1"]
import random
random.seed(23)
for _ in range(200):
    L = ["".join(random.choice("ab") for _ in range(random.randint(0, 4))) for _ in range(random.randint(0, 10))]
    P = ["".join(random.choice("ab") for _ in range(random.randint(1, 3))) for _ in range(random.randint(0, 3))]
    assert filter_by_prefixes(L, P) == [s for s in L if any(s[:len(p)] == p and len(s) >= len(p) for p in P)]
big = ["word%d" % i for i in range(100000)]
assert len(filter_by_prefixes(big, ["word9", "word1"])) == len([s for s in big if s.startswith("word9") or s.startswith("word1")])
''')

# ---------------------------------------------------------------- HumanEval/32
add(32, '''def find_root_bisection(xs: list, lo: float, hi: float):
    """ xs are coefficients of a polynomial: xs[0] + xs[1] * x + .... xs[n] * x^n
    The polynomial changes sign on [lo, hi]. Return a point x from [lo, hi] where it is (almost) 0.
    >>> round(find_root_bisection([-2, 0, 1], 0, 2), 3) # f(x) = x^2 - 2
    1.414
    """
''', '''
    def f(x):
        return sum(c * x ** i for i, c in enumerate(xs))

    if f(lo) == 0:
        return lo
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) == 0:
            return mid
        if (f(mid) < 0) == (f(lo) < 0):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
''', '''
import random
def pv(xs, x):
    return sum(c * x ** i for i, c in enumerate(xs))
assert abs(find_root_bisection([-2, 0, 1], 0, 2) - 2 ** 0.5) < 1e-9
assert abs(find_root_bisection([-2, 0, 1], -2, 0) + 2 ** 0.5) < 1e-9
assert abs(find_root_bisection([-1, 1], -5, 5) - 1.0) < 1e-9
assert abs(find_root_bisection([1, 2], -10, 10) + 0.5) < 1e-9
assert abs(find_root_bisection([-6, 11, -6, 1], 0, 1.5) - 1.0) < 1e-9
assert abs(find_root_bisection([-6, 11, -6, 1], 1.5, 2.5) - 2.0) < 1e-9
assert abs(find_root_bisection([-6, 11, -6, 1], 2.5, 10) - 3.0) < 1e-9
assert find_root_bisection([0, 1], 0, 5) == 0
assert find_root_bisection([-3, 1], 3, 10) == 3
assert abs(find_root_bisection([-27, 0, 0, 1], 0, 100) - 3.0) < 1e-9
assert abs(find_root_bisection([8, 0, 0, 1], -100, 100) + 2.0) < 1e-9
assert abs(find_root_bisection([-1e-6, 1], -1, 1) - 1e-6) < 1e-12
assert abs(find_root_bisection([-1e6, 1], 0, 1e9) - 1e6) < 1e-3
random.seed(31)
for _ in range(200):
    r = random.uniform(-9, 9)
    k = random.uniform(0.5, 4)
    xs = [-k * r, k]
    lo, hi = r - random.uniform(0.1, 20), r + random.uniform(0.1, 20)
    assert abs(find_root_bisection(xs, lo, hi) - r) < 1e-8
    cub = [-r * r * r, 0, 0, 1] if r > 0 else [r * r * r * -1, 0, 0, 1]
    root = find_root_bisection(cub, -100, 100)
    assert abs(pv(cub, root)) < 1e-6
''')

add(32, '''def horner(xs: list, x: int) -> int:
    """ Evaluate polynomial with integer coefficients xs at integer point x using exact integer arithmetic.
    xs[0] is the constant term, so the value is xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    The value of an empty polynomial is 0.
    >>> horner([1, 2, 3], 2) # 1 + 2 * 2 + 3 * 4
    17
    >>> horner([], 5)
    0
    >>> horner([7], 100)
    7
    """
''', '''
    result = 0
    for coeff in reversed(xs):
        result = result * x + coeff
    return result
''', '''
import random
assert horner([], 5) == 0
assert horner([7], 100) == 7
assert horner([0], 3) == 0
assert horner([1, 2, 3], 2) == 17
assert horner([1, 2, 3], 0) == 1
assert horner([1, 2, 3], -1) == 2
assert horner([-6, 11, -6, 1], 1) == 0
assert horner([-6, 11, -6, 1], 2) == 0
assert horner([-6, 11, -6, 1], 3) == 0
assert horner([-6, 11, -6, 1], 4) == 6
assert horner([0, 0, 0, 1], 10) == 1000
assert horner([1, 1, 1, 1, 1], 10) == 11111
assert horner([5, 0, 0, 0], 99) == 5
assert horner([1, -1], 1) == 0
assert horner([3, 4], -7) == -25
assert horner([1] * 61, 2) == 2 ** 61 - 1
assert horner([0] * 100 + [1], 3) == 3 ** 100
assert horner([1, 0, 0, 1], 10 ** 6) == 10 ** 18 + 1
random.seed(32)
for _ in range(300):
    xs = [random.randint(-9, 9) for _ in range(random.randint(0, 8))]
    x = random.randint(-12, 12)
    assert horner(xs, x) == sum(c * x ** i for i, c in enumerate(xs))
big = [random.randint(-1000, 1000) for _ in range(2000)]
assert horner(big, 3) == sum(c * 3 ** i for i, c in enumerate(big))
''')

add(32, '''def poly_multiply(xs: list, ys: list) -> list:
    """ xs and ys are coefficients of two polynomials, the first element is the constant term.
    poly_multiply returns coefficients of the product of these polynomials in the same form.
    The product with an empty polynomial is an empty list.
    >>> poly_multiply([1, 1], [1, 1]) # (1 + x) * (1 + x)
    [1, 2, 1]
    >>> poly_multiply([-1, 1], [1, 1]) # (x - 1) * (x + 1)
    [-1, 0, 1]
    >>> poly_multiply([], [1, 2])
    []
    """
''', '''
    if not xs or not ys:
        return []
    res = [0] * (len(xs) + len(ys) - 1)
    for i, a in enumerate(xs):
        for j, b in enumerate(ys):
            res[i + j] += a * b
    return res
''', '''
import random
def pv(xs, x):
    return sum(c * x ** i for i, c in enumerate(xs))
assert poly_multiply([], [1, 2]) == []
assert poly_multiply([1, 2], []) == []
assert poly_multiply([], []) == []
assert poly_multiply([1, 1], [1, 1]) == [1, 2, 1]
assert poly_multiply([-1, 1], [1, 1]) == [-1, 0, 1]
assert poly_multiply([2], [3]) == [6]
assert poly_multiply([0], [1, 2, 3]) == [0, 0, 0]
assert poly_multiply([1], [4, 5, 6]) == [4, 5, 6]
assert poly_multiply([0, 1], [0, 1]) == [0, 0, 1]
assert poly_multiply([1, 2, 3], [4, 5]) == [4, 13, 22, 15]
assert poly_multiply([-1, 1], [-2, 1]) == [2, -3, 1]
assert poly_multiply([1, -1], [1, 1, 1, 1]) == [1, 0, 0, 0, -1]
assert poly_multiply([10 ** 9, 1], [10 ** 9, 1]) == [10 ** 18, 2 * 10 ** 9, 1]
a, b = [1, 2], [3, 4]
poly_multiply(a, b)
assert a == [1, 2] and b == [3, 4]
random.seed(33)
for _ in range(200):
    p = [random.randint(-5, 5) for _ in range(random.randint(1, 6))]
    q = [random.randint(-5, 5) for _ in range(random.randint(1, 6))]
    r = poly_multiply(p, q)
    assert len(r) == len(p) + len(q) - 1
    for x in (-2, -1, 0, 1, 3):
        assert pv(r, x) == pv(p, x) * pv(q, x)
assert poly_multiply([1] * 300, [1] * 300) == [min(i, 598 - i) + 1 for i in range(599)]
''')

add(32, '''def poly_slope(xs: list, x: float):
    """ xs are coefficients of a polynomial: xs[0] + xs[1] * x + .... xs[n] * x^n
    poly_slope returns the value of the derivative of this polynomial at point x, as a float.
    >>> poly_slope([3, 1, 2, 4], 1) # f(x) = 3 + x + 2x^2 + 4x^3, f'(x) = 1 + 4x + 12x^2
    17.0
    >>> poly_slope([5], 10)
    0.0
    """
''', '''
    return float(sum(i * coeff * x ** (i - 1) for i, coeff in enumerate(xs) if i > 0))
''', '''
import random
def pv(xs, x):
    return sum(c * x ** i for i, c in enumerate(xs))
def pv(xs, x):
    return sum(c * x ** i for i, c in enumerate(xs))
def pv(xs, x):
    return sum(c * x ** i for i, c in enumerate(xs))
def pv(xs, x):
    return sum(c * x ** i for i, c in enumerate(xs))
def pv(xs, x):
    return sum(c * x ** i for i, c in enumerate(xs))
def pv(xs, x):
    return sum(c * x ** i for i, c in enumerate(xs))
assert poly_slope([], 3) == 0.0
assert poly_slope([5], 10) == 0.0
assert poly_slope([3, 1, 2, 4], 1) == 17.0
assert poly_slope([3, 1, 2, 4], 0) == 1.0
assert poly_slope([0, 1], 123) == 1.0
assert poly_slope([0, 0, 1], 3) == 6.0
assert poly_slope([0, 0, 1], -3) == -6.0
assert poly_slope([1, 2, 3], 0) == 2.0
assert poly_slope([1, 0, 0, 1], 2) == 12.0
assert poly_slope([-6, 11, -6, 1], 1) == 2.0
assert poly_slope([-6, 11, -6, 1], 2) == -1.0
assert poly_slope([-6, 11, -6, 1], 3) == 2.0
assert poly_slope([0, 0, 0, 0, 1], 2) == 32.0
assert abs(poly_slope([0, 0, 1], 0.5) - 1.0) < 1e-12
assert isinstance(poly_slope([1, 2], 3), float)
assert isinstance(poly_slope([], 3), float)
random.seed(34)
for _ in range(200):
    xs = [random.randint(-5, 5) for _ in range(random.randint(0, 7))]
    x = random.randint(-4, 4)
    exp = sum(i * c * x ** (i - 1) for i, c in enumerate(xs) if i >= 1)
    assert abs(poly_slope(xs, x) - exp) < 1e-9
    h = 1e-5
    num = (pv(xs, x + h) - pv(xs, x - h)) / (2 * h)
    assert abs(poly_slope(xs, x) - num) < 1e-2 * (1 + abs(exp))
''')

add(32, '''def find_zero_odd_degree(xs: list):
    """ xs are coefficients of a polynomial: xs[0] + xs[1] * x + .... xs[n] * x^n
    Return one x such that the polynomial is 0 at x. xs has an even number of
    coefficients and a non zero last coefficient, so a solution is guaranteed.
    >>> round(find_zero_odd_degree([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero_odd_degree([-8, 0, 0, 1]), 2) # f(x) = x^3 - 8
    2.0
    """
''', '''
    def f(x):
        return sum(c * x ** i for i, c in enumerate(xs))

    lo, hi = -1.0, 1.0
    while f(lo) * f(hi) > 0:
        lo *= 2.0
        hi *= 2.0
    for _ in range(300):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2
''', '''
import random, math
def pv(xs, x):
    return sum(c * x ** i for i, c in enumerate(xs))
assert round(find_zero_odd_degree([1, 2]), 2) == -0.5
assert round(find_zero_odd_degree([-8, 0, 0, 1]), 2) == 2.0
assert round(find_zero_odd_degree([-6, 11, -6, 1]), 2) in (1.0, 2.0, 3.0)
assert abs(find_zero_odd_degree([0, 1])) < 1e-9
assert abs(find_zero_odd_degree([0, 0, 0, 1])) < 1e-3
assert abs(find_zero_odd_degree([-1, 1]) - 1.0) < 1e-9
assert abs(find_zero_odd_degree([1, 1]) + 1.0) < 1e-9
assert abs(find_zero_odd_degree([5, -1]) - 5.0) < 1e-9
assert abs(find_zero_odd_degree([-1000000, 1]) - 1000000.0) < 1e-6
assert abs(find_zero_odd_degree([1, 0, 0, 0, 0, 1]) + 1.0) < 1e-9
assert abs(find_zero_odd_degree([0.001, 1]) + 0.001) < 1e-12
assert abs(find_zero_odd_degree([3, 0, 0, -1]) - 3 ** (1 / 3)) < 1e-9
assert abs(pv([2, -3, 0, 1], find_zero_odd_degree([2, -3, 0, 1]))) < 1e-6
random.seed(35)
for _ in range(300):
    n = random.choice([2, 4, 6])
    xs = [random.randint(-10, 10) for _ in range(n)]
    while xs[-1] == 0:
        xs[-1] = random.randint(-10, 10)
    r = find_zero_odd_degree(xs)
    assert math.isfinite(r)
    assert abs(math.fsum(c * math.pow(r, i) for i, c in enumerate(xs))) < 1e-4, xs
''')

# ---------------------------------------------------------------- HumanEval/39
add(39, '''def prime_fib_count(limit: int):
    """
    prime_fib_count returns how many different Fibonacci numbers that are not greater than limit are also prime.
    >>> prime_fib_count(1)
    0
    >>> prime_fib_count(2)
    1
    >>> prime_fib_count(13)
    4
    >>> prime_fib_count(100)
    5
    """
''', '''
    def is_prime(m):
        small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
        if m < 2 or any(m % p == 0 for p in small):
            return m in small
        d, r = m - 1, 0
        while d % 2 == 0:
            d //= 2
            r += 1
        for a in small:
            x = pow(a, d, m)
            if x in (1, m - 1):
                continue
            for _ in range(r - 1):
                x = x * x % m
                if x == m - 1:
                    break
            else:
                return False
        return True

    count = 0
    a, b = 1, 2
    while a <= limit:
        if is_prime(a):
            count += 1
        a, b = b, a + b
    return count
''', '''
KNOWN = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073, 99194853094755497]
assert prime_fib_count(-5) == 0
assert prime_fib_count(0) == 0
assert prime_fib_count(1) == 0
assert prime_fib_count(2) == 1
assert prime_fib_count(3) == 2
assert prime_fib_count(4) == 2
assert prime_fib_count(5) == 3
assert prime_fib_count(12) == 3
assert prime_fib_count(13) == 4
assert prime_fib_count(88) == 4
assert prime_fib_count(89) == 5
assert prime_fib_count(100) == 5
assert prime_fib_count(10 ** 6) == 9
assert prime_fib_count(433494436) == 9
assert prime_fib_count(433494437) == 10
assert prime_fib_count(10 ** 12) == 11
assert prime_fib_count(99194853094755496) == 11
assert prime_fib_count(99194853094755497) == 12
for lim in range(0, 3000):
    assert prime_fib_count(lim) == sum(1 for v in KNOWN if v <= lim), lim
''')

add(39, '''def prime_lucas(n: int):
    """
    prime_lucas returns n-th number that is a Lucas number and it's also prime.
    Lucas numbers start with 2, 1, 3, 4, 7, 11, 18, 29, ... and every next one is the sum of the previous two.
    >>> prime_lucas(1)
    2
    >>> prime_lucas(2)
    3
    >>> prime_lucas(3)
    7
    >>> prime_lucas(4)
    11
    >>> prime_lucas(5)
    29
    """
''', '''
    def is_prime(m):
        if m < 2:
            return False
        d = 2
        while d * d <= m:
            if m % d == 0:
                return False
            d += 1
        return True

    found = 0
    a, b = 2, 1
    while True:
        if is_prime(a):
            found += 1
            if found == n:
                return a
        a, b = b, a + b
''', '''
EXP = [2, 3, 7, 11, 29, 47, 199, 521, 2207, 3571, 9349, 3010349, 54018521, 370248451, 6643838879]
for i, v in enumerate(EXP, 1):
    assert prime_lucas(i) == v, i
def slow_prime(m):
    if m < 2:
        return False
    d = 2
    while d * d <= m:
        if m % d == 0:
            return False
        d += 1
    return True
seq, a, b = [], 2, 1
while a < 10 ** 8:
    if slow_prime(a):
        seq.append(a)
    a, b = b, a + b
assert seq == EXP[:len(seq)]
assert prime_lucas(1) == 2
assert prime_lucas(9) == 2207
assert prime_lucas(10) == 3571
assert prime_lucas(12) == 3010349
assert prime_lucas(15) == 6643838879
assert prime_lucas(2) == 3
assert prime_lucas(3) == 7
assert prime_lucas(6) == 47
assert prime_lucas(7) == 199
assert prime_lucas(8) == 521
assert prime_lucas(11) == 9349
assert prime_lucas(13) == 54018521
assert prime_lucas(14) == 370248451
''')

add(39, '''def is_fibonacci_prime(n: int) -> bool:
    """
    is_fibonacci_prime returns True if n is a Fibonacci number and it's also prime, otherwise False.
    >>> is_fibonacci_prime(2)
    True
    >>> is_fibonacci_prime(13)
    True
    >>> is_fibonacci_prime(21)
    False
    >>> is_fibonacci_prime(7)
    False
    """
''', '''
    if n < 2:
        return False
    a, b = 1, 2
    while a < n:
        a, b = b, a + b
    if a != n:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
''', '''
KNOWN = {2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073}
assert is_fibonacci_prime(2) is True
assert is_fibonacci_prime(3) is True
assert is_fibonacci_prime(5) is True
assert is_fibonacci_prime(13) is True
assert is_fibonacci_prime(21) is False
assert is_fibonacci_prime(7) is False
assert is_fibonacci_prime(1) is False
assert is_fibonacci_prime(0) is False
assert is_fibonacci_prime(-3) is False
assert is_fibonacci_prime(8) is False
assert is_fibonacci_prime(89) is True
assert is_fibonacci_prime(144) is False
assert is_fibonacci_prime(233) is True
assert is_fibonacci_prime(377) is False
assert is_fibonacci_prime(514229) is True
assert is_fibonacci_prime(514228) is False
assert is_fibonacci_prime(433494437) is True
assert is_fibonacci_prime(433494439) is False
assert is_fibonacci_prime(2971215073) is True
assert is_fibonacci_prime(2971215071) is False
for n in range(-5, 5000):
    assert is_fibonacci_prime(n) == (n in KNOWN), n
''')

add(39, '''def sum_prime_fib(n: int):
    """
    sum_prime_fib returns the sum of the first n numbers that are Fibonacci numbers and also prime.
    The sum of zero numbers is 0.
    >>> sum_prime_fib(0)
    0
    >>> sum_prime_fib(1)
    2
    >>> sum_prime_fib(3)
    10
    >>> sum_prime_fib(5)
    112
    """
''', '''
    def is_prime(m):
        small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
        if m < 2 or any(m % p == 0 for p in small):
            return m in small
        d, r = m - 1, 0
        while d % 2 == 0:
            d //= 2
            r += 1
        for a in small:
            x = pow(a, d, m)
            if x in (1, m - 1):
                continue
            for _ in range(r - 1):
                x = x * x % m
                if x == m - 1:
                    break
            else:
                return False
        return True

    total, found = 0, 0
    a, b = 1, 2
    while found < n:
        if is_prime(a):
            total += a
            found += 1
        a, b = b, a + b
    return total
''', '''
KNOWN = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073, 99194853094755497]
assert sum_prime_fib(0) == 0
for n in range(0, 13):
    assert sum_prime_fib(n) == sum(KNOWN[:n]), n
assert sum_prime_fib(1) == 2
assert sum_prime_fib(2) == 5
assert sum_prime_fib(3) == 10
assert sum_prime_fib(4) == 23
assert sum_prime_fib(5) == 112
assert sum_prime_fib(6) == 345
assert sum_prime_fib(9) == 544828
assert sum_prime_fib(10) == 544828 + 433494437
assert sum_prime_fib(12) == 99194853094755497 + 2971215073 + 433494437 + 544828
assert sum_prime_fib(11) == 2971215073 + 433494437 + 544828
assert sum_prime_fib(7) == 1942
assert sum_prime_fib(8) == 30599
''')

add(39, '''def largest_prime_fib_at_most(limit: int):
    """
    largest_prime_fib_at_most returns the largest number that is a Fibonacci number, it's also prime
    and not greater than limit (0 <= limit <= 10**12). If there is no such number, it returns None.
    >>> largest_prime_fib_at_most(1)

    >>> largest_prime_fib_at_most(12)
    5
    >>> largest_prime_fib_at_most(100)
    89
    """
''', '''
    def is_prime(m):
        if m < 2:
            return False
        d = 2
        while d * d <= m:
            if m % d == 0:
                return False
            d += 1
        return True

    best = None
    a, b = 1, 2
    while a <= limit:
        if is_prime(a):
            best = a
        a, b = b, a + b
    return best
''', '''
KNOWN = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073]
assert largest_prime_fib_at_most(0) is None
assert largest_prime_fib_at_most(1) is None
assert largest_prime_fib_at_most(2) == 2
assert largest_prime_fib_at_most(3) == 3
assert largest_prime_fib_at_most(4) == 3
assert largest_prime_fib_at_most(12) == 5
assert largest_prime_fib_at_most(13) == 13
assert largest_prime_fib_at_most(88) == 13
assert largest_prime_fib_at_most(89) == 89
assert largest_prime_fib_at_most(100) == 89
assert largest_prime_fib_at_most(10 ** 6) == 514229
assert largest_prime_fib_at_most(10 ** 9) == 433494437
assert largest_prime_fib_at_most(10 ** 12) == 2971215073
assert largest_prime_fib_at_most(2971215072) == 433494437
assert largest_prime_fib_at_most(2971215073) == 2971215073
assert largest_prime_fib_at_most(10 ** 11) == 2971215073
assert largest_prime_fib_at_most(2) == 2
for lim in range(0, 3000):
    c = [v for v in KNOWN if v <= lim]
    assert largest_prime_fib_at_most(lim) == (c[-1] if c else None), lim
''')

# ---------------------------------------------------------------- HumanEval/76
add(76, '''def is_perfect_cube(x):
    """Your task is to write a function that returns true if an integer x is a perfect cube
    (the cube of some integer, which may be negative or zero) and false in other cases.
    For example:
    is_perfect_cube(1) => true
    is_perfect_cube(27) => true
    is_perfect_cube(-8) => true
    is_perfect_cube(0) => true
    is_perfect_cube(2) => false
    is_perfect_cube(-9) => false
    """
''', '''
    a = abs(x)
    r = round(a ** (1.0 / 3))
    for c in (r - 1, r, r + 1):
        if c >= 0 and c ** 3 == a:
            return True
    return False
''', '''
CUBES = {i ** 3 for i in range(-120, 121)}
assert is_perfect_cube(0) is True
assert is_perfect_cube(1) is True
assert is_perfect_cube(-1) is True
assert is_perfect_cube(8) is True
assert is_perfect_cube(-8) is True
assert is_perfect_cube(27) is True
assert is_perfect_cube(2) is False
assert is_perfect_cube(-9) is False
assert is_perfect_cube(26) is False
assert is_perfect_cube(28) is False
assert is_perfect_cube(63) is False
assert is_perfect_cube(64) is True
assert is_perfect_cube(10 ** 18) is True
assert is_perfect_cube(10 ** 18 - 1) is False
assert is_perfect_cube(10 ** 18 + 1) is False
assert is_perfect_cube(-10 ** 18) is True
assert is_perfect_cube(999999 ** 3) is True
assert is_perfect_cube(999999 ** 3 + 1) is False
assert is_perfect_cube(999999 ** 3 - 1) is False
assert is_perfect_cube((10 ** 6 + 1) ** 3) is True
assert is_perfect_cube((10 ** 6 + 1) ** 3 - 1) is False
for x in range(-2000, 2000):
    assert is_perfect_cube(x) == (x in CUBES), x
for k in range(1, 3000):
    assert is_perfect_cube(k ** 3) and is_perfect_cube(-k ** 3)
    assert not is_perfect_cube(k ** 3 + 1) or k == 0
    assert not is_perfect_cube(k ** 3 - 1) or k == 1
''')

add(76, '''def power_exponent(x, n):
    """Your task is to write a function that returns the exponent k (a non-negative integer)
    such that n**k = x, or -1 if there is no such k. Both x and n are positive integers.
    If n is 1, then only x = 1 is a power of n (with k = 0).
    For example:
    power_exponent(1, 4) => 0
    power_exponent(8, 2) => 3
    power_exponent(81, 3) => 4
    power_exponent(3, 2) => -1
    power_exponent(3, 1) => -1
    power_exponent(1, 1) => 0
    """
''', '''
    if x == 1:
        return 0
    if n == 1:
        return -1
    k, p = 0, 1
    while p < x:
        p *= n
        k += 1
    return k if p == x else -1
''', '''
assert power_exponent(1, 4) == 0
assert power_exponent(1, 1) == 0
assert power_exponent(1, 2) == 0
assert power_exponent(2, 2) == 1
assert power_exponent(8, 2) == 3
assert power_exponent(81, 3) == 4
assert power_exponent(3, 2) == -1
assert power_exponent(3, 1) == -1
assert power_exponent(2, 1) == -1
assert power_exponent(5, 3) == -1
assert power_exponent(7, 7) == 1
assert power_exponent(6, 7) == -1
assert power_exponent(8, 9) == -1
assert power_exponent(9, 8) == -1
assert power_exponent(16, 4) == 2
assert power_exponent(16, 2) == 4
assert power_exponent(16, 16) == 1
assert power_exponent(2 ** 100, 2) == 100
assert power_exponent(2 ** 100 + 1, 2) == -1
assert power_exponent(2 ** 100 - 1, 2) == -1
assert power_exponent(10 ** 18, 10) == 18
assert power_exponent(10 ** 18, 1000) == 6
assert power_exponent(10 ** 18, 7) == -1
assert power_exponent(10 ** 100, 10) == 100
assert power_exponent(10 ** 30, 10 ** 30) == 1
for n in range(1, 12):
    for x in range(1, 400):
        exp, p, k = -1, 1, 0
        while p <= x and n > 1:
            if p == x:
                exp = k
                break
            p *= n
            k += 1
        if x == 1:
            exp = 0
        assert power_exponent(x, n) == exp, (x, n)
''')

add(76, '''def nearest_power_above(x, n):
    """Your task is to write a function that returns the smallest power of n that is greater than
    or equal to x. Here x is a positive integer and n is an integer greater than 1.
    A power of n is a number n**k for a non-negative integer k.
    For example:
    nearest_power_above(1, 2) => 1
    nearest_power_above(5, 2) => 8
    nearest_power_above(8, 2) => 8
    nearest_power_above(10, 3) => 27
    nearest_power_above(100, 10) => 100
    """
''', '''
    p = 1
    while p < x:
        p *= n
    return p
''', '''
assert nearest_power_above(1, 2) == 1
assert nearest_power_above(2, 2) == 2
assert nearest_power_above(3, 2) == 4
assert nearest_power_above(5, 2) == 8
assert nearest_power_above(8, 2) == 8
assert nearest_power_above(9, 2) == 16
assert nearest_power_above(10, 3) == 27
assert nearest_power_above(9, 3) == 9
assert nearest_power_above(100, 10) == 100
assert nearest_power_above(101, 10) == 1000
assert nearest_power_above(1, 10) == 1
assert nearest_power_above(7, 100) == 100
assert nearest_power_above(2 ** 64, 2) == 2 ** 64
assert nearest_power_above(2 ** 64 + 1, 2) == 2 ** 65
assert nearest_power_above(10 ** 50, 10) == 10 ** 50
assert nearest_power_above(10 ** 50 - 1, 10) == 10 ** 50
assert nearest_power_above(3 ** 40 + 1, 3) == 3 ** 41
for n in range(2, 9):
    for x in range(1, 500):
        exp = 1
        while exp < x:
            exp *= n
        assert nearest_power_above(x, n) == exp, (x, n)
        r = nearest_power_above(x, n)
        assert r >= x and (r == 1 or r // n < x)
''')

add(76, '''def count_powers_in_range(n, lo, hi):
    """Your task is to write a function that counts how many powers of n lie in the closed range [lo, hi].
    A power of n is a number n**k for a non-negative integer k (so 1 is always a power of n).
    Here n is an integer greater than 1 and 1 <= lo <= hi.
    For example:
    count_powers_in_range(2, 1, 10) => 4
    count_powers_in_range(2, 3, 7) => 1
    count_powers_in_range(10, 11, 99) => 0
    count_powers_in_range(3, 1, 1) => 1
    """
''', '''
    count = 0
    p = 1
    while p <= hi:
        if p >= lo:
            count += 1
        p *= n
    return count
''', '''
assert count_powers_in_range(2, 1, 10) == 4
assert count_powers_in_range(2, 3, 7) == 1
assert count_powers_in_range(10, 11, 99) == 0
assert count_powers_in_range(3, 1, 1) == 1
assert count_powers_in_range(2, 1, 1) == 1
assert count_powers_in_range(2, 2, 2) == 1
assert count_powers_in_range(2, 3, 3) == 0
assert count_powers_in_range(2, 1, 2 ** 20) == 21
assert count_powers_in_range(2, 2 ** 20, 2 ** 20) == 1
assert count_powers_in_range(2, 2 ** 20 + 1, 2 ** 30) == 10
assert count_powers_in_range(10, 1, 10 ** 18) == 19
assert count_powers_in_range(10, 10 ** 17, 10 ** 18) == 2
assert count_powers_in_range(7, 8, 48) == 0
assert count_powers_in_range(7, 7, 49) == 2
assert count_powers_in_range(5, 1, 10 ** 100) == 144
assert count_powers_in_range(1000, 1, 10 ** 30) == 11
for n in range(2, 7):
    for lo in range(1, 60):
        for hi in range(lo, 60):
            exp = sum(1 for k in range(0, 10) if lo <= n ** k <= hi)
            assert count_powers_in_range(n, lo, hi) == exp, (n, lo, hi)
''')

add(76, '''def is_signed_power(x, n):
    """Your task is to write a function that returns true if an integer x is a power of an integer n
    and false in other cases. Here n may be negative or zero.
    x is a power of n if n**k = x for some non-negative integer k (n**0 = 1 for any n, including 0).
    For example:
    is_signed_power(1, 5) => true
    is_signed_power(-8, -2) => true
    is_signed_power(8, -2) => false
    is_signed_power(16, -2) => true
    is_signed_power(0, 0) => true
    is_signed_power(5, 0) => false
    is_signed_power(-1, 1) => false
    """
''', '''
    if x == 1:
        return True
    if n in (0, 1):
        return x == n
    if n == -1:
        return x == -1
    p = n
    while abs(p) <= abs(x):
        if p == x:
            return True
        p *= n
    return False
''', '''
def ref(x, n):
    for k in range(0, 40):
        if n ** k == x:
            return True
    return False
assert is_signed_power(1, 5) is True
assert is_signed_power(-8, -2) is True
assert is_signed_power(8, -2) is False
assert is_signed_power(16, -2) is True
assert is_signed_power(0, 0) is True
assert is_signed_power(5, 0) is False
assert is_signed_power(-1, 1) is False
assert is_signed_power(1, 1) is True
assert is_signed_power(1, 0) is True
assert is_signed_power(1, -1) is True
assert is_signed_power(-1, -1) is True
assert is_signed_power(2, -1) is False
assert is_signed_power(0, 5) is False
assert is_signed_power(0, -5) is False
assert is_signed_power(0, 1) is False
assert is_signed_power(-27, -3) is True
assert is_signed_power(81, -3) is True
assert is_signed_power(-81, -3) is False
assert is_signed_power(2 ** 60, 2) is True
assert is_signed_power(-2 ** 61, -2) is True
assert is_signed_power(2 ** 60 + 1, 2) is False
assert is_signed_power(10 ** 30, -10) is True
assert is_signed_power(-10 ** 31, -10) is True
for n in range(-6, 7):
    for x in range(-300, 300):
        assert is_signed_power(x, n) == ref(x, n), (x, n)
''')
