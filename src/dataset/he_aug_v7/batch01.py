# parents: HumanEval/10 (make_palindrome), /12 (longest), /15 (string_sequence), /22 (filter_integers), /25 (factorize)
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------------------------------------------------------- HumanEval/10
add(10, '''def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def palindrome_by_prepending(string: str) -> str:
    """ Find the shortest palindrome that ends with a supplied string.
    Algorithm idea is simple:
    - Find the longest prefix of supplied string that is a palindrome.
    - Prepend to the beginning of the string reverse of a string suffix that comes after the palindromic prefix.
    >>> palindrome_by_prepending('')
    ''
    >>> palindrome_by_prepending('cat')
    'tacat'
    >>> palindrome_by_prepending('catac')
    'catac'
    """
''', '''
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            return string[i:][::-1] + string
''', '''
import itertools
def ref(s):
    n = len(s)
    for add in range(n + 1):
        cand = s[n - add:][::-1] + s if add else s
        if cand == cand[::-1]:
            return cand
assert palindrome_by_prepending("") == ""
assert palindrome_by_prepending("a") == "a"
assert palindrome_by_prepending("ab") == "bab"
assert palindrome_by_prepending("cat") == "tacat"
assert palindrome_by_prepending("catac") == "catac"
assert palindrome_by_prepending("racecar") == "racecar"
assert palindrome_by_prepending("aab") == "baab"
assert palindrome_by_prepending("abb") == "bbabb"
assert palindrome_by_prepending("aaaa") == "aaaa"
assert palindrome_by_prepending("abcd") == "dcbabcd"
assert palindrome_by_prepending("xyzzy") == "yzzyxyzzy"
assert palindrome_by_prepending("Aa") == "aAa"
for n in range(0, 9):
    for t in itertools.product("ab", repeat=n):
        s = "".join(t)
        r = palindrome_by_prepending(s)
        assert r == ref(s), s
        assert r == r[::-1] and r.endswith(s)
assert palindrome_by_prepending("a" * 5000) == "a" * 5000
r = palindrome_by_prepending("ab" * 1500)
assert r == "b" + "ab" * 1500 and r == r[::-1]
r = palindrome_by_prepending("a" * 2000 + "b")
assert r == "b" + "a" * 2000 + "b" and r == r[::-1]
''')

add(10, '''def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def longest_palindromic_suffix(string: str) -> str:
    """ Find the longest postfix of a supplied string that is a palindrome.
    The empty string counts as a palindrome, so the result always exists.
    >>> longest_palindromic_suffix('')
    ''
    >>> longest_palindromic_suffix('cat')
    't'
    >>> longest_palindromic_suffix('cata')
    'ata'
    >>> longest_palindromic_suffix('racecar')
    'racecar'
    """
''', '''
    for i in range(len(string) + 1):
        if is_palindrome(string[i:]):
            return string[i:]
''', '''
import itertools
def ref(s):
    best = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if j == len(s) and s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(best):
                best = s[i:j]
    return best
assert longest_palindromic_suffix("") == ""
assert longest_palindromic_suffix("a") == "a"
assert longest_palindromic_suffix("ab") == "b"
assert longest_palindromic_suffix("abb") == "bb"
assert longest_palindromic_suffix("cata") == "ata"
assert longest_palindromic_suffix("cat") == "t"
assert longest_palindromic_suffix("xracecar") == "racecar"
assert longest_palindromic_suffix("aaaa") == "aaaa"
assert longest_palindromic_suffix("abcba") == "abcba"
assert longest_palindromic_suffix("abcbab") == "bab"
assert longest_palindromic_suffix("Aa") == "a"
for n in range(0, 10):
    for t in itertools.product("ab", repeat=n):
        s = "".join(t)
        r = longest_palindromic_suffix(s)
        assert r == ref(s), s
        assert s.endswith(r) and r == r[::-1]
assert longest_palindromic_suffix("b" + "a" * 3000) == "a" * 3000
assert longest_palindromic_suffix("ab" * 1000) == "b" + "ab" * 999
assert longest_palindromic_suffix("ab" * 1000 + "c") == "c"
''')

add(10, '''def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def min_appends_for_palindrome(string: str) -> int:
    """ Return the minimal number of characters that have to be appended to the end
    of a supplied string so that the result is a palindrome.
    >>> min_appends_for_palindrome('')
    0
    >>> min_appends_for_palindrome('cat')
    2
    >>> min_appends_for_palindrome('cata')
    1
    >>> min_appends_for_palindrome('level')
    0
    """
''', '''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return i
    return 0
''', '''
import itertools
def ref(s):
    k = 0
    while True:
        for extra in itertools.product("abc", repeat=k):
            c = s + "".join(extra)
            if c == c[::-1]:
                return k
        k += 1
assert min_appends_for_palindrome("") == 0
assert min_appends_for_palindrome("a") == 0
assert min_appends_for_palindrome("ab") == 1
assert min_appends_for_palindrome("abc") == 2
assert min_appends_for_palindrome("aba") == 0
assert min_appends_for_palindrome("abab") == 1
assert min_appends_for_palindrome("aab") == 2
assert min_appends_for_palindrome("abcd") == 3
assert min_appends_for_palindrome("aaaaab") == 5
assert min_appends_for_palindrome("baaaaa") == 1
assert min_appends_for_palindrome("racecars") == 7
assert min_appends_for_palindrome("Aa") == 1
for n in range(0, 7):
    for t in itertools.product("abc", repeat=n):
        s = "".join(t)
        assert min_appends_for_palindrome(s) == ref(s), s
assert min_appends_for_palindrome("a" * 4000 + "b") == 4000
assert min_appends_for_palindrome("ab" * 1500) == 1
''')

