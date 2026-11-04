# parents 26-33
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------- parent 26: tri ----------------
add(26, '''def pell(n):
    """The Pell sequence is defined by the recurrence:
    pell(0) = 0
    pell(1) = 1
    pell(n) = 2 * pell(n - 1) + pell(n - 2) for n >= 2.
    You are given a non-negative integer number n, you have to return a list of the
    first n + 1 numbers of the Pell sequence.
    Examples:
    pell(0) = [0]
    pell(4) = [0, 1, 2, 5, 12]
    """
''', '''
    if n == 0:
        return [0]
    result = [0, 1]
    for i in range(2, n + 1):
        result.append(2 * result[-1] + result[-2])
    return result
''', '''
assert pell(0) == [0]
assert pell(1) == [0, 1]
assert pell(2) == [0, 1, 2]
assert pell(4) == [0, 1, 2, 5, 12]
assert pell(8) == [0, 1, 2, 5, 12, 29, 70, 169, 408]
r = pell(5000)
assert len(r) == 5001
assert r[-1] == 2 * r[-2] + r[-3]
assert r[100] == 2 * r[99] + r[98]
''')

add(26, '''def padovan(n):
    """The Padovan sequence is defined by the recurrence:
    p(0) = p(1) = p(2) = 1
    p(n) = p(n - 2) + p(n - 3) for n >= 3.
    You are given a non-negative integer number n, you have to return a list of the
    first n + 1 numbers of the Padovan sequence.
    Examples:
    padovan(0) = [1]
    padovan(2) = [1, 1, 1]
    padovan(7) = [1, 1, 1, 2, 2, 3, 4, 5]
    """
''', '''
    result = [1, 1, 1]
    for i in range(3, n + 1):
        result.append(result[i - 2] + result[i - 3])
    return result[:n + 1]
''', '''
assert padovan(0) == [1]
assert padovan(1) == [1, 1]
assert padovan(2) == [1, 1, 1]
assert padovan(3) == [1, 1, 1, 2]
assert padovan(7) == [1, 1, 1, 2, 2, 3, 4, 5]
assert padovan(12) == [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21]
r = padovan(10000)
assert len(r) == 10001 and r[-1] == r[-3] + r[-4]
''')

add(26, '''def tri_mod(n):
    """Tribonacci-like sequence defined by the recurrence:
    t(0) = 0
    t(1) = 1
    t(2) = 1
    t(n) = t(n - 1) + t(n - 2) + t(n - 3), for n >= 3.
    You are given a non-negative integer number n, you have to return a list of the
    first n + 1 numbers of this sequence, each one taken modulo 10**9 + 7.
    Examples:
    tri_mod(0) = [0]
    tri_mod(2) = [0, 1, 1]
    tri_mod(6) = [0, 1, 1, 2, 4, 7, 13]
    """
''', '''
    mod = 10 ** 9 + 7
    result = [0, 1, 1]
    for i in range(3, n + 1):
        result.append((result[-1] + result[-2] + result[-3]) % mod)
    return result[:n + 1]
''', '''
assert tri_mod(0) == [0]
assert tri_mod(1) == [0, 1]
assert tri_mod(2) == [0, 1, 1]
assert tri_mod(3) == [0, 1, 1, 2]
assert tri_mod(6) == [0, 1, 1, 2, 4, 7, 13]
r = tri_mod(10 ** 5)
assert len(r) == 10 ** 5 + 1
assert all(0 <= x < 10 ** 9 + 7 for x in r)
assert r[-1] == (r[-2] + r[-3] + r[-4]) % (10 ** 9 + 7)
a, b, c = 0, 1, 1
for _ in range(10 ** 5 - 2):
    a, b, c = b, c, a + b + c
assert r[-1] == c % (10 ** 9 + 7)
''')

add(26, '''def collatz_lengths(n):
    """Collatz sequence of a number x: if x is even the next number is x / 2, otherwise it is
    3 * x + 1; the sequence ends when it reaches 1. The length is the count of numbers in
    the sequence including x and 1.
    You are given a positive integer n, return a list with the Collatz sequence length of
    every integer from 1 to n (element at index i is the length for i + 1).
    Examples:
    collatz_lengths(1) = [1]
    collatz_lengths(6) = [1, 2, 8, 3, 6, 9]
    """
''', '''
    cache = {1: 1}
    result = []
    for start in range(1, n + 1):
        x = start
        path = []
        while x not in cache:
            path.append(x)
            x = x // 2 if x % 2 == 0 else 3 * x + 1
        length = cache[x]
        for v in reversed(path):
            length += 1
            cache[v] = length
        result.append(cache[start])
    return result
''', '''
assert collatz_lengths(1) == [1]
assert collatz_lengths(2) == [1, 2]
assert collatz_lengths(6) == [1, 2, 8, 3, 6, 9]
assert collatz_lengths(10) == [1, 2, 8, 3, 6, 9, 17, 4, 20, 7]
r = collatz_lengths(30000)
assert len(r) == 30000
assert max(r) == 308 and r.index(max(r)) + 1 == 26623 or max(r) > 300
assert r[26] == 112
def brute(x):
    c = 1
    while x != 1:
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        c += 1
    return c
for i in (1, 7, 27, 97, 871, 6171):
    assert collatz_lengths(i)[-1] == brute(i), i
''')

add(26, '''def catalan_numbers(n):
    """The Catalan numbers are defined by the recurrence:
    c(0) = 1
    c(n) = c(0) * c(n - 1) + c(1) * c(n - 2) + ... + c(n - 1) * c(0), for n >= 1.
    You are given a non-negative integer number n, you have to return a list of the first
    n + 1 Catalan numbers.
    Examples:
    catalan_numbers(0) = [1]
    catalan_numbers(5) = [1, 1, 2, 5, 14, 42]
    """
''', '''
    c = [1]
    for i in range(1, n + 1):
        c.append(c[-1] * 2 * (2 * i - 1) // (i + 1))
    return c
''', '''
assert catalan_numbers(0) == [1]
assert catalan_numbers(1) == [1, 1]
assert catalan_numbers(2) == [1, 1, 2]
assert catalan_numbers(5) == [1, 1, 2, 5, 14, 42]
assert catalan_numbers(10)[-1] == 16796
assert catalan_numbers(30)[-1] == 3814986502092304
r = catalan_numbers(40)
for i in range(1, 41):
    assert r[i] == sum(r[j] * r[i - 1 - j] for j in range(i)), i
big = catalan_numbers(2000)
assert len(big) == 2001 and big[-1] > 10 ** 1000
''')

# ---------------- parent 27: is_nested ----------------
add(27, '''def max_nesting_depth(string):
    \'\'\'
    Create a function that takes a string as input which contains only square brackets.
    The function should return the maximum nesting depth of a valid bracket sequence made of the
    string, or -1 if the brackets are not balanced. An empty string has depth 0.

    max_nesting_depth('[[]]') ➞ 2
    max_nesting_depth('[][]') ➞ 1
    max_nesting_depth('[[]') ➞ -1
    max_nesting_depth('][') ➞ -1
    max_nesting_depth('') ➞ 0
    \'\'\'
''', '''
    depth = best = 0
    for ch in string:
        if ch == "[":
            depth += 1
            best = max(best, depth)
        else:
            depth -= 1
            if depth < 0:
                return -1
    return best if depth == 0 else -1
''', '''
assert max_nesting_depth("") == 0
assert max_nesting_depth("[]") == 1
assert max_nesting_depth("[[]]") == 2
assert max_nesting_depth("[][]") == 1
assert max_nesting_depth("[[]") == -1
assert max_nesting_depth("[]]") == -1
assert max_nesting_depth("][") == -1
assert max_nesting_depth("[") == -1
assert max_nesting_depth("]") == -1
assert max_nesting_depth("[[][[]]]") == 3
assert max_nesting_depth("[" * 100000 + "]" * 100000) == 100000
assert max_nesting_depth("[]" * 100000) == 1
assert max_nesting_depth("[" * 100000 + "]" * 99999) == -1
''')

