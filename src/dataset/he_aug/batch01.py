# parents 1-5
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------- parent 1: make_palindrome ----------------
add(1, '''def make_palindrome_front(string: str) -> str:
    """ Find the shortest palindrome that ends with a supplied string, by adding characters to the front.
    >>> make_palindrome_front('')
    ''
    >>> make_palindrome_front('cat')
    'tacat'
    >>> make_palindrome_front('abb')
    'bbabb'
    """
''', '''
    for i in range(len(string), -1, -1):
        prefix = string[:i]
        if prefix == prefix[::-1]:
            return string[i:][::-1] + string
    return string
''', '''
assert make_palindrome_front("") == ""
assert make_palindrome_front("a") == "a"
assert make_palindrome_front("aa") == "aa"
assert make_palindrome_front("ab") == "bab"
assert make_palindrome_front("racecar") == "racecar"
assert make_palindrome_front("aacecaaa") == "aaacecaaa"
assert make_palindrome_front("abcd") == "dcbabcd"
import random
random.seed(1)
for _ in range(300):
    s = "".join(random.choice("ab") for _ in range(random.randint(0, 9)))
    r = make_palindrome_front(s)
    assert r == r[::-1] and r.endswith(s)
    best = None
    for k in range(len(s) + 1):
        c = s[len(s) - k:][::-1] + s
        if c == c[::-1]:
            best = c
            break
    assert r == best, (s, r, best)
s = "ab" * 2000 + "c"
r = make_palindrome_front(s)
assert r == r[::-1] and r.endswith(s) and len(r) == len(s) + 2 and r.startswith("cb")
''')

add(1, '''def longest_palindromic_suffix(string: str) -> str:
    """ Return the longest suffix of the given string that is a palindrome.
    For an empty string return an empty string.
    >>> longest_palindromic_suffix('')
    ''
    >>> longest_palindromic_suffix('cat')
    't'
    >>> longest_palindromic_suffix('abaxyzzyxf')
    'f'
    >>> longest_palindromic_suffix('xabba')
    'abba'
    """
''', '''
    for i in range(len(string)):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            return suffix
    return ""
''', '''
assert longest_palindromic_suffix("") == ""
assert longest_palindromic_suffix("a") == "a"
assert longest_palindromic_suffix("aaa") == "aaa"
assert longest_palindromic_suffix("ab") == "b"
assert longest_palindromic_suffix("racecar") == "racecar"
assert longest_palindromic_suffix("abacabad") == "d"
assert longest_palindromic_suffix("zzabcba") == "abcba"
assert longest_palindromic_suffix("Aa") == "a"
import random
random.seed(2)
for _ in range(300):
    s = "".join(random.choice("abc") for _ in range(random.randint(0, 10)))
    exp = max((s[i:] for i in range(len(s) + 1) if s[i:] == s[i:][::-1]), key=len)
    assert longest_palindromic_suffix(s) == exp
s = "x" + "a" * 20000
assert longest_palindromic_suffix(s) == "a" * 20000
''')

add(1, '''def min_chars_to_palindrome(string: str) -> int:
    """ Return the minimum number of characters that must be appended to the end of the string
    to make it a palindrome.
    >>> min_chars_to_palindrome('')
    0
    >>> min_chars_to_palindrome('cat')
    2
    >>> min_chars_to_palindrome('cata')
    1
    >>> min_chars_to_palindrome('aba')
    0
    """
''', '''
    for i in range(len(string)):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            return i
    return 0
''', '''
assert min_chars_to_palindrome("") == 0
assert min_chars_to_palindrome("a") == 0
assert min_chars_to_palindrome("ab") == 1
assert min_chars_to_palindrome("abc") == 2
assert min_chars_to_palindrome("abcb") == 1
assert min_chars_to_palindrome("aacecaaa") == 5
assert min_chars_to_palindrome("abcd") == 3
assert min_chars_to_palindrome("a" * 5000) == 0
assert min_chars_to_palindrome("ab" * 1000) == 1
import random
random.seed(3)
for _ in range(300):
    s = "".join(random.choice("ab") for _ in range(random.randint(0, 9)))
    k = min(k for k in range(len(s) + 1) if (s + s[:k][::-1]) == (s + s[:k][::-1])[::-1])
    assert min_chars_to_palindrome(s) == k
''')