add(10, '''def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome_nocase(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string, where palindromes are
    checked ignoring letter case ('Aba' is a palindrome). The supplied string is kept unchanged.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome ignoring case.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_nocase('')
    ''
    >>> make_palindrome_nocase('Cat')
    'CataC'
    >>> make_palindrome_nocase('abB')
    'abBa'
    """
''', '''
    for i in range(len(string) + 1):
        if is_palindrome(string[i:].lower()):
            return string + string[:i][::-1]
''', '''
import itertools
def ref(s):
    for k in range(len(s) + 1):
        c = s + s[:k][::-1]
        if c.lower() == c.lower()[::-1]:
            return c
assert make_palindrome_nocase("") == ""
assert make_palindrome_nocase("a") == "a"
assert make_palindrome_nocase("Cat") == "CatC"[0:3] + "aC"
assert make_palindrome_nocase("AbA") == "AbA"
assert make_palindrome_nocase("abB") == "abBa"
assert make_palindrome_nocase("Ab") == "AbA"
assert make_palindrome_nocase("aB") == "aBa"
assert make_palindrome_nocase("AaAa") == "AaAa"
assert make_palindrome_nocase("Aa") == "Aa"
assert make_palindrome_nocase("xYz") == "xYzYx"
assert make_palindrome_nocase("RaceCar") == "RaceCar"
assert make_palindrome_nocase("abc1") == "abc1cba"
for n in range(0, 7):
    for t in itertools.product("aAb", repeat=n):
        s = "".join(t)
        r = make_palindrome_nocase(s)
        assert r == ref(s), s
        assert r.startswith(s) and r.lower() == r.lower()[::-1]
big = "Ab" * 1200
r = make_palindrome_nocase(big)
assert r.startswith(big) and r.lower() == r.lower()[::-1] and len(r) == 2401
''')

add(10, '''def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def count_palindromic_suffixes(string: str) -> int:
    """ Count how many non-empty suffixes of a supplied string are palindromes.
    Suffixes at different starting positions are counted separately, even if they are equal.
    >>> count_palindromic_suffixes('')
    0
    >>> count_palindromic_suffixes('cat')
    1
    >>> count_palindromic_suffixes('aaa')
    3
    >>> count_palindromic_suffixes('abaaba')
    3
    """
''', '''
    return sum(1 for i in range(len(string)) if is_palindrome(string[i:]))
''', '''
import itertools
def ref(s):
    c = 0
    for i in range(len(s)):
        t = s[i:]
        ok = True
        for a in range(len(t) // 2):
            if t[a] != t[len(t) - 1 - a]:
                ok = False
        c += ok
    return c
assert count_palindromic_suffixes("") == 0
assert count_palindromic_suffixes("a") == 1
assert count_palindromic_suffixes("ab") == 1
assert count_palindromic_suffixes("aa") == 2
assert count_palindromic_suffixes("aba") == 2
assert count_palindromic_suffixes("abaaba") == 3
assert count_palindromic_suffixes("abc") == 1
assert count_palindromic_suffixes("aaa") == 3
assert count_palindromic_suffixes("baaa") == 3
assert count_palindromic_suffixes("abcba") == 2
assert count_palindromic_suffixes("Aa") == 1
assert count_palindromic_suffixes("a" * 2000) == 2000
assert count_palindromic_suffixes("ab" * 1000) == 1000
assert count_palindromic_suffixes("ab" * 1000 + "c") == 1
for n in range(0, 10):
    for t in itertools.product("ab", repeat=n):
        s = "".join(t)
        assert count_palindromic_suffixes(s) == ref(s), s
''')