add(27, '''def count_valid_pairs(string):
    \'\'\'
    Create a function that takes a string as input which contains only square brackets.
    The function should return the maximum number of matched pairs '[]' that can be formed
    by choosing a subsequence of the brackets (ignoring unmatched brackets).

    count_valid_pairs('[[]]') ➞ 2
    count_valid_pairs('[]]]]]]][[[[[]') ➞ 2
    count_valid_pairs('][') ➞ 0
    count_valid_pairs('') ➞ 0
    \'\'\'
''', '''
    open_count = 0
    pairs = 0
    for ch in string:
        if ch == "[":
            open_count += 1
        elif open_count > 0:
            open_count -= 1
            pairs += 1
    return pairs
''', '''
assert count_valid_pairs("") == 0
assert count_valid_pairs("[") == 0
assert count_valid_pairs("]") == 0
assert count_valid_pairs("[]") == 1
assert count_valid_pairs("][") == 0
assert count_valid_pairs("[[]]") == 2
assert count_valid_pairs("[]]]]]]][[[[[]") == 2
assert count_valid_pairs("[[[]") == 1
assert count_valid_pairs("[][][]") == 3
assert count_valid_pairs("]]]]][[[[[") == 0
assert count_valid_pairs("[]" * 100000) == 100000
assert count_valid_pairs("[" * 100000 + "]" * 100000) == 100000
assert count_valid_pairs("]" * 100000 + "[" * 100000) == 0
''')

add(27, '''def min_bracket_additions(string):
    \'\'\'
    Create a function that takes a string as input which contains only square brackets.
    The function should return the minimum number of brackets (of any kind, inserted at any
    position) that must be added to make the string a valid balanced bracket sequence.

    min_bracket_additions('[[]]') ➞ 0
    min_bracket_additions('[[') ➞ 2
    min_bracket_additions('][') ➞ 2
    min_bracket_additions('') ➞ 0
    \'\'\'
''', '''
    need_open = 0
    balance = 0
    for ch in string:
        if ch == "[":
            balance += 1
        elif balance > 0:
            balance -= 1
        else:
            need_open += 1
    return need_open + balance
''', '''
assert min_bracket_additions("") == 0
assert min_bracket_additions("[]") == 0
assert min_bracket_additions("[[]]") == 0
assert min_bracket_additions("[[") == 2
assert min_bracket_additions("]]") == 2
assert min_bracket_additions("][") == 2
assert min_bracket_additions("[]]") == 1
assert min_bracket_additions("[[]") == 1
assert min_bracket_additions("]]][[[") == 6
assert min_bracket_additions("[" * 100000) == 100000
assert min_bracket_additions("]" * 100000 + "[" * 100000) == 200000
assert min_bracket_additions("[]" * 100000) == 0
''')

add(27, '''def longest_valid_brackets(string):
    \'\'\'
    Create a function that takes a string as input which contains only square brackets.
    The function should return the length of the longest contiguous substring that is a valid
    balanced bracket sequence.

    longest_valid_brackets('[[]]') ➞ 4
    longest_valid_brackets('[]][[]') ➞ 2
    longest_valid_brackets('[[]') ➞ 2
    longest_valid_brackets('') ➞ 0
    \'\'\'
''', '''
    stack = [-1]
    best = 0
    for i, ch in enumerate(string):
        if ch == "[":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                best = max(best, i - stack[-1])
    return best
''', '''
assert longest_valid_brackets("") == 0
assert longest_valid_brackets("[") == 0
assert longest_valid_brackets("]") == 0
assert longest_valid_brackets("[]") == 2
assert longest_valid_brackets("[[]]") == 4
assert longest_valid_brackets("[]][[]") == 2
assert longest_valid_brackets("[[]") == 2
assert longest_valid_brackets("[]]") == 2
assert longest_valid_brackets("[][]") == 4
assert longest_valid_brackets("[]][[][]") == 4
assert longest_valid_brackets("]" * 1000 + "[" * 1000) == 0
assert longest_valid_brackets("][" * 1000) == 1998
assert longest_valid_brackets("[" * 100000 + "]" * 100000) == 200000
assert longest_valid_brackets("[]" * 100000) == 200000
assert longest_valid_brackets("[" * 100000) == 0
import random
random.seed(21)
def brute(s):
    best = 0
    for i in range(len(s)):
        bal = 0
        for j in range(i, len(s)):
            bal += 1 if s[j] == "[" else -1
            if bal < 0:
                break
            if bal == 0:
                best = max(best, j - i + 1)
    return best
for _ in range(300):
    s = "".join(random.choice("[]") for _ in range(random.randint(0, 14)))
    assert longest_valid_brackets(s) == brute(s), s
''')

add(27, '''def is_valid_mixed_brackets(string):
    \'\'\'
    Create a function that takes a string as input which contains only the characters
    '(', ')', '[', ']', '{' and '}'. The function should return True if and only if the brackets
    are balanced and correctly nested (every closing bracket matches the most recent unmatched
    opening bracket of the same kind). The empty string is valid.

    is_valid_mixed_brackets('([]{})') ➞ True
    is_valid_mixed_brackets('([)]') ➞ False
    is_valid_mixed_brackets('((') ➞ False
    is_valid_mixed_brackets('') ➞ True
    \'\'\'
''', '''
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in string:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack
''', '''
assert is_valid_mixed_brackets("") is True
assert is_valid_mixed_brackets("()") is True
assert is_valid_mixed_brackets("([]{})") is True
assert is_valid_mixed_brackets("([)]") is False
assert is_valid_mixed_brackets("((") is False
assert is_valid_mixed_brackets("))") is False
assert is_valid_mixed_brackets(")(") is False
assert is_valid_mixed_brackets("{[()]}") is True
assert is_valid_mixed_brackets("{[(])}") is False
assert is_valid_mixed_brackets("(]") is False
assert is_valid_mixed_brackets("[") is False
assert is_valid_mixed_brackets("}") is False
assert is_valid_mixed_brackets("(" * 100000 + ")" * 100000) is True
assert is_valid_mixed_brackets("(" * 100000 + "]" + ")" * 99999) is False
assert is_valid_mixed_brackets("()[]{}" * 50000) is True
assert is_valid_mixed_brackets("(" * 100001 + ")" * 100000) is False
''')

# ---------------- parent 28: check_if_last_char_is_a_letter ----------------
add(28, '''def check_if_first_char_is_a_letter(txt):
    \'\'\'
    Create a function that returns True if the first character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_first_char_is_a_letter("apple pie") ➞ False
    check_if_first_char_is_a_letter("a pie") ➞ True
    check_if_first_char_is_a_letter(" a pie") ➞ False
    check_if_first_char_is_a_letter("") ➞ False
    \'\'\'
''', '''
    if len(txt) == 0:
        return False
    if len(txt) == 1:
        return txt.isalpha()
    return txt[0].isalpha() and txt[1] == " "
''', '''
assert check_if_first_char_is_a_letter("") is False
assert check_if_first_char_is_a_letter("a") is True
assert check_if_first_char_is_a_letter("Z") is True
assert check_if_first_char_is_a_letter("1") is False
assert check_if_first_char_is_a_letter(" ") is False
assert check_if_first_char_is_a_letter("apple pie") is False
assert check_if_first_char_is_a_letter("a pie") is True
assert check_if_first_char_is_a_letter(" a pie") is False
assert check_if_first_char_is_a_letter("a") is True
assert check_if_first_char_is_a_letter("a ") is True
assert check_if_first_char_is_a_letter("1 a") is False
assert check_if_first_char_is_a_letter("a1") is False
assert check_if_first_char_is_a_letter("a\\tb") is False
assert check_if_first_char_is_a_letter("a" + " b" * 100000) is True
assert check_if_first_char_is_a_letter("ab" + " b" * 100000) is False
''')