add(1, '''def make_palindrome_ignore_case(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string, comparing characters
    case-insensitively. Find the longest suffix that is a palindrome ignoring case, then append
    the reverse of the remaining prefix (original characters, original case).
    >>> make_palindrome_ignore_case('')
    ''
    >>> make_palindrome_ignore_case('Abc')
    'AbcbA'
    >>> make_palindrome_ignore_case('abB')
    'abBa'
    """
''', '''
    low = string.lower()
    for i in range(len(string)):
        suffix = low[i:]
        if suffix == suffix[::-1]:
            return string + string[:i][::-1]
    return string
''', '''
assert make_palindrome_ignore_case("") == ""
assert make_palindrome_ignore_case("A") == "A"
assert make_palindrome_ignore_case("Aa") == "Aa"
assert make_palindrome_ignore_case("RaceCar") == "RaceCar"
assert make_palindrome_ignore_case("ab") == "aba"
assert make_palindrome_ignore_case("Ab") == "AbA"
assert make_palindrome_ignore_case("aB") == "aBa"
assert make_palindrome_ignore_case("xYz") == "xYzYx"
import random
random.seed(4)
for _ in range(300):
    s = "".join(random.choice("aAbB") for _ in range(random.randint(0, 8)))
    r = make_palindrome_ignore_case(s)
    assert r.startswith(s) and r.lower() == r.lower()[::-1]
    # shortest
    for k in range(len(s) + 1):
        c = s + s[:k][::-1]
        if c.lower() == c.lower()[::-1]:
            assert len(r) == len(c)
            break
''')

add(1, '''def count_palindromic_substrings(string: str) -> int:
    """ Count the substrings of the given string that are palindromes.
    Substrings with different start or end positions are counted separately,
    even if they consist of the same characters.
    >>> count_palindromic_substrings('')
    0
    >>> count_palindromic_substrings('abc')
    3
    >>> count_palindromic_substrings('aaa')
    6
    """
''', '''
    n = len(string)
    count = 0
    for center in range(2 * n - 1):
        lo = center // 2
        hi = lo + center % 2
        while lo >= 0 and hi < n and string[lo] == string[hi]:
            count += 1
            lo -= 1
            hi += 1
    return count
''', '''
assert count_palindromic_substrings("") == 0
assert count_palindromic_substrings("a") == 1
assert count_palindromic_substrings("ab") == 2
assert count_palindromic_substrings("abba") == 6
assert count_palindromic_substrings("racecar") == 10
import random
random.seed(5)
for _ in range(200):
    s = "".join(random.choice("ab") for _ in range(random.randint(0, 12)))
    exp = sum(1 for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] == s[i:j][::-1])
    assert count_palindromic_substrings(s) == exp
n = 1500
assert count_palindromic_substrings("a" * n) == n * (n + 1) // 2
''')

# ---------------- parent 2: string_sequence ----------------
add(2, '''def string_countdown(n: int) -> str:
    """ Return a string containing space-delimited numbers from n down to 0 inclusive.
    If n is negative, return an empty string.
    >>> string_countdown(0)
    '0'
    >>> string_countdown(3)
    '3 2 1 0'
    >>> string_countdown(-1)
    ''
    """
''', '''
    return " ".join(map(str, range(n, -1, -1)))
''', '''
assert string_countdown(0) == "0"
assert string_countdown(1) == "1 0"
assert string_countdown(10) == "10 9 8 7 6 5 4 3 2 1 0"
assert string_countdown(-5) == ""
assert len(string_countdown(10**5).split()) == 10**5 + 1
assert string_countdown(10**5).startswith("100000 99999")
''')