# ---------------------------------------------------------------- HumanEval/12
add(12, '''from typing import List, Optional


def shortest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the shortest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> shortest([])

    >>> shortest(['a', 'b', 'c'])
    'a'
    >>> shortest(['aaa', 'bb', 'cc'])
    'bb'
    """
''', '''
    if not strings:
        return None

    minlen = min(len(x) for x in strings)
    for s in strings:
        if len(s) == minlen:
            return s
''', '''
assert shortest([]) is None
assert shortest(["a"]) == "a"
assert shortest([""]) == ""
assert shortest(["a", "b", "c"]) == "a"
assert shortest(["aaa", "bb", "cc"]) == "bb"
assert shortest(["bb", "cc", "aaa"]) == "bb"
assert shortest(["abc", "", "x", ""]) == ""
assert shortest(["abc", "de", "f", "g"]) == "f"
s = ["x", "y"]
assert shortest(s) is s[0]
t = ["ab", "cd"]
assert shortest(t) is t[0]
assert shortest(["  ", " "]) == " "
assert shortest(["Z", "a"]) == "Z"
assert shortest(["long" * 100, "mid" * 10, "mid" * 10]) == "mid" * 10
import random
random.seed(1)
for _ in range(300):
    L = [("a" * random.randint(0, 6)) + str(random.randint(0, 9)) for _ in range(random.randint(1, 8))]
    exp = min(L, key=len)
    assert shortest(L) == exp and shortest(L) is exp or shortest(L) == exp
    assert L.index(shortest(L)) == min(range(len(L)), key=lambda i: len(L[i]))
big = ["a" * 5 for _ in range(100000)] + ["b"]
assert shortest(big) == "b"
''')

add(12, '''from typing import List, Optional


def longest_last(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the last one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest_last([])

    >>> longest_last(['a', 'b', 'c'])
    'c'
    >>> longest_last(['aa', 'b', 'cc'])
    'cc'
    """
''', '''
    if not strings:
        return None

    best = strings[0]
    for s in strings:
        if len(s) >= len(best):
            best = s
    return best
''', '''
assert longest_last([]) is None
assert longest_last(["a"]) == "a"
assert longest_last([""]) == ""
assert longest_last(["", ""]) == ""
assert longest_last(["a", "b", "c"]) == "c"
assert longest_last(["aa", "b", "cc"]) == "cc"
assert longest_last(["aa", "bb", "c"]) == "bb"
assert longest_last(["abc", "x", "y"]) == "abc"
assert longest_last(["x", "abc", "y", "def", "g"]) == "def"
a, b = "xy", "zw"
assert longest_last([a, b]) is b
assert longest_last(["a" * 10, "b" * 9]) == "a" * 10
import random
random.seed(2)
for _ in range(300):
    L = [chr(97 + random.randint(0, 25)) * random.randint(0, 5) for _ in range(random.randint(1, 9))]
    m = max(len(x) for x in L)
    idx = max(i for i in range(len(L)) if len(L[i]) == m)
    assert longest_last(L) == L[idx]
big = ["a" * 3 for _ in range(100000)]
big[-1] = "b" * 3
assert longest_last(big) == "bbb"
assert longest_last([" ", "  ", "\\t\\t"]) == "\\t\\t"
''')

add(12, '''def longest_word(sentence: str) -> str:
    """ Return the longest word of a sentence. Words are separated by single or multiple spaces.
    Return the first one in case of multiple words of the same length.
    Return an empty string in case the sentence contains no words.
    >>> longest_word('')
    ''
    >>> longest_word('a bb ccc')
    'ccc'
    >>> longest_word('aa bb c')
    'aa'
    """
''', '''
    best = ""
    for w in sentence.split():
        if len(w) > len(best):
            best = w
    return best
''', '''
assert longest_word("") == ""
assert longest_word("   ") == ""
assert longest_word("a") == "a"
assert longest_word("a bb ccc") == "ccc"
assert longest_word("aa bb c") == "aa"
assert longest_word("  aa   bb  ") == "aa"
assert longest_word("x yy zz") == "yy"
assert longest_word("hello, world!") == "hello,"
assert longest_word("one two three four") == "three"
assert longest_word("ab\\tcdef") == "cdef"
assert longest_word("ab  cd  ef") == "ab"
assert longest_word("a" * 10000 + " " + "b" * 10001) == "b" * 10001
assert longest_word(" ".join(["w"] * 50000)) == "w"
import random
random.seed(3)
for _ in range(300):
    ws = ["".join(random.choice("abc") for _ in range(random.randint(1, 6))) for _ in range(random.randint(0, 7))]
    s = (" " * random.randint(0, 2)).join(["", ""]) + (" " * random.randint(1, 3)).join(ws)
    exp = ""
    for w in ws:
        if len(w) > len(exp):
            exp = w
    assert longest_word(s) == exp
''')