add(28, '''def count_single_letter_words(txt):
    \'\'\'
    Create a function that returns the number of words in the given string that consist of exactly
    one alphabetical character.
    Note: "word" is a group of characters separated by one or more spaces.

    Examples:
    count_single_letter_words("a b cc d1") ➞ 2
    count_single_letter_words("") ➞ 0
    count_single_letter_words("  x  ") ➞ 1
    count_single_letter_words("1 2 3") ➞ 0
    \'\'\'
''', '''
    return sum(1 for w in txt.split(" ") if len(w) == 1 and w.isalpha())
''', '''
assert count_single_letter_words("") == 0
assert count_single_letter_words(" ") == 0
assert count_single_letter_words("a") == 1
assert count_single_letter_words("a b cc d1") == 2
assert count_single_letter_words("  x  ") == 1
assert count_single_letter_words("1 2 3") == 0
assert count_single_letter_words("a a a a") == 4
assert count_single_letter_words("A B") == 2
assert count_single_letter_words("ab c") == 1
assert count_single_letter_words("! ? a") == 1
assert count_single_letter_words("a " * 100000) == 100000
assert count_single_letter_words("a\\tb") == 0
''')

add(28, '''def last_word_length(txt):
    \'\'\'
    Create a function that returns the length of the last word in a string.
    A "word" is a maximal group of non-space characters (separated by spaces).
    Trailing spaces are ignored. If the string has no words, return 0.

    Examples:
    last_word_length("hello world") ➞ 5
    last_word_length("fly me   to   the moon  ") ➞ 4
    last_word_length("") ➞ 0
    last_word_length("   ") ➞ 0
    \'\'\'
''', '''
    words = txt.split(" ")
    for w in reversed(words):
        if w:
            return len(w)
    return 0
''', '''
assert last_word_length("") == 0
assert last_word_length(" ") == 0
assert last_word_length("   ") == 0
assert last_word_length("a") == 1
assert last_word_length("hello world") == 5
assert last_word_length("fly me   to   the moon  ") == 4
assert last_word_length("  a") == 1
assert last_word_length("a  ") == 1
assert last_word_length("ab cde ") == 3
assert last_word_length("x" * 100000) == 100000
assert last_word_length("a " * 100000 + "bb  ") == 2
assert last_word_length(" " * 100000) == 0
''')

add(28, '''def last_char_is_unique_letter(txt):
    \'\'\'
    Create a function that returns True if the last non-space character of a given string is an
    alphabetical character that does not appear anywhere else in the string (the comparison
    is case-insensitive), and False otherwise. Trailing spaces are ignored.

    Examples:
    last_char_is_unique_letter("apple pie") ➞ False
    last_char_is_unique_letter("abc") ➞ True
    last_char_is_unique_letter("abC c") ➞ False
    last_char_is_unique_letter("ab1  ") ➞ False
    last_char_is_unique_letter("") ➞ False
    \'\'\'
''', '''
    stripped = txt.rstrip(" ")
    if not stripped:
        return False
    last = stripped[-1]
    if not last.isalpha():
        return False
    return stripped.lower().count(last.lower()) == 1
''', '''
assert last_char_is_unique_letter("") is False
assert last_char_is_unique_letter("   ") is False
assert last_char_is_unique_letter("a") is True
assert last_char_is_unique_letter("a   ") is True
assert last_char_is_unique_letter("apple pie") is False
assert last_char_is_unique_letter("abc") is True
assert last_char_is_unique_letter("abC c") is False
assert last_char_is_unique_letter("ab1  ") is False
assert last_char_is_unique_letter("aA") is False
assert last_char_is_unique_letter("a b z") is True
assert last_char_is_unique_letter("1") is False
assert last_char_is_unique_letter("a" * 100000 + "b") is True
assert last_char_is_unique_letter("a" * 100000) is False
''')

add(28, '''def ends_with_standalone_digit(txt):
    \'\'\'
    Create a function that returns True if the last character of a given string is a digit
    ('0'-'9') and is a separate word (it is preceded by a space or it is the only character),
    and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    ends_with_standalone_digit("version 2") ➞ True
    ends_with_standalone_digit("version2") ➞ False
    ends_with_standalone_digit("5") ➞ True
    ends_with_standalone_digit("version 2 ") ➞ False
    ends_with_standalone_digit("") ➞ False
    \'\'\'
''', '''
    if not txt:
        return False
    if len(txt) == 1:
        return txt in "0123456789"
    return txt[-1] in "0123456789" and txt[-2] == " "
''', '''
assert ends_with_standalone_digit("") is False
assert ends_with_standalone_digit("5") is True
assert ends_with_standalone_digit("a") is False
assert ends_with_standalone_digit(" ") is False
assert ends_with_standalone_digit("version 2") is True
assert ends_with_standalone_digit("version2") is False
assert ends_with_standalone_digit("version 2 ") is False
assert ends_with_standalone_digit("version 22") is False
assert ends_with_standalone_digit(" 9") is True
assert ends_with_standalone_digit("a b") is False
assert ends_with_standalone_digit("\\u0663") is False
assert ends_with_standalone_digit("x \\u0663") is False
assert ends_with_standalone_digit("\\u00b2") is False
assert ends_with_standalone_digit("a " * 100000 + "7") is True
''')

# ---------------- parent 29: special_factorial ----------------
add(29, '''def superfactorial_ratio(n):
    """The ratio of consecutive Brazilian factorials is defined as:
    ratio(n) = brazilian_factorial(n) / brazilian_factorial(n - 1) for n > 1
    where brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    and ratio(1) = 1. In other words ratio(n) = n!.
    The function receives an integer n >= 1 and should return ratio(n) as an integer.
    For example:
    >>> superfactorial_ratio(4)
    24
    >>> superfactorial_ratio(1)
    1
    """
''', '''
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
''', '''
assert superfactorial_ratio(1) == 1
assert superfactorial_ratio(2) == 2
assert superfactorial_ratio(3) == 6
assert superfactorial_ratio(4) == 24
assert superfactorial_ratio(10) == 3628800
assert superfactorial_ratio(20) == 2432902008176640000
import math
assert superfactorial_ratio(500) == math.factorial(500)
assert superfactorial_ratio(3000) == math.factorial(3000)
''')

add(29, '''def double_factorial(n):
    """The double factorial of n is defined as the product of all integers from 1 to n that
    have the same parity as n:
    double_factorial(n) = n * (n - 2) * (n - 4) * ... down to 1 or 2
    The double factorial of 0 is 1 and of -1 is 1. The function receives an integer n >= 0
    and should return its double factorial.
    For example:
    >>> double_factorial(5)
    15
    >>> double_factorial(8)
    384
    >>> double_factorial(0)
    1
    """
''', '''
    result = 1
    while n > 1:
        result *= n
        n -= 2
    return result
''', '''
assert double_factorial(0) == 1
assert double_factorial(1) == 1
assert double_factorial(2) == 2
assert double_factorial(3) == 3
assert double_factorial(4) == 8
assert double_factorial(5) == 15
assert double_factorial(8) == 384
assert double_factorial(9) == 945
assert double_factorial(20) == 3715891200
assert double_factorial(21) == 13749310575
import math
assert double_factorial(2000) * double_factorial(1999) == math.factorial(2000)
assert double_factorial(10001) > 10 ** 10000
''')