add(2, '''def string_sequence_step(start: int, stop: int, step: int) -> str:
    """ Return a string containing space-delimited numbers from start to stop inclusive,
    moving by step. The step may be negative. If no number fits, return an empty string.
    Raise ValueError if step is 0.
    >>> string_sequence_step(0, 10, 5)
    '0 5 10'
    >>> string_sequence_step(5, 1, -2)
    '5 3 1'
    >>> string_sequence_step(5, 1, 1)
    ''
    """
''', '''
    if step == 0:
        raise ValueError("step must not be zero")
    end = stop + 1 if step > 0 else stop - 1
    return " ".join(map(str, range(start, end, step)))
''', '''
assert string_sequence_step(3, 3, 1) == "3"
assert string_sequence_step(3, 3, -1) == "3"
assert string_sequence_step(0, 9, 3) == "0 3 6 9"
assert string_sequence_step(0, 10, 3) == "0 3 6 9"
assert string_sequence_step(-3, 3, 2) == "-3 -1 1 3"
assert string_sequence_step(10, 0, -5) == "10 5 0"
assert string_sequence_step(1, 0, 1) == ""
assert string_sequence_step(0, 1, -1) == ""
assert string_sequence_step(0, 10**6, 10**5) == " ".join(str(i * 10**5) for i in range(11))
try:
    string_sequence_step(0, 5, 0)
    assert False
except ValueError:
    pass
''')

add(2, '''def padded_sequence(n: int, width: int) -> str:
    """ Return a string containing space-delimited numbers from 0 to n inclusive,
    each number padded with leading zeros to at least the given width.
    >>> padded_sequence(3, 2)
    '00 01 02 03'
    >>> padded_sequence(10, 1)
    '0 1 2 3 4 5 6 7 8 9 10'
    """
''', '''
    return " ".join(str(i).zfill(width) for i in range(n + 1))
''', '''
assert padded_sequence(0, 1) == "0"
assert padded_sequence(0, 3) == "000"
assert padded_sequence(2, 0) == "0 1 2"
assert padded_sequence(11, 2) == "00 01 02 03 04 05 06 07 08 09 10 11"
assert padded_sequence(100, 2).endswith("99 100")
assert padded_sequence(-1, 2) == ""
assert len(padded_sequence(10**5, 6)) == (10**5 + 1) * 7 - 1
''')

add(2, '''def even_sequence(n: int) -> str:
    """ Return a string containing space-delimited even numbers starting from 0 up to n inclusive.
    If n is negative, return an empty string.
    >>> even_sequence(0)
    '0'
    >>> even_sequence(7)
    '0 2 4 6'
    >>> even_sequence(8)
    '0 2 4 6 8'
    """
''', '''
    return " ".join(map(str, range(0, n + 1, 2)))
''', '''
assert even_sequence(0) == "0"
assert even_sequence(1) == "0"
assert even_sequence(2) == "0 2"
assert even_sequence(9) == "0 2 4 6 8"
assert even_sequence(-4) == ""
assert even_sequence(-1) == ""
assert len(even_sequence(10**6).split()) == 500001
''')

add(2, '''def sequence_without_digit(n: int, d: int) -> str:
    """ Return a string containing space-delimited numbers from 0 to n inclusive,
    skipping every number whose decimal representation contains the digit d (0-9).
    If every number is skipped, return an empty string.
    >>> sequence_without_digit(12, 1)
    '0 2 3 4 5 6 7 8 9'
    >>> sequence_without_digit(5, 0)
    '1 2 3 4 5'
    """
''', '''
    digit = str(d)
    return " ".join(str(i) for i in range(n + 1) if digit not in str(i))
''', '''
assert sequence_without_digit(0, 0) == ""
assert sequence_without_digit(0, 5) == "0"
assert sequence_without_digit(20, 2) == "0 1 3 4 5 6 7 8 9 10 11 13 14 15 16 17 18 19"
assert sequence_without_digit(25, 9).split()[-1] == "25"
assert sequence_without_digit(100, 1).split()[-1] == "99"
assert sequence_without_digit(-3, 1) == ""
assert len(sequence_without_digit(10**5, 7).split()) == sum(1 for i in range(10**5 + 1) if "7" not in str(i))
''')