add(12, '''from typing import List


def index_of_longest(strings: List[str]) -> int:
    """ Out of list of strings, return the index of the longest one. Return the index of the first one
    in case of multiple strings of the same length. Return -1 in case the input list is empty.
    >>> index_of_longest([])
    -1
    >>> index_of_longest(['a', 'b', 'c'])
    0
    >>> index_of_longest(['a', 'bb', 'cc'])
    1
    """
''', '''
    best = -1
    for i, s in enumerate(strings):
        if best == -1 or len(s) > len(strings[best]):
            best = i
    return best
''', '''
assert index_of_longest([]) == -1
assert index_of_longest([""]) == 0
assert index_of_longest(["a"]) == 0
assert index_of_longest(["a", "b", "c"]) == 0
assert index_of_longest(["a", "bb", "cc"]) == 1
assert index_of_longest(["", "", "x"]) == 2
assert index_of_longest(["abc", "de", "abc"]) == 0
assert index_of_longest(["", ""]) == 0
assert index_of_longest(["ab", "abc", "abcd", "abc"]) == 2
assert index_of_longest(["abcd", "abc", "ab"]) == 0
assert index_of_longest([" ", "  ", " "]) == 1
import random
random.seed(4)
for _ in range(300):
    L = ["z" * random.randint(0, 5) for _ in range(random.randint(1, 9))]
    m = max(map(len, L))
    exp = [i for i, x in enumerate(L) if len(x) == m][0]
    assert index_of_longest(L) == exp
big = ["a"] * 100000 + ["bb"] + ["cc"]
assert index_of_longest(big) == 100000
''')

add(12, '''from typing import List


def longest_common_prefix(strings: List[str]) -> str:
    """ Return the longest string that is a prefix of every string of the list.
    Return an empty string in case the input list is empty or there is no common prefix.
    >>> longest_common_prefix([])
    ''
    >>> longest_common_prefix(['flower', 'flow', 'flight'])
    'fl'
    >>> longest_common_prefix(['dog', 'racecar'])
    ''
    """
''', '''
    if not strings:
        return ""

    first = min(strings)
    last = max(strings)
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]
''', '''
def ref(L):
    if not L:
        return ""
    p = ""
    for i in range(min(map(len, L))):
        if len({x[i] for x in L}) == 1:
            p += L[0][i]
        else:
            break
    return p
assert longest_common_prefix([]) == ""
assert longest_common_prefix([""]) == ""
assert longest_common_prefix(["abc"]) == "abc"
assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""
assert longest_common_prefix(["abc", "abc", "abc"]) == "abc"
assert longest_common_prefix(["abc", "ab", "abcd"]) == "ab"
assert longest_common_prefix(["", "abc"]) == ""
assert longest_common_prefix(["Abc", "abc"]) == ""
assert longest_common_prefix(["a", "a", ""]) == ""
assert longest_common_prefix(["interview", "internet", "interval", "intern"]) == "inter"
assert longest_common_prefix(["x" * 50000 + "a", "x" * 50000 + "b"]) == "x" * 50000
import random
random.seed(5)
for _ in range(400):
    L = ["".join(random.choice("ab") for _ in range(random.randint(0, 6))) for _ in range(random.randint(0, 6))]
    assert longest_common_prefix(L) == ref(L), L
''')

# ---------------------------------------------------------------- HumanEval/15
add(15, '''def count_down_string(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from n down to 0 inclusive.
    >>> count_down_string(0)
    '0'
    >>> count_down_string(5)
    '5 4 3 2 1 0'
    """
''', '''
    return " ".join(map(str, range(n, -1, -1)))
''', '''
assert count_down_string(0) == "0"
assert count_down_string(1) == "1 0"
assert count_down_string(5) == "5 4 3 2 1 0"
assert count_down_string(10) == "10 9 8 7 6 5 4 3 2 1 0"
assert count_down_string(2) == "2 1 0"
assert count_down_string(3) == "3 2 1 0"
assert count_down_string(9) == "9 8 7 6 5 4 3 2 1 0"
assert count_down_string(12).split(" ")[0] == "12"
assert count_down_string(100).split(" ")[-1] == "0"
assert count_down_string(100).split(" ")[1] == "99"
for n in range(0, 200):
    s = count_down_string(n)
    assert s.split(" ") == [str(i) for i in range(n, -1, -1)]
    assert "  " not in s and not s.startswith(" ") and not s.endswith(" ")
big = count_down_string(200000)
assert big.startswith("200000 199999 ") and big.endswith(" 1 0")
assert len(big.split(" ")) == 200001
''')

add(15, '''def string_sequence_step(n: int, step: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive,
    increasing by step each time. step is a positive integer.
    >>> string_sequence_step(0, 3)
    '0'
    >>> string_sequence_step(10, 5)
    '0 5 10'
    >>> string_sequence_step(10, 3)
    '0 3 6 9'
    """
''', '''
    return " ".join(map(str, range(0, n + 1, step)))
''', '''
assert string_sequence_step(0, 1) == "0"
assert string_sequence_step(0, 7) == "0"
assert string_sequence_step(5, 1) == "0 1 2 3 4 5"
assert string_sequence_step(10, 5) == "0 5 10"
assert string_sequence_step(10, 3) == "0 3 6 9"
assert string_sequence_step(3, 10) == "0"
assert string_sequence_step(9, 9) == "0 9"
assert string_sequence_step(8, 9) == "0"
assert string_sequence_step(20, 4) == "0 4 8 12 16 20"
assert string_sequence_step(19, 4) == "0 4 8 12 16"
for n in range(0, 60):
    for st in range(1, 20):
        exp = " ".join(str(i) for i in range(0, n + 1) if i % st == 0)
        assert string_sequence_step(n, st) == exp
assert string_sequence_step(10 ** 6, 10 ** 6) == "0 1000000"
assert len(string_sequence_step(10 ** 6, 1).split(" ")) == 10 ** 6 + 1
''')