add(29, '''def factorial_digit_sum(n):
    """Return the sum of the decimal digits of n! (the factorial of n), where n >= 0
    and n can be as large as 1000.
    For example:
    >>> factorial_digit_sum(5)
    3
    >>> factorial_digit_sum(10)
    27
    >>> factorial_digit_sum(0)
    1
    """
''', '''
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return sum(int(c) for c in str(fact))
''', '''
assert factorial_digit_sum(0) == 1
assert factorial_digit_sum(1) == 1
assert factorial_digit_sum(5) == 3
assert factorial_digit_sum(10) == 27
assert factorial_digit_sum(20) == 54
assert factorial_digit_sum(100) == 648
assert factorial_digit_sum(1000) == 10539
import math
assert factorial_digit_sum(500) == sum(map(int, str(math.factorial(500))))
''')

add(29, '''def trailing_zeros_of_special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0.
    Return the number of trailing zeros in the decimal representation of the Brazilian
    factorial of n. n can be as large as 10**5, so do not compute the factorial itself.
    For example:
    >>> trailing_zeros_of_special_factorial(5)
    1
    >>> trailing_zeros_of_special_factorial(1)
    0
    """
''', '''
    def zeros(k):
        c = 0
        while k:
            k //= 5
            c += k
        return c

    def twos(k):
        c = 0
        while k:
            k //= 2
            c += k
        return c

    five = two = 0
    for i in range(1, n + 1):
        five += zeros(i)
        two += twos(i)
    return min(five, two)
''', '''
assert trailing_zeros_of_special_factorial(1) == 0
assert trailing_zeros_of_special_factorial(4) == 0
assert trailing_zeros_of_special_factorial(5) == 1
import math
def brute(n):
    f = 1
    for i in range(1, n + 1):
        f *= math.factorial(i)
    s = str(f)
    return len(s) - len(s.rstrip("0"))
for n in range(1, 60):
    assert trailing_zeros_of_special_factorial(n) == brute(n), n
r = trailing_zeros_of_special_factorial(10 ** 5)
assert r > 0 and isinstance(r, int)
''')

add(29, '''def special_factorial_mod(n, m):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0.
    Return the Brazilian factorial of n modulo m, where m >= 1.
    n can be as large as 10**5, so keep the numbers small.
    For example:
    >>> special_factorial_mod(4, 1000)
    288
    >>> special_factorial_mod(4, 100)
    88
    >>> special_factorial_mod(10, 1)
    0
    """
''', '''
    fact = 1 % m
    ans = 1 % m
    for i in range(2, n + 1):
        fact = fact * i % m
        ans = ans * fact % m
    return ans
''', '''
assert special_factorial_mod(1, 1) == 0
assert special_factorial_mod(1, 2) == 1
assert special_factorial_mod(4, 1000) == 288
assert special_factorial_mod(4, 100) == 88
assert special_factorial_mod(10, 1) == 0
assert special_factorial_mod(3, 7) == 12 % 7
import math
def brute(n, m):
    f = 1
    for i in range(1, n + 1):
        f *= math.factorial(i)
    return f % m
for n in range(1, 25):
    for m in (1, 2, 7, 10, 1000, 10 ** 9 + 7):
        assert special_factorial_mod(n, m) == brute(n, m), (n, m)
assert special_factorial_mod(10 ** 5, 2) == 0
''')

# ---------------- parent 30: file_name_check ----------------
add(30, '''def image_name_check(file_name):
    """Create a function which takes a string representing an image's file name, and returns
    'Yes' if the file name is valid, and returns 'No' otherwise.
    A file name is considered to be valid if and only if all the following conditions
    are met:
    - The file name contains exactly one dot '.'
    - The substring before the dot is not empty, and consists only of latin letters
    ('a'-'z' and 'A'-'Z'), digits ('0'-'9') and underscores '_'. It has at most 8 characters.
    - The substring after the dot should be one of these: ['png', 'jpg', 'gif'] (lower case)
    Examples:
    image_name_check("photo_1.png") # => 'Yes'
    image_name_check("photo.PNG") # => 'No'
    image_name_check("verylongname.png") # => 'No'
    """
''', '''
    if file_name.count(".") != 1:
        return "No"
    name, ext = file_name.split(".")
    if not 1 <= len(name) <= 8 or ext not in ("png", "jpg", "gif"):
        return "No"
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    return "Yes" if all(c in allowed for c in name) else "No"
''', '''
assert image_name_check("photo_1.png") == "Yes"
assert image_name_check("a.gif") == "Yes"
assert image_name_check("12345678.jpg") == "Yes"
assert image_name_check("123456789.jpg") == "No"
assert image_name_check("photo.PNG") == "No"
assert image_name_check("verylongname.png") == "No"
assert image_name_check(".png") == "No"
assert image_name_check("photo.") == "No"
assert image_name_check("") == "No"
assert image_name_check(".") == "No"
assert image_name_check("photo") == "No"
assert image_name_check("photopng") == "No"
assert image_name_check("a.b.png") == "No"
assert image_name_check("a..png") == "No"
assert image_name_check("pho to.png") == "No"
assert image_name_check("pho-to.png") == "No"
assert image_name_check("photo.pngx") == "No"
assert image_name_check("photo.pn") == "No"
assert image_name_check("photo.png ") == "No"
assert image_name_check("\\u00e9a.png") == "No"
assert image_name_check("a\\u0663.png") == "No"
assert image_name_check("_.gif") == "Yes"
assert image_name_check("a" * 100000 + ".png") == "No"
assert image_name_check("a" * 100000) == "No"
''')

add(30, '''def password_check(password):
    """Create a function which takes a string representing a password, and returns
    'Strong' if the password is strong, and returns 'Weak' otherwise.
    A password is strong if and only if all the following conditions are met:
    - It has at least 8 characters.
    - It contains at least one lower case letter ('a'-'z'), one upper case letter ('A'-'Z')
    and one digit ('0'-'9').
    - It does not contain any space character.
    - It does not contain the same character three or more times in a row.
    Examples:
    password_check("Abcdef12") # => 'Strong'
    password_check("abcdef12") # => 'Weak'
    password_check("Abbb1234") # => 'Weak'
    """
''', '''
    if len(password) < 8 or " " in password:
        return "Weak"
    if not any("a" <= c <= "z" for c in password):
        return "Weak"
    if not any("A" <= c <= "Z" for c in password):
        return "Weak"
    if not any("0" <= c <= "9" for c in password):
        return "Weak"
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return "Weak"
    return "Strong"
''', '''
assert password_check("Abcdef12") == "Strong"
assert password_check("abcdef12") == "Weak"
assert password_check("ABCDEF12") == "Weak"
assert password_check("Abcdefgh") == "Weak"
assert password_check("Abcde12") == "Weak"
assert password_check("Abbb1234") == "Weak"
assert password_check("Aaa12345") == "Strong"
assert password_check("Aa112345") == "Strong"
assert password_check("Aa1 2345") == "Weak"
assert password_check("") == "Weak"
assert password_check("Aa1!Aa1!") == "Strong"
assert password_check("Aa1\\tAa1!") == "Strong"
assert password_check("Aa1\\u00e9\\u00e9\\u00e9Aa") == "Weak"
assert password_check("\\u00e9\\u00e9\\u00e9a1A") == "Weak"
assert password_check("Ab1\\u0663cdef") == "Strong"
assert password_check("Ab\\u0663\\u0663cdef") == "Weak"
assert password_check("aA1" * 100000) == "Strong"
assert password_check("aA1" * 100000 + "zzz") == "Weak"
assert password_check("1111111A") == "Weak"
''')