# ---------------- parent 3: filter_integers ----------------
add(3, '''from typing import List, Any


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats.
    Integers and booleans are not floats.
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    >>> filter_floats([1, 2.5, True, 'abc', {}, [], 0.0])
    [2.5, 0.0]
    """
''', '''
    return [x for x in values if type(x) is float]
''', '''
assert filter_floats([]) == []
assert filter_floats([1, 2, 3]) == []
assert filter_floats([1.0, 2.0]) == [1.0, 2.0]
assert filter_floats([True, False, 1, 0]) == []
assert filter_floats([-1.5, None, "1.5", 2.5e10, float("inf")]) == [-1.5, 2.5e10, float("inf")]
assert filter_floats([[1.5], (2.5,), {3.5}]) == []
assert len(filter_floats([0.5, 1] * 50000)) == 50000
''')

add(3, '''from typing import List, Any


def filter_booleans(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for booleans.
    The integers 0 and 1 are not booleans.
    >>> filter_booleans([1, True, 0, False, 'True'])
    [True, False]
    >>> filter_booleans([None, 3.14, []])
    []
    """
''', '''
    return [x for x in values if type(x) is bool]
''', '''
assert filter_booleans([]) == []
assert filter_booleans([0, 1, 2]) == []
assert filter_booleans([True, True, False]) == [True, True, False]
assert filter_booleans([1.0, 0.0, "", None, [], {}]) == []
assert filter_booleans([False, 0, True, 1, False]) == [False, True, False]
assert filter_booleans([[True], (False,)]) == []
assert filter_booleans([True, 0] * 10000) == [True] * 10000
''')

add(3, '''from typing import List, Any


def flatten_integers(values: List[Any]) -> List[int]:
    """ Recursively flatten nested lists and tuples and return only the integers, in order.
    Booleans are not integers.
    >>> flatten_integers([1, [2, ['a', 3]], (4, [5.5, True])])
    [1, 2, 3, 4]
    >>> flatten_integers([[], [[]], 'abc'])
    []
    """
''', '''
    result = []
    for x in values:
        if isinstance(x, (list, tuple)):
            result.extend(flatten_integers(x))
        elif type(x) is int:
            result.append(x)
    return result
''', '''
assert flatten_integers([]) == []
assert flatten_integers([1, 2, 3]) == [1, 2, 3]
assert flatten_integers([True, False, 0, 1]) == [0, 1]
assert flatten_integers([[[[7]]], 8]) == [7, 8]
assert flatten_integers(["12", 1.0, None, {1: 2}, {3}]) == []
assert flatten_integers([-1, [-2, (-3,)]]) == [-1, -2, -3]
deep = [1]
for _ in range(200):
    deep = [deep, 2]
r = flatten_integers(deep)
assert len(r) == 201 and r[0] == 1 and r.count(2) == 200
assert flatten_integers([[1, 2]] * 20000) == [1, 2] * 20000
''')

add(3, '''from typing import List, Any


def filter_digit_strings(values: List[Any]) -> List[int]:
    """ From a list of any python values keep only the strings that are non-empty and consist
    only of the ASCII digits 0-9, and return them converted to integers, in order.
    >>> filter_digit_strings(['12', 'a1', '', 7, '007'])
    [12, 7]
    >>> filter_digit_strings(['-5', '3.5', ' 4'])
    []
    """
''', '''
    result = []
    for x in values:
        if type(x) is str and x != "" and all(c in "0123456789" for c in x):
            result.append(int(x))
    return result
''', '''
assert filter_digit_strings([]) == []
assert filter_digit_strings(["0"]) == [0]
assert filter_digit_strings(["12", "a1", "", "007"]) == [12, 7]
assert filter_digit_strings([5, 5.0, None, True]) == []
assert filter_digit_strings(["\\u00b2", "\\u0663", "\\uff11", "1\\u00b2"]) == []
assert filter_digit_strings(["+1", "-1", "1e3", "1_0", "1 "]) == []
assert filter_digit_strings(["9" * 30]) == [10**30 - 1]
assert filter_digit_strings(["1", ["2"], ("3",)]) == [1]
assert len(filter_digit_strings(["42"] * 50000)) == 50000
''')