add(15, '''def even_sequence(n: int) -> str:
    """ Return a string containing space-delimited even numbers starting from 0 upto n inclusive.
    >>> even_sequence(0)
    '0'
    >>> even_sequence(5)
    '0 2 4'
    >>> even_sequence(6)
    '0 2 4 6'
    """
''', '''
    return " ".join(str(i) for i in range(0, n + 1, 2))
''', '''
assert even_sequence(0) == "0"
assert even_sequence(1) == "0"
assert even_sequence(2) == "0 2"
assert even_sequence(3) == "0 2"
assert even_sequence(5) == "0 2 4"
assert even_sequence(6) == "0 2 4 6"
assert even_sequence(10) == "0 2 4 6 8 10"
assert even_sequence(11) == "0 2 4 6 8 10"
assert even_sequence(7) == "0 2 4 6"
assert even_sequence(8) == "0 2 4 6 8"
assert even_sequence(100).split(" ")[-1] == "100"
for n in range(0, 300):
    assert even_sequence(n) == " ".join(str(i) for i in range(n + 1) if i % 2 == 0)
big = even_sequence(10 ** 6)
assert big.endswith(" 999998 1000000") and big.startswith("0 2 4")
assert len(big.split()) == 500001
''')

add(15, '''def string_range(a: int, b: int) -> str:
    """ Return a string containing comma-delimited numbers starting from a and going to b inclusive.
    If a is greater than b, the numbers are going down from a to b.
    >>> string_range(0, 0)
    '0'
    >>> string_range(1, 4)
    '1,2,3,4'
    >>> string_range(3, -1)
    '3,2,1,0,-1'
    """
''', '''
    if a <= b:
        return ",".join(map(str, range(a, b + 1)))
    return ",".join(map(str, range(a, b - 1, -1)))
''', '''
assert string_range(0, 0) == "0"
assert string_range(5, 5) == "5"
assert string_range(-5, -5) == "-5"
assert string_range(1, 4) == "1,2,3,4"
assert string_range(4, 1) == "4,3,2,1"
assert string_range(3, -1) == "3,2,1,0,-1"
assert string_range(-3, 1) == "-3,-2,-1,0,1"
assert string_range(-1, -3) == "-1,-2,-3"
assert string_range(-3, -1) == "-3,-2,-1"
assert string_range(0, 3) == "0,1,2,3"
assert string_range(10, 8) == "10,9,8"
for a in range(-12, 13):
    for b in range(-12, 13):
        exp = list(range(a, b + 1)) if a <= b else list(range(a, b - 1, -1))
        assert string_range(a, b).split(",") == [str(x) for x in exp]
assert len(string_range(-10 ** 5, 10 ** 5).split(",")) == 200001
assert len(string_range(10 ** 5, -10 ** 5).split(",")) == 200001
''')

add(15, '''def squares_sequence(n: int) -> str:
    """ Return a string containing space-delimited squares of the numbers starting from 0 upto n inclusive.
    >>> squares_sequence(0)
    '0'
    >>> squares_sequence(4)
    '0 1 4 9 16'
    """
''', '''
    return " ".join(str(i * i) for i in range(n + 1))
''', '''
assert squares_sequence(0) == "0"
assert squares_sequence(1) == "0 1"
assert squares_sequence(2) == "0 1 4"
assert squares_sequence(4) == "0 1 4 9 16"
assert squares_sequence(10) == "0 1 4 9 16 25 36 49 64 81 100"
for n in range(0, 100):
    parts = squares_sequence(n).split(" ")
    assert len(parts) == n + 1
    assert all(int(p) == i * i for i, p in enumerate(parts))
big = squares_sequence(10 ** 5)
assert big.endswith(" 9999800001 10000000000")
assert big.count(" ") == 10 ** 5
assert squares_sequence(3) == "0 1 4 9"
assert squares_sequence(5) == "0 1 4 9 16 25"
assert squares_sequence(6).split(" ")[-1] == "36"
assert squares_sequence(7).count(" ") == 7
assert squares_sequence(12).split(" ")[-1] == "144"
''')