add(30, '''def extension_check(file_name):
    """Create a function which takes a string representing a file name, and returns the
    extension in lower case when the file name is valid, or the string 'invalid' otherwise.
    A file name is valid if and only if all the following conditions are met:
    - It contains at least one dot '.'
    - The part before the LAST dot is not empty and does not start or end with a dot or a space.
    - The part after the LAST dot (the extension) is not empty, has at most 5 characters and
    consists only of latin letters and digits.
    Examples:
    extension_check("archive.tar.GZ") # => 'gz'
    extension_check("README") # => 'invalid'
    extension_check(".gitignore") # => 'invalid'
    """
''', '''
    if "." not in file_name:
        return "invalid"
    name, ext = file_name.rsplit(".", 1)
    if not name or name[0] in ". " or name[-1] in ". ":
        return "invalid"
    if not 1 <= len(ext) <= 5:
        return "invalid"
    if not all(c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for c in ext):
        return "invalid"
    return ext.lower()
''', '''
assert extension_check("archive.tar.GZ") == "gz"
assert extension_check("a.b") == "b"
assert extension_check("file.TXT") == "txt"
assert extension_check("file.mp4") == "mp4"
assert extension_check("file.abcde") == "abcde"
assert extension_check("file.abcdef") == "invalid"
assert extension_check("README") == "invalid"
assert extension_check("") == "invalid"
assert extension_check(".gitignore") == "invalid"
assert extension_check("file.") == "invalid"
assert extension_check(".") == "invalid"
assert extension_check("..") == "invalid"
assert extension_check("a..b") == "invalid"
assert extension_check("a .b") == "invalid"
assert extension_check(" a.b") == "invalid"
assert extension_check("a b.c") == "c"
assert extension_check("file.t_t") == "invalid"
assert extension_check("file.t t") == "invalid"
assert extension_check("file.\\u00e9") == "invalid"
assert extension_check("x." + "a" * 100000) == "invalid"
assert extension_check("a" * 100000 + ".txt") == "txt"
''')

add(30, '''def valid_identifier_name(name):
    """Create a function which takes a string and returns 'Yes' if it is a valid variable
    identifier, and 'No' otherwise. A valid identifier satisfies all these conditions:
    - It is not empty and starts with a latin letter ('a'-'z', 'A'-'Z') or an underscore.
    - The other characters are latin letters, digits ('0'-'9') or underscores.
    - It is not one of the reserved words: 'if', 'else', 'for', 'while', 'def', 'class'.
    - It contains at most 3 digits.
    Examples:
    valid_identifier_name("my_var1") # => 'Yes'
    valid_identifier_name("1var") # => 'No'
    valid_identifier_name("class") # => 'No'
    """
''', '''
    if not name or name in ("if", "else", "for", "while", "def", "class"):
        return "No"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    digits = "0123456789"
    if name[0] not in letters:
        return "No"
    if any(c not in letters and c not in digits for c in name):
        return "No"
    return "Yes" if sum(1 for c in name if c in digits) <= 3 else "No"
''', '''
assert valid_identifier_name("my_var1") == "Yes"
assert valid_identifier_name("_") == "Yes"
assert valid_identifier_name("a") == "Yes"
assert valid_identifier_name("_1") == "Yes"
assert valid_identifier_name("a123") == "Yes"
assert valid_identifier_name("a1234") == "No"
assert valid_identifier_name("a1b2c3") == "Yes"
assert valid_identifier_name("a1b2c3d4") == "No"
assert valid_identifier_name("1var") == "No"
assert valid_identifier_name("class") == "No"
assert valid_identifier_name("Class") == "Yes"
assert valid_identifier_name("classes") == "Yes"
assert valid_identifier_name("if") == "No"
assert valid_identifier_name("while") == "No"
assert valid_identifier_name("") == "No"
assert valid_identifier_name("a-b") == "No"
assert valid_identifier_name("a b") == "No"
assert valid_identifier_name("a.b") == "No"
assert valid_identifier_name("\\u00e9a") == "No"
assert valid_identifier_name("a\\u0663") == "No"
assert valid_identifier_name("a" * 100000) == "Yes"
assert valid_identifier_name("_" * 100000 + "1") == "Yes"
''')

add(30, '''def url_check(url):
    """Create a function which takes a string representing a simple URL, and returns 'Yes' if
    the URL is valid, and returns 'No' otherwise. A URL is valid if and only if:
    - It starts with 'http://' or 'https://'.
    - The host (the part after the scheme up to the first '/' or the end) is not empty,
    consists only of lower case letters, digits, '-' and '.', does not start or end with '-' or '.',
    and contains at least one '.'.
    - The rest of the URL (path), if any, starts with '/' and contains no spaces.
    Examples:
    url_check("https://example.com/path") # => 'Yes'
    url_check("ftp://example.com") # => 'No'
    url_check("http://localhost") # => 'No'
    """
''', '''
    if url.startswith("https://"):
        rest = url[8:]
    elif url.startswith("http://"):
        rest = url[7:]
    else:
        return "No"
    slash = rest.find("/")
    host, path = (rest, "") if slash == -1 else (rest[:slash], rest[slash:])
    if not host or "." not in host or host[0] in "-." or host[-1] in "-.":
        return "No"
    if any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-." for c in host):
        return "No"
    if " " in path:
        return "No"
    return "Yes"
''', '''
assert url_check("https://example.com/path") == "Yes"
assert url_check("http://example.com") == "Yes"
assert url_check("http://a.b") == "Yes"
assert url_check("https://my-site.co.uk/a/b?c=d") == "Yes"
assert url_check("https://example.com/") == "Yes"
assert url_check("ftp://example.com") == "No"
assert url_check("http://localhost") == "No"
assert url_check("http://") == "No"
assert url_check("https://") == "No"
assert url_check("") == "No"
assert url_check("example.com") == "No"
assert url_check("http:/example.com") == "No"
assert url_check("http://.example.com") == "No"
assert url_check("http://example.com.") == "No"
assert url_check("http://-example.com") == "No"
assert url_check("http://example-.com/x") == "Yes"
assert url_check("http://example.com-") == "No"
assert url_check("http://Example.com") == "No"
assert url_check("http://exa mple.com") == "No"
assert url_check("http://example.com/a b") == "No"
assert url_check("http:///path.com") == "No"
assert url_check("HTTP://example.com") == "No"
assert url_check("http://exam_ple.com") == "No"
assert url_check("http://example.com/" + "a" * 100000) == "Yes"
assert url_check("http://" + "a." * 50000 + "com") == "Yes"
''')

# ---------------- parent 31: order_by_points ----------------
add(31, '''def order_by_length_then_value(nums):
    """
    Write a function which sorts the given list of integers in ascending order
    according to the number of their digits (the minus sign is not counted).
    Numbers with the same number of digits are ordered by value, ascending.
    The input list must not be modified.

    For example:
    >>> order_by_length_then_value([100, 5, -20, 33, -7])
    [-7, 5, -20, 33, 100]
    >>> order_by_length_then_value([])
    []
    """
''', '''
    return sorted(nums, key=lambda x: (len(str(abs(x))), x))
''', '''
assert order_by_length_then_value([]) == []
assert order_by_length_then_value([0]) == [0]
assert order_by_length_then_value([100, 5, -20, 33, -7]) == [-7, 5, -20, 33, 100]
assert order_by_length_then_value([10, -10, 9, -9]) == [-9, 9, -10, 10]
assert order_by_length_then_value([5, 5, 5]) == [5, 5, 5]
assert order_by_length_then_value([10 ** 18, -10 ** 18, 1]) == [1, -10 ** 18, 10 ** 18]
assert order_by_length_then_value([0, -0, 1, -1]) == [-1, 0, 0, 1]
orig = [3, 1, 2]
order_by_length_then_value(orig)
assert orig == [3, 1, 2]
assert order_by_length_then_value(list(range(100000, -1, -1))) == sorted(range(100001), key=lambda x: (len(str(x)), x))
''')