add(3, '''from typing import List, Any, Optional


def first_integer(values: List[Any]) -> Optional[int]:
    """ Return the first integer in the given list of any python values, or None if there is none.
    Booleans are not integers.
    >>> first_integer(['a', 3.14, 5, 7])
    5
    >>> first_integer([True, 'x']) is None
    True
    """
''', '''
    for x in values:
        if type(x) is int:
            return x
    return None
''', '''
assert first_integer([]) is None
assert first_integer([1]) == 1
assert first_integer([0]) == 0
assert first_integer([True, False, 2]) == 2
assert first_integer([1.0, "1", None, -4, 5]) == -4
assert first_integer([[1], (2,)]) is None
assert first_integer([2.5] * 100000 + [9]) == 9
assert first_integer([10**30]) == 10**30
''')

# ---------------- parent 4: factorize ----------------
add(4, '''def count_prime_factors(n: int) -> int:
    """ Return the number of prime factors of the given integer n >= 1, counted with multiplicity.
    For n = 1 the answer is 0.
    >>> count_prime_factors(1)
    0
    >>> count_prime_factors(8)
    3
    >>> count_prime_factors(70)
    3
    """
''', '''
    count = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            count += 1
        i += 1
    if n > 1:
        count += 1
    return count
''', '''
assert count_prime_factors(1) == 0
assert count_prime_factors(2) == 1
assert count_prime_factors(4) == 2
assert count_prime_factors(12) == 3
assert count_prime_factors(97) == 1
assert count_prime_factors(2**40) == 40
assert count_prime_factors(2**20 * 3**10 * 5) == 31
assert count_prime_factors(999999999989) == 1
assert count_prime_factors(1000003 * 1000033) == 2
def brute(n):
    c = 0
    d = 2
    while n > 1:
        while n % d == 0:
            n //= d
            c += 1
        d += 1
    return c
for n in range(1, 500):
    assert count_prime_factors(n) == brute(n)
''')

add(4, '''from typing import List


def distinct_prime_factors(n: int) -> List[int]:
    """ Return the sorted list of distinct prime factors of the given integer n >= 1.
    For n = 1 return an empty list.
    >>> distinct_prime_factors(1)
    []
    >>> distinct_prime_factors(8)
    [2]
    >>> distinct_prime_factors(70)
    [2, 5, 7]
    """
''', '''
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        result.append(n)
    return result
''', '''
assert distinct_prime_factors(1) == []
assert distinct_prime_factors(2) == [2]
assert distinct_prime_factors(36) == [2, 3]
assert distinct_prime_factors(49) == [7]
assert distinct_prime_factors(2 * 3 * 5 * 7 * 11 * 13) == [2, 3, 5, 7, 11, 13]
assert distinct_prime_factors(2**60) == [2]
assert distinct_prime_factors(999999999989) == [999999999989]
assert distinct_prime_factors(1000003 * 1000033) == [1000003, 1000033]
for n in range(1, 400):
    exp = [p for p in range(2, n + 1) if n % p == 0 and all(p % q for q in range(2, p))]
    assert distinct_prime_factors(n) == exp
''')

add(4, '''from typing import Dict


def factorize_dict(n: int) -> Dict[int, int]:
    """ Return a dictionary that maps each prime factor of the integer n >= 1 to its exponent.
    For n = 1 return an empty dictionary.
    >>> factorize_dict(1)
    {}
    >>> factorize_dict(8)
    {2: 3}
    >>> factorize_dict(180)
    {2: 2, 3: 2, 5: 1}
    """
''', '''
    result = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            result[i] = result.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result
''', '''
assert factorize_dict(1) == {}
assert factorize_dict(2) == {2: 1}
assert factorize_dict(9) == {3: 2}
assert factorize_dict(360) == {2: 3, 3: 2, 5: 1}
assert factorize_dict(2**30 * 3) == {2: 30, 3: 1}
assert factorize_dict(999999999989) == {999999999989: 1}
assert factorize_dict(1000003**2) == {1000003: 2}
assert list(factorize_dict(2310)) == [2, 3, 5, 7, 11]
for n in range(1, 300):
    d = factorize_dict(n)
    prod = 1
    for p, e in d.items():
        prod *= p ** e
    assert prod == n
''')