# ---------------------------------------------------------------- HumanEval/22
add(22, '''from typing import List, Any


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    >>> filter_strings([1, 2, 3, 'abc', {}, []])
    ['abc']
    """
''', '''
    return [x for x in values if isinstance(x, str)]
''', '''
assert filter_strings([]) == []
assert filter_strings(["a", 3.14, 5]) == ["a"]
assert filter_strings([1, 2, 3, "abc", {}, []]) == ["abc"]
assert filter_strings(["", "x", ""]) == ["", "x", ""]
assert filter_strings([1, 2.5, None, True, [], {}, (), set()]) == []
assert filter_strings([b"bytes", "str"]) == ["str"]
assert filter_strings(["1", 1, "2", 2]) == ["1", "2"]
assert filter_strings([["a"], ("b",), {"c": "d"}, "e"]) == ["e"]
assert filter_strings([None, "None"]) == ["None"]
assert filter_strings(["b", "a", "b"]) == ["b", "a", "b"]
x = ["q"]
assert filter_strings(x) == ["q"] and x == ["q"]
assert filter_strings(["é", "日本", 5]) == ["é", "日本"]
assert filter_strings(["a"] * 100000 + [1] * 100000) == ["a"] * 100000
assert filter_strings([str(i) if i % 2 else i for i in range(1000)]) == [str(i) for i in range(1000) if i % 2]
''')

add(22, '''from typing import List, Any


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floating point numbers
    (integers and booleans are not floats)
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    >>> filter_floats([1, 2.0, 3, 'abc', {}, []])
    [2.0]
    """
''', '''
    return [x for x in values if isinstance(x, float)]
''', '''
assert filter_floats([]) == []
assert filter_floats(["a", 3.14, 5]) == [3.14]
assert filter_floats([1, 2.0, 3, "abc", {}, []]) == [2.0]
assert filter_floats([1, 2, 3]) == []
assert filter_floats([True, False, 1, 0]) == []
assert filter_floats([0.0, -0.5, 1e10, 2.5e-3]) == [0.0, -0.5, 1e10, 2.5e-3]
assert filter_floats([float("inf"), float("-inf")]) == [float("inf"), float("-inf")]
r = filter_floats([float("nan"), 1.0])
assert len(r) == 2 and r[0] != r[0] and r[1] == 1.0
assert filter_floats(["1.5", 1.5]) == [1.5]
assert filter_floats([[1.5], (2.5,), {3.5}, 4.5]) == [4.5]
assert filter_floats([1.0, 1, 1.0]) == [1.0, 1.0]
assert filter_floats([None, 2.0, None]) == [2.0]
assert filter_floats([complex(1, 2), 1.5]) == [1.5]
assert filter_floats([0.5] * 100000 + [1] * 100000) == [0.5] * 100000
''')

add(22, '''from typing import List, Any


def filter_lists(values: List[Any]) -> List[list]:
    """ Filter given list of any python values only for lists (tuples and other containers are not lists)
    >>> filter_lists(['a', 3.14, [5]])
    [[5]]
    >>> filter_lists([1, 2, 3, 'abc', {}, [], (1, 2), [1, [2]]])
    [[], [1, [2]]]
    """
''', '''
    return [x for x in values if isinstance(x, list)]
''', '''
assert filter_lists([]) == []
assert filter_lists(["a", 3.14, [5]]) == [[5]]
assert filter_lists([1, 2, 3, "abc", {}, [], (1, 2), [1, [2]]]) == [[], [1, [2]]]
assert filter_lists([(1,), {1}, {1: 2}, "[]", None]) == []
assert filter_lists([[], [], []]) == [[], [], []]
assert filter_lists([[1], [2, 3], 4]) == [[1], [2, 3]]
assert filter_lists([[[]]]) == [[[]]]
assert filter_lists([range(3), list(range(3))]) == [[0, 1, 2]]
a = [1]
res = filter_lists([a, 5])
assert res[0] is a
assert filter_lists([bytearray(b"a"), [b"a"]]) == [[b"a"]]
assert filter_lists([True, False, 0, 1]) == []
assert filter_lists([[0]] * 50000 + [0] * 50000) == [[0]] * 50000
assert filter_lists(["x", ["y"], "z", ["w"]]) == [["y"], ["w"]]
''')

add(22, '''from typing import List, Any


def filter_dicts(values: List[Any]) -> List[dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dicts(['a', 3.14, {'k': 5}])
    [{'k': 5}]
    >>> filter_dicts([1, 2, 3, 'abc', {}, [], {1: 2}])
    [{}, {1: 2}]
    """
''', '''
    return [x for x in values if isinstance(x, dict)]
''', '''
assert filter_dicts([]) == []
assert filter_dicts(["a", 3.14, {"k": 5}]) == [{"k": 5}]
assert filter_dicts([1, 2, 3, "abc", {}, [], {1: 2}]) == [{}, {1: 2}]
assert filter_dicts([set(), {1}, [], ()]) == []
assert filter_dicts([[("a", 1)], ("a", 1)]) == []
assert filter_dicts([{}, {}]) == [{}, {}]
assert filter_dicts([{"a": {"b": 1}}, 1]) == [{"a": {"b": 1}}]
assert filter_dicts([None, "{}", 0]) == []
assert filter_dicts([{"x": 1}, "y", {"z": 2}]) == [{"x": 1}, {"z": 2}]
d = {1: 1}
assert filter_dicts([d])[0] is d
assert filter_dicts([{i: i} for i in range(1000)] + [i for i in range(1000)]) == [{i: i} for i in range(1000)]
assert filter_dicts([True, 1.5, b""]) == []
assert filter_dicts([{}] * 100000 + [[]] * 100000) == [{}] * 100000
''')