add(31, '''def order_by_digit_product(nums):
    """
    Write a function which sorts the given list of non-negative integers
    in ascending order according to the product of their digits.
    Note: if there are several items with the same product of digits,
    order them based on their index in the original list.

    For example:
    >>> order_by_digit_product([23, 10, 5, 11])
    [10, 11, 5, 23]
    >>> order_by_digit_product([])
    []
    """
''', '''
    def prod(x):
        p = 1
        for c in str(x):
            p *= int(c)
        return p
    return sorted(nums, key=prod)
''', '''
assert order_by_digit_product([]) == []
assert order_by_digit_product([0]) == [0]
assert order_by_digit_product([23, 10, 5, 11]) == [10, 11, 5, 23]
assert order_by_digit_product([99, 11, 9, 1]) == [11, 1, 9, 99]
assert order_by_digit_product([20, 10, 30]) == [20, 10, 30]
assert order_by_digit_product([5, 0, 50, 7]) == [0, 50, 5, 7]
assert order_by_digit_product([111, 11, 1]) == [111, 11, 1]
assert order_by_digit_product([999999999, 1]) == [1, 999999999]
orig = [3, 1, 2]
order_by_digit_product(orig)
assert orig == [3, 1, 2]
big = list(range(100000))
r = order_by_digit_product(big)
assert len(r) == 100000 and r[0] == 0 and sorted(r) == big
''')

add(31, '''def order_by_popcount(nums):
    """
    Write a function which sorts the given list of non-negative integers
    in ascending order according to the number of 1 bits in their binary representation.
    Note: if there are several items with the same number of 1 bits,
    order them by value, ascending.

    For example:
    >>> order_by_popcount([5, 3, 7, 1, 8])
    [1, 8, 3, 5, 7]
    >>> order_by_popcount([])
    []
    """
''', '''
    return sorted(nums, key=lambda x: (bin(x).count("1"), x))
''', '''
assert order_by_popcount([]) == []
assert order_by_popcount([0]) == [0]
assert order_by_popcount([5, 3, 7, 1, 8]) == [1, 8, 3, 5, 7]
assert order_by_popcount([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 4, 8, 3, 5, 6, 7]
assert order_by_popcount([7, 7, 0]) == [0, 7, 7]
assert order_by_popcount([2 ** 100, 2 ** 100 - 1, 3]) == [2 ** 100, 3, 2 ** 100 - 1]
assert order_by_popcount(list(range(1000, -1, -1))) == sorted(range(1001), key=lambda x: (bin(x).count("1"), x))
assert order_by_popcount([1024] * 100000) == [1024] * 100000
''')

add(31, '''def order_by_last_digit(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to their last decimal digit (the digit of the absolute value).
    Note: if there are several items with the same last digit,
    order them based on their index in the original list.

    For example:
    >>> order_by_last_digit([21, 32, -11, 40])
    [40, 21, -11, 32]
    >>> order_by_last_digit([])
    []
    """
''', '''
    return sorted(nums, key=lambda x: abs(x) % 10)
''', '''
assert order_by_last_digit([]) == []
assert order_by_last_digit([0]) == [0]
assert order_by_last_digit([21, 32, -11, 40]) == [40, 21, -11, 32]
assert order_by_last_digit([-19, 9, -9]) == [-19, 9, -9]
assert order_by_last_digit([10, 20, 30]) == [10, 20, 30]
assert order_by_last_digit([-5, 15, -25]) == [-5, 15, -25]
assert order_by_last_digit([-12, 2, -2, 22]) == [-12, 2, -2, 22]
assert order_by_last_digit([-1, -10, 100]) == [-10, 100, -1]
assert order_by_last_digit([10 ** 18 + 3, 10 ** 18 + 1]) == [10 ** 18 + 1, 10 ** 18 + 3]
orig = [3, 1, 2]
order_by_last_digit(orig)
assert orig == [3, 1, 2]
assert order_by_last_digit(list(range(100000))) == sorted(range(100000), key=lambda x: x % 10)
''')

add(31, '''def order_by_vowels(words):
    """
    Write a function which sorts the given list of words in descending order according to
    the number of vowels (a, e, i, o, u, case-insensitive) they contain.
    Note: if there are several words with the same number of vowels,
    order them based on their index in the original list.

    For example:
    >>> order_by_vowels(['sky', 'Audio', 'tree', 'a'])
    ['Audio', 'tree', 'a', 'sky']
    >>> order_by_vowels([])
    []
    """
''', '''
    return sorted(words, key=lambda w: -sum(1 for c in w.lower() if c in "aeiou"))
''', '''
assert order_by_vowels([]) == []
assert order_by_vowels([""]) == [""]
assert order_by_vowels(["sky", "Audio", "tree", "a"]) == ["Audio", "tree", "a", "sky"]
assert order_by_vowels(["bcd", "fgh"]) == ["bcd", "fgh"]
assert order_by_vowels(["fgh", "bcd"]) == ["fgh", "bcd"]
assert order_by_vowels(["AEIOU", "aeiou", "x"]) == ["AEIOU", "aeiou", "x"]
assert order_by_vowels(["a", "e", "ba"]) == ["a", "e", "ba"]
assert order_by_vowels(["xay", "aeb", "a1e"]) == ["aeb", "a1e", "xay"]
assert order_by_vowels(["y", "a"]) == ["a", "y"]
assert order_by_vowels(["a" * 100000, "e" * 100001]) == ["e" * 100001, "a" * 100000]
orig = ["b", "a"]
order_by_vowels(orig)
assert orig == ["b", "a"]
''')

# ---------------- parent 32: do_algebra ----------------
add(32, '''def do_algebra_left(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and
    the second list is a list of integers. Build the algebraic expression and evaluate it
    strictly from left to right, WITHOUT operator precedence (each operation is applied to the
    running result and the next operand).

    The basic algebra operations:
    Addition ( + )
    Subtraction ( - )
    Multiplication ( * )
    Floor division ( // )
    Exponentiation ( ** )

    Example:
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = ((2 + 3) * 4) - 5 = 15

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of non-negative integers.
        Floor division never divides by zero.
    """
''', '''
    result = operand[0]
    for op, x in zip(operator, operand[1:]):
        if op == "+":
            result += x
        elif op == "-":
            result -= x
        elif op == "*":
            result *= x
        elif op == "//":
            result //= x
        else:
            result **= x
    return result
''', '''
assert do_algebra_left([], [7]) == 7
assert do_algebra_left(["+", "*", "-"], [2, 3, 4, 5]) == 15
assert do_algebra_left(["-"], [3, 5]) == -2
assert do_algebra_left(["//"], [7, 2]) == 3
assert do_algebra_left(["**"], [2, 10]) == 1024
assert do_algebra_left(["**", "**"], [2, 3, 2]) == 64
assert do_algebra_left(["-", "//"], [1, 2, 2]) == -1
assert do_algebra_left(["*", "+"], [0, 5, 1]) == 1
assert do_algebra_left(["**"], [0, 0]) == 1
assert do_algebra_left(["+", "-", "*", "//", "**"], [1, 2, 3, 4, 5, 2]) == (((((1 + 2) - 3) * 4) // 5) ** 2)
assert do_algebra_left(["+"] * 99999, [1] * 100000) == 100000
assert do_algebra_left(["*"] * 99, [2] * 100) == 2 ** 100
assert do_algebra_left(["**", "**"], [10, 100, 2]) == 10 ** 200
''')