add(4, '''def second_largest_prime_factor(n: int) -> int:
    """ Return the second largest DISTINCT prime factor of the integer n > 1.
    If n has fewer than two distinct prime factors, return -1.
    >>> second_largest_prime_factor(30)
    3
    >>> second_largest_prime_factor(2048)
    -1
    >>> second_largest_prime_factor(97)
    -1
    """
''', '''
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors[-2] if len(factors) >= 2 else -1
''', '''
assert second_largest_prime_factor(2) == -1
assert second_largest_prime_factor(6) == 2
assert second_largest_prime_factor(30) == 3
assert second_largest_prime_factor(12) == 2
assert second_largest_prime_factor(49) == -1
assert second_largest_prime_factor(2048) == -1
assert second_largest_prime_factor(13195) == 13
assert second_largest_prime_factor(2 ** 50 * 3 ** 20) == 2
assert second_largest_prime_factor(999999999989) == -1
assert second_largest_prime_factor(2 * 999999937) == 2
assert second_largest_prime_factor(1000003 * 999983) == 999983
assert second_largest_prime_factor(1000003 ** 2) == -1
for n in range(2, 400):
    ps = [p for p in range(2, n + 1) if n % p == 0 and all(p % q for q in range(2, p))]
    assert second_largest_prime_factor(n) == (ps[-2] if len(ps) > 1 else -1), n
''')

add(4, '''def is_smooth(n: int, bound: int) -> bool:
    """ Return True if every prime factor of the integer n >= 1 is less than or equal to bound.
    The number 1 is smooth for every bound.
    >>> is_smooth(1, 2)
    True
    >>> is_smooth(60, 5)
    True
    >>> is_smooth(70, 5)
    False
    """
''', '''
    p = 2
    while p * p <= n:
        if n % p == 0:
            if p > bound:
                return False
            while n % p == 0:
                n //= p
        p += 1
    return n == 1 or n <= bound
''', '''
assert is_smooth(1, 1) is True
assert is_smooth(1, 100) is True
assert is_smooth(2, 1) is False
assert is_smooth(2, 2) is True
assert is_smooth(49, 6) is False
assert is_smooth(49, 7) is True
assert is_smooth(97, 96) is False
assert is_smooth(97, 97) is True
assert is_smooth(2**60 * 3**30, 3) is True
assert is_smooth(2**60 * 5, 3) is False
assert is_smooth(999999999989, 10**12) is True
assert is_smooth(999999999989, 999999999988) is False
def brute(n, b):
    d = 2
    while n > 1:
        while n % d == 0:
            if d > b:
                return False
            n //= d
        d += 1
    return True
for n in range(1, 200):
    for b in range(1, 15):
        assert is_smooth(n, b) == brute(n, b), (n, b)
''')

# ---------------- parent 5: remove_duplicates ----------------
add(5, '''from typing import List


def keep_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, keep only elements that occur more than once.
    Keep every occurrence and keep the order of elements the same as in the input.
    >>> keep_duplicates([1, 2, 3, 2, 4])
    [2, 2]
    >>> keep_duplicates([1, 2, 3])
    []
    """
''', '''
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return [number for number in numbers if counts[number] > 1]
''', '''
assert keep_duplicates([]) == []
assert keep_duplicates([1]) == []
assert keep_duplicates([1, 1]) == [1, 1]
assert keep_duplicates([3, 1, 3, 1, 2]) == [3, 1, 3, 1]
assert keep_duplicates([-1, 1, -1]) == [-1, -1]
assert keep_duplicates([0, 0, 0]) == [0, 0, 0]
assert keep_duplicates(list(range(100000))) == []
assert keep_duplicates(list(range(50000)) * 2) == list(range(50000)) * 2
''')