add(22, '''from typing import List, Any


def squares_of_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers and return their squares
    in the original order. Note that in Python a boolean is also an integer (True is 1, False is 0).
    >>> squares_of_integers(['a', 3.14, 5])
    [25]
    >>> squares_of_integers([1, 2, 3, 'abc', {}, [], -4])
    [1, 4, 9, 16]
    """
''', '''
    return [x * x for x in values if isinstance(x, int)]
''', '''
assert squares_of_integers([]) == []
assert squares_of_integers(["a", 3.14, 5]) == [25]
assert squares_of_integers([1, 2, 3, "abc", {}, [], -4]) == [1, 4, 9, 16]
assert squares_of_integers([0]) == [0]
assert squares_of_integers([2.0, 3.0]) == []
assert squares_of_integers([True, False, 2]) == [1, 0, 4]
assert squares_of_integers(["3", 3]) == [9]
assert squares_of_integers([10 ** 10]) == [10 ** 20]
assert squares_of_integers([-1, -2, -3]) == [1, 4, 9]
assert squares_of_integers([None, [1], (2,), {3}, 4]) == [16]
assert squares_of_integers([2 ** 100]) == [2 ** 200]
assert squares_of_integers([7, 7.0, 7]) == [49, 49]
assert squares_of_integers(list(range(1000))) == [i * i for i in range(1000)]
assert sum(squares_of_integers(list(range(100000)) + ["x"] * 100000)) == sum(i * i for i in range(100000))
''')

# ---------------------------------------------------------------- HumanEval/25
add(25, '''from typing import List


def distinct_prime_factors(n: int) -> List[int]:
    """ Return list of distinct prime factors of given integer in the order from smallest to largest.
    Each prime factor should be listed only once, no matter how many times it divides the number.
    For 1 the list is empty.
    >>> distinct_prime_factors(8)
    [2]
    >>> distinct_prime_factors(70)
    [2, 5, 7]
    >>> distinct_prime_factors(1)
    []
    """
''', '''
    res = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        res.append(n)
    return res
''', '''
def ref(n):
    out = []
    for p in range(2, n + 1):
        if n % p == 0 and all(p % q for q in range(2, p)):
            out.append(p)
    return out
assert distinct_prime_factors(1) == []
assert distinct_prime_factors(2) == [2]
assert distinct_prime_factors(3) == [3]
assert distinct_prime_factors(4) == [2]
assert distinct_prime_factors(8) == [2]
assert distinct_prime_factors(25) == [5]
assert distinct_prime_factors(70) == [2, 5, 7]
assert distinct_prime_factors(360) == [2, 3, 5]
assert distinct_prime_factors(97) == [97]
assert distinct_prime_factors(2 * 3 * 5 * 7 * 11 * 13) == [2, 3, 5, 7, 11, 13]
assert distinct_prime_factors(2 ** 40) == [2]
assert distinct_prime_factors(999999937) == [999999937]
assert distinct_prime_factors(999999937 * 2) == [2, 999999937]
assert distinct_prime_factors(1000003 * 1000033) == [1000003, 1000033]
assert distinct_prime_factors(10 ** 12) == [2, 5]
assert distinct_prime_factors(2 ** 31 - 1) == [2 ** 31 - 1]
for n in range(1, 400):
    assert distinct_prime_factors(n) == ref(n), n
''')

add(25, '''def count_prime_factors(n: int) -> int:
    """ Return the number of prime factors of given integer, counted with multiplicity.
    Input number is equal to the product of all its prime factors. For 1 the answer is 0.
    >>> count_prime_factors(1)
    0
    >>> count_prime_factors(8)
    3
    >>> count_prime_factors(70)
    3
    >>> count_prime_factors(25)
    2
    """
''', '''
    cnt = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            cnt += 1
        d += 1
    if n > 1:
        cnt += 1
    return cnt
''', '''
def ref(n):
    c = 0
    for p in range(2, n + 1):
        while n % p == 0:
            n //= p
            c += 1
    return c
assert count_prime_factors(1) == 0
assert count_prime_factors(2) == 1
assert count_prime_factors(4) == 2
assert count_prime_factors(6) == 2
assert count_prime_factors(8) == 3
assert count_prime_factors(25) == 2
assert count_prime_factors(70) == 3
assert count_prime_factors(97) == 1
assert count_prime_factors(2 ** 30) == 30
assert count_prime_factors(3 ** 19) == 19
assert count_prime_factors(2 ** 20 * 3 ** 10 * 5 ** 5) == 35
assert count_prime_factors(999999937) == 1
assert count_prime_factors(999983 * 999983) == 2
assert count_prime_factors(10 ** 12) == 24
assert count_prime_factors(1000003 * 1000033) == 2
for n in range(1, 600):
    assert count_prime_factors(n) == ref(n), n
''')