add(32, '''def do_algebra_safe(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and
    the second list is a list of integers. Build the algebraic expression and return its
    evaluation using the usual Python operator precedence, but if the expression would divide by
    zero (floor division by 0, either directly or because a sub-expression evaluates to 0),
    return None instead of raising an exception.

    The basic algebra operations:
    Addition ( + )
    Subtraction ( - )
    Multiplication ( * )
    Floor division ( // )
    Exponentiation ( ** )

    Example:
    operator = ['+', '//']
    operand = [2, 6, 3]
    result = 2 + 6 // 3 = 4
    operator = ['//']
    operand = [5, 0]
    result = None

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of non-negative integers (exponents are small, at most 50).
    """
''', '''
    expr = str(operand[0])
    for op, x in zip(operator, operand[1:]):
        expr += " " + op + " " + str(x)
    try:
        return eval(expr)
    except ZeroDivisionError:
        return None
''', '''
assert do_algebra_safe([], [5]) == 5
assert do_algebra_safe(["+", "//"], [2, 6, 3]) == 4
assert do_algebra_safe(["//"], [5, 0]) is None
assert do_algebra_safe(["//"], [0, 5]) == 0
assert do_algebra_safe(["-", "//"], [5, 3, 5]) == 5
assert do_algebra_safe(["//", "-"], [5, 2, 2]) == 0
assert do_algebra_safe(["+", "//", "*"], [1, 2, 0, 5]) is None
assert do_algebra_safe(["*", "//"], [0, 3, 1]) == 0
assert do_algebra_safe(["**", "+"], [2, 3, 1]) == 9
assert do_algebra_safe(["+", "**"], [1, 2, 3]) == 9
assert do_algebra_safe(["**", "**"], [2, 3, 2]) == 512
assert do_algebra_safe(["**"], [0, 0]) == 1
assert do_algebra_safe(["+", "*"] * 4, [1, 2, 3, 4, 5, 6, 7, 8, 9][:9]) == 1 + 2 * 3 + 4 * 5 + 6 * 7 + 8 * 9
assert do_algebra_safe(["//", "//"], [100, 5, 0]) is None
assert do_algebra_safe(["-", "-"], [10, 3, 2]) == 5
assert do_algebra_safe(["*"] * 999, [1] * 1000) == 1
''')

add(32, '''def do_algebra_rpn(tokens):
    """
    Given a list of tokens that represents an arithmetic expression in Reverse Polish Notation,
    evaluate it and return the integer result. Valid tokens are non-negative integers given as
    strings and the operators '+', '-', '*', '//'. Division is floor division (like Python's //)
    and it never divides by zero. The expression is always valid and not empty.

    Example:
    tokens = ['2', '3', '+', '4', '*']
    result = (2 + 3) * 4 = 20
    tokens = ['7', '2', '//']
    result = 3

    Note:
        Intermediate results can be negative.
    """
''', '''
    stack = []
    for t in tokens:
        if t in ("+", "-", "*", "//"):
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(a // b)
        else:
            stack.append(int(t))
    return stack[0]
''', '''
assert do_algebra_rpn(["5"]) == 5
assert do_algebra_rpn(["0"]) == 0
assert do_algebra_rpn(["2", "3", "+", "4", "*"]) == 20
assert do_algebra_rpn(["7", "2", "//"]) == 3
assert do_algebra_rpn(["3", "5", "-"]) == -2
assert do_algebra_rpn(["3", "5", "-", "2", "//"]) == -1
assert do_algebra_rpn(["1", "3", "-", "4", "//"]) == -1
assert do_algebra_rpn(["10", "6", "9", "3", "+", "-", "11", "*", "//", "17", "+", "5", "+"]) == 21
assert do_algebra_rpn(["4", "13", "5", "//", "+"]) == 6
assert do_algebra_rpn(["0", "7", "-", "2", "//"]) == -4
assert do_algebra_rpn(["1000000000", "1000000000", "*"]) == 10 ** 18
assert do_algebra_rpn(["1"] + ["1", "+"] * 99999) == 100000
assert do_algebra_rpn(["1"] * 100000 + ["+"] * 99999) == 100000
assert do_algebra_rpn(["12345678901234567890", "1", "*"]) == 12345678901234567890
''')

add(32, '''def do_algebra_count(operator, operand, target):
    """
    Given two lists operator, and operand, and an integer target. The operators are chosen
    from + - * and the operands are integers (can be negative). The i-th operator is placed
    between the i-th and the (i+1)-th operand. Return the number of ways to replace every
    operator that is the character '?' by one of '+', '-', '*' such that the usual Python
    precedence evaluation of the whole expression equals target.
    Operators that are not '?' stay unchanged.

    Example:
    operator = ['?', '+']
    operand = [1, 2, 3]
    target = 6
    The options: 1+2+3 = 6, 1-2+3 = 2, 1*2+3 = 5, so the result is 1

    Note:
        The number of '?' is at most 10.
    """
''', '''
    import itertools
    positions = [i for i, op in enumerate(operator) if op == "?"]
    count = 0
    for choice in itertools.product("+-*", repeat=len(positions)):
        ops = list(operator)
        for p, c in zip(positions, choice):
            ops[p] = c
        expr = str(operand[0])
        for op, x in zip(ops, operand[1:]):
            expr += " " + op + " (" + str(x) + ")"
        if eval(expr) == target:
            count += 1
    return count
''', '''
assert do_algebra_count([], [5], 5) == 1
assert do_algebra_count([], [5], 4) == 0
assert do_algebra_count(["?", "+"], [1, 2, 3], 6) == 1
assert do_algebra_count(["?"], [3, 3], 6) == 1
assert do_algebra_count(["?"], [3, 3], 9) == 1
assert do_algebra_count(["?"], [3, 3], 0) == 1
assert do_algebra_count(["?"], [2, 2], 4) == 2
assert do_algebra_count(["?", "?"], [0, 0, 0], 0) == 9
assert do_algebra_count(["+", "-"], [1, 2, 3], 0) == 1
assert do_algebra_count(["?", "?"], [1, 2, 3], 7) == 1
assert do_algebra_count(["?"] * 10, [0] * 11, 0) == 3 ** 10
assert do_algebra_count(["?", "?"], [-1, -1, -1], -3) == 1
''')

add(32, '''def evaluate_with_variables(expression, variables):
    """
    Given a string expression that contains non-negative integers, variable names (lower case
    latin letters only), the operators '+', '-', '*' and spaces, and a dictionary variables that maps
    every variable name to an integer, return the value of the expression using the usual
    precedence (multiplication before addition and subtraction, left to right otherwise).
    Do not use eval. The expression is always valid and not empty; there are no parentheses and no
    unary operators.

    Example:
    evaluate_with_variables("2 + x * 3", {"x": 4}) == 14
    evaluate_with_variables("a - b - c", {"a": 10, "b": 3, "c": 2}) == 5
    """
''', '''
    tokens = expression.split()
    values = []
    for t in tokens:
        if t in "+-*" and len(t) == 1:
            values.append(t)
        elif t.isdigit():
            values.append(int(t))
        else:
            values.append(variables[t])
    # first pass: multiplication
    terms = [values[0]]
    ops = []
    i = 1
    while i < len(values):
        op, v = values[i], values[i + 1]
        if op == "*":
            terms[-1] *= v
        else:
            ops.append(op)
            terms.append(v)
        i += 2
    result = terms[0]
    for op, v in zip(ops, terms[1:]):
        result = result + v if op == "+" else result - v
    return result
''', '''
assert evaluate_with_variables("5", {}) == 5
assert evaluate_with_variables("x", {"x": -3}) == -3
assert evaluate_with_variables("2 + x * 3", {"x": 4}) == 14
assert evaluate_with_variables("a - b - c", {"a": 10, "b": 3, "c": 2}) == 5
assert evaluate_with_variables("2 * 3 * 4", {}) == 24
assert evaluate_with_variables("1 - 2 * 3", {}) == -5
assert evaluate_with_variables("x * x - x", {"x": -2}) == 6
assert evaluate_with_variables("a * b + c * d", {"a": 1, "b": 2, "c": 3, "d": 4}) == 14
assert evaluate_with_variables("ab + abc", {"ab": 1, "abc": 2}) == 3
assert evaluate_with_variables("0 * x", {"x": 10 ** 18}) == 0
assert evaluate_with_variables("x * x * x", {"x": 10 ** 6}) == 10 ** 18
assert evaluate_with_variables("  1   +   2  ", {}) == 3
assert evaluate_with_variables("1 + 2 * 3 - 4 * 5 + 6", {}) == -7
assert evaluate_with_variables(" + ".join(["1"] * 50000), {}) == 50000
assert evaluate_with_variables(" * ".join(["1"] * 50000), {}) == 1
import random
random.seed(33)
for _ in range(300):
    n = random.randint(1, 6)
    toks = [str(random.randint(0, 9))]
    for _ in range(n):
        toks += [random.choice("+-*"), str(random.randint(0, 9))]
    e = " ".join(toks)
    assert evaluate_with_variables(e, {}) == eval(e), e
''')