add(5, '''from typing import List


def unique_in_order(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove repeated elements so that each value stays only once,
    at the position of its first occurrence.
    >>> unique_in_order([1, 2, 3, 2, 4, 1])
    [1, 2, 3, 4]
    >>> unique_in_order([])
    []
    """
''', '''
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result
''', '''
assert unique_in_order([]) == []
assert unique_in_order([5]) == [5]
assert unique_in_order([5, 5, 5]) == [5]
assert unique_in_order([3, 1, 3, 2, 1, 2]) == [3, 1, 2]
assert unique_in_order([0, -0, 1, -1, 1]) == [0, 1, -1]
assert unique_in_order(list(range(100000)) * 3) == list(range(100000))
assert unique_in_order([10**20, 10**20, 1]) == [10**20, 1]
''')

add(5, '''from typing import List


def remove_adjacent_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, collapse every run of equal consecutive elements into one element.
    Equal elements that are not next to each other are kept.
    >>> remove_adjacent_duplicates([1, 1, 2, 2, 2, 1])
    [1, 2, 1]
    >>> remove_adjacent_duplicates([3, 3])
    [3]
    """
''', '''
    result = []
    for number in numbers:
        if not result or result[-1] != number:
            result.append(number)
    return result
''', '''
assert remove_adjacent_duplicates([]) == []
assert remove_adjacent_duplicates([1]) == [1]
assert remove_adjacent_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_adjacent_duplicates([0, 0, 0, 0]) == [0]
assert remove_adjacent_duplicates([1, 2, 1, 2]) == [1, 2, 1, 2]
assert remove_adjacent_duplicates([-1, -1, 1, 1, -1]) == [-1, 1, -1]
assert remove_adjacent_duplicates([7] * 100000) == [7]
assert remove_adjacent_duplicates([1, 2] * 50000) == [1, 2] * 50000
''')

add(5, '''from typing import List


def remove_exact_count(numbers: List[int], k: int) -> List[int]:
    """ From a list of integers, remove all elements that occur exactly k times in the list.
    Keep order of elements left the same as in the input.
    >>> remove_exact_count([1, 2, 3, 2, 4], 2)
    [1, 3, 4]
    >>> remove_exact_count([1, 1, 1, 2], 1)
    [1, 1, 1]
    """
''', '''
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return [number for number in numbers if counts[number] != k]
''', '''
assert remove_exact_count([], 1) == []
assert remove_exact_count([1, 2, 3], 1) == []
assert remove_exact_count([1, 2, 3], 2) == [1, 2, 3]
assert remove_exact_count([1, 1, 2, 2, 2], 3) == [1, 1]
assert remove_exact_count([1, 1, 2, 2, 2], 0) == [1, 1, 2, 2, 2]
assert remove_exact_count([4, 4, 4, 4], 4) == []
assert remove_exact_count([-1, -1, 5], 2) == [5]
assert remove_exact_count(list(range(1000)) * 2 + [5000], 2) == [5000]
assert remove_exact_count([0] * 100000, 99999) == [0] * 100000
''')

add(5, '''from typing import List


def remove_duplicate_words(words: List[str]) -> List[str]:
    """ From a list of words, remove all words that occur more than once, ignoring case.
    Words that are left keep their original spelling and order.
    >>> remove_duplicate_words(['Cat', 'dog', 'cat', 'Bird'])
    ['dog', 'Bird']
    >>> remove_duplicate_words(['a', 'A', 'a'])
    []
    """
''', '''
    counts = {}
    for word in words:
        key = word.lower()
        counts[key] = counts.get(key, 0) + 1
    return [word for word in words if counts[word.lower()] == 1]
''', '''
assert remove_duplicate_words([]) == []
assert remove_duplicate_words(["x"]) == ["x"]
assert remove_duplicate_words(["x", "X"]) == []
assert remove_duplicate_words(["", "", "a"]) == ["a"]
assert remove_duplicate_words(["Ab", "aB", "ab ", "AB"]) == ["ab "]
assert remove_duplicate_words(["one", "two", "three"]) == ["one", "two", "three"]
assert remove_duplicate_words(["a" * 100, "A" * 100]) == []
assert remove_duplicate_words([str(i) for i in range(50000)]) == [str(i) for i in range(50000)]
''')