add(25, '''from typing import List, Tuple


def factorize_with_exponents(n: int) -> List[Tuple[int, int]]:
    """ Return list of (prime, exponent) pairs of the prime factorization of given integer,
    ordered by prime from smallest to largest. Input number should be equal to the product
    of prime ** exponent over all pairs. For 1 the list is empty.
    >>> factorize_with_exponents(8)
    [(2, 3)]
    >>> factorize_with_exponents(70)
    [(2, 1), (5, 1), (7, 1)]
    >>> factorize_with_exponents(1)
    []
    """
''', '''
    res = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            res.append((d, e))
        d += 1
    if n > 1:
        res.append((n, 1))
    return res
''', '''
def ref(n):
    out, p = [], 2
    while n > 1:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    return out
assert factorize_with_exponents(1) == []
assert factorize_with_exponents(2) == [(2, 1)]
assert factorize_with_exponents(8) == [(2, 3)]
assert factorize_with_exponents(70) == [(2, 1), (5, 1), (7, 1)]
assert factorize_with_exponents(36) == [(2, 2), (3, 2)]
assert factorize_with_exponents(97) == [(97, 1)]
assert factorize_with_exponents(2 ** 20 * 7) == [(2, 20), (7, 1)]
assert factorize_with_exponents(999999937) == [(999999937, 1)]
assert factorize_with_exponents(999999937 * 4) == [(2, 2), (999999937, 1)]
assert factorize_with_exponents(10 ** 12) == [(2, 12), (5, 12)]
assert factorize_with_exponents(49) == [(7, 2)]
assert factorize_with_exponents(1001) == [(7, 1), (11, 1), (13, 1)]
for n in range(1, 700):
    r = factorize_with_exponents(n)
    assert r == ref(n), n
    prod = 1
    for p, e in r:
        prod *= p ** e
    assert prod == n
''')

add(25, '''def largest_prime_factor(n: int) -> int:
    """ Return the largest prime factor of given integer n, where n > 1.
    >>> largest_prime_factor(8)
    2
    >>> largest_prime_factor(70)
    7
    >>> largest_prime_factor(13195)
    29
    """
''', '''
    best = 1
    d = 2
    while d * d <= n:
        while n % d == 0:
            best = d
            n //= d
        d += 1
    if n > 1:
        best = n
    return best
''', '''
def ref(n):
    best = 0
    for p in range(2, n + 1):
        if n % p == 0 and all(p % q for q in range(2, p)):
            best = p
    return best
assert largest_prime_factor(2) == 2
assert largest_prime_factor(3) == 3
assert largest_prime_factor(4) == 2
assert largest_prime_factor(8) == 2
assert largest_prime_factor(70) == 7
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(97) == 97
assert largest_prime_factor(2 * 97) == 97
assert largest_prime_factor(600851475143) == 6857
assert largest_prime_factor(999999937) == 999999937
assert largest_prime_factor(999999937 * 2) == 999999937
assert largest_prime_factor(2 ** 40) == 2
assert largest_prime_factor(10 ** 12) == 5
assert largest_prime_factor(1000003 * 1000033) == 1000033
assert largest_prime_factor(2 ** 31 - 1) == 2 ** 31 - 1
for n in range(2, 300):
    assert largest_prime_factor(n) == ref(n), n
''')

add(25, '''def sum_of_prime_factors(n: int) -> int:
    """ Return the sum of prime factors of given integer, where each factor is added as many times
    as it appears in the factorization. For 1 the sum is 0.
    >>> sum_of_prime_factors(1)
    0
    >>> sum_of_prime_factors(8)
    6
    >>> sum_of_prime_factors(25)
    10
    >>> sum_of_prime_factors(70)
    14
    """
''', '''
    total = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            total += d
            n //= d
        d += 1
    if n > 1:
        total += n
    return total
''', '''
def ref(n):
    s, p = 0, 2
    while n > 1:
        while n % p == 0:
            s += p
            n //= p
        p += 1
    return s
assert sum_of_prime_factors(1) == 0
assert sum_of_prime_factors(2) == 2
assert sum_of_prime_factors(4) == 4
assert sum_of_prime_factors(8) == 6
assert sum_of_prime_factors(25) == 10
assert sum_of_prime_factors(70) == 14
assert sum_of_prime_factors(97) == 97
assert sum_of_prime_factors(2 ** 30) == 60
assert sum_of_prime_factors(999999937) == 999999937
assert sum_of_prime_factors(999999937 * 3) == 999999940
assert sum_of_prime_factors(10 ** 12) == 12 * 2 + 12 * 5
assert sum_of_prime_factors(30030) == 2 + 3 + 5 + 7 + 11 + 13
assert sum_of_prime_factors(1000003 * 1000033) == 1000003 + 1000033
for n in range(1, 800):
    assert sum_of_prime_factors(n) == ref(n), n
''')