# ---------------- parent 33: generate_integers ----------------
add(33, '''def generate_odd_digits(a, b):
    """
    Given two positive integers a and b, return the odd digits between a
    and b, in ascending order. Only single digits (1-9) are considered.

    For example:
    generate_odd_digits(2, 8) => [3, 5, 7]
    generate_odd_digits(8, 2) => [3, 5, 7]
    generate_odd_digits(10, 14) => []
    """
''', '''
    lo, hi = min(a, b), max(a, b)
    return [i for i in range(max(lo, 1), min(hi, 9) + 1) if i % 2 == 1]
''', '''
assert generate_odd_digits(2, 8) == [3, 5, 7]
assert generate_odd_digits(8, 2) == [3, 5, 7]
assert generate_odd_digits(10, 14) == []
assert generate_odd_digits(1, 1) == [1]
assert generate_odd_digits(2, 2) == []
assert generate_odd_digits(1, 100) == [1, 3, 5, 7, 9]
assert generate_odd_digits(9, 9) == [9]
assert generate_odd_digits(9, 10 ** 18) == [9]
assert generate_odd_digits(10 ** 18, 10 ** 19) == []
assert generate_odd_digits(5, 1) == [1, 3, 5]
assert generate_odd_digits(0, 3) == [1, 3]
''')

add(33, '''def generate_digit_range(a, b, step):
    """
    Given two positive integers a and b and a positive integer step, return the single digits
    (0-9) that are between a and b inclusive and are reachable from the smaller of the two
    by repeatedly adding step, in ascending order.

    For example:
    generate_digit_range(2, 8, 3) => [2, 5, 8]
    generate_digit_range(8, 2, 3) => [2, 5, 8]
    generate_digit_range(10, 14, 1) => []
    """
''', '''
    lo, hi = min(a, b), max(a, b)
    return [x for x in range(lo, min(hi, 9) + 1, step)]
''', '''
assert generate_digit_range(2, 8, 3) == [2, 5, 8]
assert generate_digit_range(8, 2, 3) == [2, 5, 8]
assert generate_digit_range(10, 14, 1) == []
assert generate_digit_range(1, 9, 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert generate_digit_range(1, 9, 100) == [1]
assert generate_digit_range(5, 5, 1) == [5]
assert generate_digit_range(0, 9, 3) == [0, 3, 6, 9]
assert generate_digit_range(3, 100, 2) == [3, 5, 7, 9]
assert generate_digit_range(9, 10 ** 18, 10 ** 18) == [9]
assert generate_digit_range(10, 10, 1) == []
assert generate_digit_range(4, 6, 10 ** 30) == [4]
''')

add(33, '''def generate_primes_in_range(a, b):
    """
    Given two integers a and b (in any order), return the prime numbers between a and b
    inclusive, in ascending order. Values can be negative and the distance between a and b is at
    most 10**5.

    For example:
    generate_primes_in_range(2, 10) => [2, 3, 5, 7]
    generate_primes_in_range(10, 2) => [2, 3, 5, 7]
    generate_primes_in_range(-5, 1) => []
    """
''', '''
    lo, hi = min(a, b), max(a, b)
    result = []
    for n in range(max(lo, 2), hi + 1):
        i = 2
        while i * i <= n:
            if n % i == 0:
                break
            i += 1
        else:
            result.append(n)
    return result
''', '''
assert generate_primes_in_range(2, 10) == [2, 3, 5, 7]
assert generate_primes_in_range(10, 2) == [2, 3, 5, 7]
assert generate_primes_in_range(-5, 1) == []
assert generate_primes_in_range(-5, 2) == [2]
assert generate_primes_in_range(0, 0) == []
assert generate_primes_in_range(1, 1) == []
assert generate_primes_in_range(2, 2) == [2]
assert generate_primes_in_range(3, 3) == [3]
assert generate_primes_in_range(4, 4) == []
assert generate_primes_in_range(14, 16) == []
assert generate_primes_in_range(10 ** 9, 10 ** 9 + 20) == [1000000007, 1000000009]
assert len(generate_primes_in_range(0, 10 ** 5)) == 9592
''')

add(33, '''def generate_even_numbers(a, b):
    """
    Given two integers a and b (in any order, can be negative), return the even numbers between
    a and b inclusive, in ascending order. The distance between a and b is at most 10**6.

    For example:
    generate_even_numbers(2, 8) => [2, 4, 6, 8]
    generate_even_numbers(8, 2) => [2, 4, 6, 8]
    generate_even_numbers(-3, 3) => [-2, 0, 2]
    generate_even_numbers(5, 5) => []
    """
''', '''
    lo, hi = min(a, b), max(a, b)
    start = lo if lo % 2 == 0 else lo + 1
    return list(range(start, hi + 1, 2))
''', '''
assert generate_even_numbers(2, 8) == [2, 4, 6, 8]
assert generate_even_numbers(8, 2) == [2, 4, 6, 8]
assert generate_even_numbers(-3, 3) == [-2, 0, 2]
assert generate_even_numbers(5, 5) == []
assert generate_even_numbers(4, 4) == [4]
assert generate_even_numbers(0, 0) == [0]
assert generate_even_numbers(-4, -4) == [-4]
assert generate_even_numbers(-5, -5) == []
assert generate_even_numbers(-1, 1) == [0]
assert generate_even_numbers(1, 2) == [2]
assert generate_even_numbers(10 ** 18 - 1, 10 ** 18 + 1) == [10 ** 18]
assert len(generate_even_numbers(-10 ** 6, 0)) == 500001
assert generate_even_numbers(-10 ** 18 - 1, -10 ** 18 + 1) == [-10 ** 18]
''')

add(33, '''def generate_square_digits(a, b):
    """
    Given two positive integers a and b (in any order), return the perfect squares between a
    and b inclusive, in ascending order. The values can be as large as 10**18, but there are at
    most 10**5 squares in the range.

    For example:
    generate_square_digits(1, 20) => [1, 4, 9, 16]
    generate_square_digits(20, 1) => [1, 4, 9, 16]
    generate_square_digits(5, 8) => []
    """
''', '''
    import math
    lo, hi = min(a, b), max(a, b)
    start = math.isqrt(max(lo - 1, 0)) + 1
    end = math.isqrt(hi)
    return [i * i for i in range(start, end + 1)]
''', '''
assert generate_square_digits(1, 20) == [1, 4, 9, 16]
assert generate_square_digits(20, 1) == [1, 4, 9, 16]
assert generate_square_digits(5, 8) == []
assert generate_square_digits(4, 4) == [4]
assert generate_square_digits(1, 1) == [1]
assert generate_square_digits(2, 2) == []
assert generate_square_digits(3, 4) == [4]
assert generate_square_digits(4, 9) == [4, 9]
assert generate_square_digits(5, 9) == [9]
assert generate_square_digits(10 ** 18, 10 ** 18) == [10 ** 18]
assert generate_square_digits(10 ** 18 - 1, 10 ** 18 - 1) == []
r = generate_square_digits(10 ** 18 - 2 * 10 ** 9 * 1000, 10 ** 18)
assert len(r) == 1001 and r[-1] == 10 ** 18 and r[0] == (10 ** 9 - 1000) ** 2
assert generate_square_digits(999999999999999999, 10 ** 18) == [10 ** 18]
''')
