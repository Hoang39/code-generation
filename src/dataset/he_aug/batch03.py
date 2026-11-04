# parents 11-20
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------- parent 11: starts_one_ends ----------------
add(11, '''def starts_and_ends_with(n, d):
    """
    Given a positive integer n and a digit d (0-9), return the count of the n-digit
    positive integers (no leading zeros) that start AND end with the digit d.
    The result can be large, Python integers are unbounded.
    Examples:
    starts_and_ends_with(1, 5) == 1
    starts_and_ends_with(2, 5) == 1
    starts_and_ends_with(3, 5) == 10
    starts_and_ends_with(2, 0) == 0
    """
''', '''
    if n == 1:
        return 1
    if d == 0:
        return 0
    return 10 ** (n - 2)
''', '''
assert starts_and_ends_with(1, 0) == 1
assert starts_and_ends_with(1, 9) == 1
assert starts_and_ends_with(2, 0) == 0
assert starts_and_ends_with(2, 1) == 1
assert starts_and_ends_with(3, 0) == 0
assert starts_and_ends_with(3, 7) == 10
assert starts_and_ends_with(4, 9) == 100
assert starts_and_ends_with(50, 3) == 10 ** 48
assert starts_and_ends_with(2000, 3) == 10 ** 1998
for n in range(1, 5):
    for d in range(10):
        lo = 10 ** (n - 1) if n > 1 else 0
        c = sum(1 for x in range(max(lo, 1) if n > 1 else 0, 10 ** n) if str(x)[0] == str(d) and str(x)[-1] == str(d))
        assert starts_and_ends_with(n, d) == c, (n, d)
''')

add(11, '''def starts_or_ends_with(n, d):
    """
    Given a positive integer n and a digit d (1-9), return the count of the n-digit
    positive integers that start OR end with the digit d.
    Examples:
    starts_or_ends_with(1, 5) == 1
    starts_or_ends_with(2, 5) == 18
    starts_or_ends_with(3, 5) == 180
    """
''', '''
    if n == 1:
        return 1
    return 18 * 10 ** (n - 2)
''', '''
assert starts_or_ends_with(1, 1) == 1
assert starts_or_ends_with(1, 9) == 1
assert starts_or_ends_with(2, 9) == 18
assert starts_or_ends_with(3, 4) == 180
assert starts_or_ends_with(10, 2) == 18 * 10 ** 8
assert starts_or_ends_with(1500, 2) == 18 * 10 ** 1498
for n in range(1, 5):
    for d in range(1, 10):
        c = sum(1 for x in range(10 ** (n - 1) if n > 1 else 1, 10 ** n) if str(x)[0] == str(d) or str(x)[-1] == str(d))
        assert starts_or_ends_with(n, d) == c, (n, d)
''')

add(11, '''def count_n_digit_without(n, d):
    """
    Given a positive integer n and a digit d (0-9), return the count of the n-digit
    positive integers (no leading zeros) that do not contain the digit d anywhere.
    Examples:
    count_n_digit_without(1, 5) == 8
    count_n_digit_without(2, 0) == 81
    count_n_digit_without(2, 5) == 72
    """
''', '''
    if d == 0:
        return 9 ** n
    if n == 1:
        return 8
    return 8 * 9 ** (n - 1)
''', '''
assert count_n_digit_without(1, 0) == 9
assert count_n_digit_without(1, 1) == 8
assert count_n_digit_without(2, 0) == 81
assert count_n_digit_without(2, 5) == 72
assert count_n_digit_without(3, 9) == 648
assert count_n_digit_without(30, 7) == 8 * 9 ** 29
assert count_n_digit_without(1000, 0) == 9 ** 1000
for n in range(1, 5):
    for d in range(10):
        c = sum(1 for x in range(10 ** (n - 1) if n > 1 else 1, 10 ** n) if str(d) not in str(x))
        assert count_n_digit_without(n, d) == c, (n, d)
''')

add(11, '''def count_n_digit_palindromes(n):
    """
    Given a positive integer n, return the count of the n-digit positive integers
    (no leading zeros) that are palindromes in base 10.
    Examples:
    count_n_digit_palindromes(1) == 9
    count_n_digit_palindromes(2) == 9
    count_n_digit_palindromes(3) == 90
    """
''', '''
    return 9 * 10 ** ((n - 1) // 2)
''', '''
assert count_n_digit_palindromes(1) == 9
assert count_n_digit_palindromes(2) == 9
assert count_n_digit_palindromes(3) == 90
assert count_n_digit_palindromes(4) == 90
assert count_n_digit_palindromes(5) == 900
assert count_n_digit_palindromes(100) == 9 * 10 ** 49
assert count_n_digit_palindromes(1001) == 9 * 10 ** 500
for n in range(1, 7):
    c = sum(1 for x in range(10 ** (n - 1) if n > 1 else 1, 10 ** n) if str(x) == str(x)[::-1])
    assert count_n_digit_palindromes(n) == c, n
''')

add(11, '''def count_n_digit_multiples(n, k):
    """
    Given positive integers n and k, return the count of the n-digit positive integers
    (no leading zeros) that are divisible by k.
    Examples:
    count_n_digit_multiples(1, 3) == 3
    count_n_digit_multiples(2, 10) == 9
    count_n_digit_multiples(2, 1000) == 0
    """
''', '''
    lo = 10 ** (n - 1)
    hi = 10 ** n - 1
    return hi // k - (lo - 1) // k
''', '''
assert count_n_digit_multiples(1, 1) == 9
assert count_n_digit_multiples(1, 3) == 3
assert count_n_digit_multiples(1, 10) == 0
assert count_n_digit_multiples(2, 10) == 9
assert count_n_digit_multiples(2, 7) == 13
assert count_n_digit_multiples(2, 1000) == 0
assert count_n_digit_multiples(3, 100) == 9
assert count_n_digit_multiples(3, 999) == 1
assert count_n_digit_multiples(3, 1) == 900
assert count_n_digit_multiples(100, 7) == (10 ** 100 - 1) // 7 - (10 ** 99 - 1) // 7
assert count_n_digit_multiples(1000, 1) == 9 * 10 ** 999
for n in range(1, 4):
    for k in range(1, 60):
        c = sum(1 for x in range(10 ** (n - 1) if n > 1 else 1, 10 ** n) if x % k == 0)
        assert count_n_digit_multiples(n, k) == c, (n, k)
''')

# ---------------- parent 12: anti_shuffle ----------------
add(12, '''def reverse_sort_words(s):
    """
    Write a function that takes a string and returns a version of it where every word
    (separated by single spaces) has its characters arranged in descending order based on
    ascii value. Keep the order of words and every blank space (including leading,
    trailing and repeated ones) as in the sentence.

    For example:
    reverse_sort_words('Hi') returns 'iH'
    reverse_sort_words('hello world') returns 'ollhe wrold'
    reverse_sort_words(' a  b ') returns ' a  b '
    """
''', '''
    return " ".join("".join(sorted(w, reverse=True)) for w in s.split(" "))
''', '''
assert reverse_sort_words("") == ""
assert reverse_sort_words(" ") == " "
assert reverse_sort_words("Hi") == "iH"
assert reverse_sort_words("hello world") == "ollhe wrold"
assert reverse_sort_words(" a  b ") == " a  b "
assert reverse_sort_words("abc  cba") == "cba  cba"
assert reverse_sort_words("Zz aA") == "zZ aA"
assert reverse_sort_words("a1B2") == "aB21"
assert reverse_sort_words("!!!") == "!!!"
assert reverse_sort_words("\\tb a") == "b\\t a"
big = "dcba " * 20000
assert reverse_sort_words(big) == "dcba " * 20000
''')

add(12, '''def sort_words_by_length(s):
    """
    Write a function that takes a string of words separated by single spaces and returns
    the words sorted by length (shorter first). Words with the same length keep their
    original relative order. The result is a string with words joined by one space.
    An empty string gives an empty string.

    For example:
    sort_words_by_length('a bb c') returns 'a c bb'
    sort_words_by_length('three two one') returns 'two one three'
    """
''', '''
    if not s:
        return ""
    return " ".join(sorted(s.split(" "), key=len))
''', '''
assert sort_words_by_length("") == ""
assert sort_words_by_length("a") == "a"
assert sort_words_by_length("a bb c") == "a c bb"
assert sort_words_by_length("three two one") == "two one three"
assert sort_words_by_length("bb aa cc") == "bb aa cc"
assert sort_words_by_length("x" * 50 + " y") == "y " + "x" * 50
assert sort_words_by_length("ab a") == "a ab"
assert sort_words_by_length(" ".join(["abc", "d"] * 30000)) == " ".join(["d"] * 30000 + ["abc"] * 30000)
''')

add(12, '''def sort_letters_keep_others(s):
    """
    Write a function that takes a string and returns it with all letters (a-z, A-Z) sorted
    ignoring case in ascending order (when two letters are equal ignoring case, keep their
    original relative order), while every non-letter character stays at its original position.

    For example:
    sort_letters_keep_others('b-a') returns 'a-b'
    sort_letters_keep_others('Hello, World!') returns 'deHll, loorW!'
    """
''', '''
    letters = sorted((c for c in s if c.isalpha() and c.isascii()), key=lambda c: c.lower())
    it = iter(letters)
    return "".join(next(it) if c.isalpha() and c.isascii() else c for c in s)
''', '''
assert sort_letters_keep_others("") == ""
assert sort_letters_keep_others("123") == "123"
assert sort_letters_keep_others("b-a") == "a-b"
assert sort_letters_keep_others("Hello, World!") == "deHll, loorW!"
assert sort_letters_keep_others("aA") == "aA"
assert sort_letters_keep_others("Aa") == "Aa"
assert sort_letters_keep_others("ba AB") == "aA bB"
assert sort_letters_keep_others("z") == "z"
assert sort_letters_keep_others("c b a") == "a b c"
assert sort_letters_keep_others("zyx" * 10000) == "".join(sorted("zyx" * 10000))
s = "9z8y7x"
assert sort_letters_keep_others(s) == "9x8y7z"
''')

add(12, '''def anti_shuffle_lines(text):
    """
    Write a function that takes a multi-line string and returns it where, inside every line,
    each word (separated by space) is replaced by a word with the characters arranged in
    ascending order based on ascii value. Lines are separated by the newline character '\\\\n'.
    Keep the order of lines, words and blank spaces. Empty lines stay empty.

    For example:
    anti_shuffle_lines('ba\\\\ndc fe') returns 'ab\\\\ncd ef'
    """
''', '''
    return "\\n".join(" ".join("".join(sorted(w)) for w in line.split(" ")) for line in text.split("\\n"))
''', '''
assert anti_shuffle_lines("") == ""
assert anti_shuffle_lines("\\n") == "\\n"
assert anti_shuffle_lines("ba\\ndc fe") == "ab\\ncd ef"
assert anti_shuffle_lines("\\n\\nba") == "\\n\\nab"
assert anti_shuffle_lines("ba\\n") == "ab\\n"
assert anti_shuffle_lines(" ba  ba ") == " ab  ab "
assert anti_shuffle_lines("Hello World") == "Hello Wdlor"
assert anti_shuffle_lines(("cba\\n" * 30000)) == "abc\\n" * 30000
''')

add(12, '''def count_anagram_words(s):
    """
    Write a function that takes a string of words separated by spaces and returns the number
    of words (counted with repetition, empty words ignored) whose sorted characters are equal to the
    sorted characters of the FIRST word. The first word itself counts. For a string without
    words return 0. Comparison is case-sensitive.

    For example:
    count_anagram_words('listen silent enlist google') returns 3
    count_anagram_words('Aa aA a') returns 2
    """
''', '''
    words = s.split()
    if not words:
        return 0
    key = sorted(words[0])
    return sum(1 for w in words if sorted(w) == key)
''', '''
assert count_anagram_words("") == 0
assert count_anagram_words("   ") == 0
assert count_anagram_words("a") == 1
assert count_anagram_words("listen silent enlist google") == 3
assert count_anagram_words("Aa aA a") == 2
assert count_anagram_words("Aa aa") == 1
assert count_anagram_words("  ab   ba  ab ") == 3
assert count_anagram_words("ab abc") == 1
assert count_anagram_words(("abc cba bca " * 20000)) == 60000
''')

# ---------------- parent 13: is_bored ----------------
add(13, '''def count_questions(S):
    """
    You'll be given a string of text, and your task is to count the number of
    sentences that are questions. Sentences are delimited by '.', '?' or '!'.
    A sentence is a question when it ends with '?'. A '?' at the very end of the
    string counts, repeated delimiters like '?!' or '??' produce empty sentences
    which are ignored (only the last delimiter before an empty piece matters, so
    '??' contains one question).

    For example:
    >>> count_questions("Hello world")
    0
    >>> count_questions("Who are you? I am fine. Really?")
    2
    """
''', '''
    count = 0
    has_text = False
    for ch in S:
        if ch in ".!?":
            if has_text and ch == "?":
                count += 1
            has_text = False
        elif not ch.isspace():
            has_text = True
    return count
''', '''
assert count_questions("") == 0
assert count_questions("?") == 0
assert count_questions("a?") == 1
assert count_questions("??") == 0
assert count_questions("a??") == 1
assert count_questions("a?!") == 1
assert count_questions("a!?") == 0
assert count_questions("a? b? c.") == 2
assert count_questions("  ?  ") == 0
assert count_questions("Who? What? Why") == 2
assert count_questions("Really?" * 50000) == 50000
assert count_questions("x." * 50000) == 0
''')

add(13, '''def count_sentences(S):
    """
    You'll be given a string of words, and your task is to count the number of
    sentences. Sentences are delimited by '.', '?' or '!'. A piece that is empty or
    contains only whitespace is not a sentence.

    For example:
    >>> count_sentences("Hello world")
    1
    >>> count_sentences("Hi. How are you? Fine!")
    3
    >>> count_sentences("...")
    0
    """
''', '''
    for d in "?!":
        S = S.replace(d, ".")
    return len([p for p in S.split(".") if p.strip()])
''', '''
assert count_sentences("") == 0
assert count_sentences(" ") == 0
assert count_sentences("...") == 0
assert count_sentences("?!.") == 0
assert count_sentences("a") == 1
assert count_sentences("a.") == 1
assert count_sentences("a. b") == 2
assert count_sentences("a.. b!!") == 2
assert count_sentences("Hi. How are you? Fine!") == 3
assert count_sentences(" . a . ") == 1
assert count_sentences("a.\\nb.") == 2
assert count_sentences("w. " * 40000) == 40000
''')

add(13, '''def count_bored_sentences(S):
    """
    You'll be given a string of words. A boredom is a sentence that starts with the
    word "I" (a standalone word, so "I", "I am" and "I'm" ... only "I" followed by a space
    or the end of the sentence counts, "It" and "I'm" do not). Sentences are delimited by
    '.', '?' or '!', and leading whitespace of a sentence is ignored.

    For example:
    >>> count_bored_sentences("I am bored. It is late! I")
    2
    >>> count_bored_sentences("I'm here. Hi I")
    0
    """
''', '''
    for d in "?!":
        S = S.replace(d, ".")
    count = 0
    for sentence in S.split("."):
        words = sentence.split()
        if words and words[0] == "I":
            count += 1
    return count
''', '''
assert count_bored_sentences("") == 0
assert count_bored_sentences("I") == 1
assert count_bored_sentences("I.") == 1
assert count_bored_sentences("I am bored. It is late! I") == 2
assert count_bored_sentences("I'm here. Hi I") == 0
assert count_bored_sentences("  I am.   I do?") == 2
assert count_bored_sentences("i am") == 0
assert count_bored_sentences("I\\tam") == 1
assert count_bored_sentences("Hi.I am") == 1
assert count_bored_sentences("II. I I. Is") == 1
assert count_bored_sentences("I am. " * 40000) == 40000
''')

add(13, '''def longest_sentence_words(S):
    """
    You'll be given a string of words. Sentences are delimited by '.', '?' or '!'.
    Return the number of words (separated by whitespace) of the sentence that has the most
    words. If there are no words at all, return 0.

    For example:
    >>> longest_sentence_words("Hello world")
    2
    >>> longest_sentence_words("Hi. The sun is shining! Ok?")
    4
    """
''', '''
    for d in "?!":
        S = S.replace(d, ".")
    return max((len(p.split()) for p in S.split(".")), default=0)
''', '''
assert longest_sentence_words("") == 0
assert longest_sentence_words("...") == 0
assert longest_sentence_words("a") == 1
assert longest_sentence_words("Hello world") == 2
assert longest_sentence_words("Hi. The sun is shining! Ok?") == 4
assert longest_sentence_words("a b. c d e!   f") == 3
assert longest_sentence_words("a  b\\n c") == 3
assert longest_sentence_words("w " * 100000) == 100000
assert longest_sentence_words("w. " * 100000) == 1
''')

add(13, '''def capitalize_sentences(S):
    """
    You'll be given a string of text. Sentences are delimited by '.', '?' or '!'.
    Return the text where the first letter of every sentence is converted to upper case.
    Delimiters, spaces and all other characters stay exactly where they are; only the first
    non-space character of each sentence is changed (if it is a letter).

    For example:
    >>> capitalize_sentences("hello world. how are you? fine!")
    'Hello world. How are you? Fine!'
    >>> capitalize_sentences("  a.b")
    '  A.B'
    """
''', '''
    result = []
    start = True
    for ch in S:
        if start and not ch.isspace():
            if ch in ".?!":
                result.append(ch)
            else:
                result.append(ch.upper())
                start = False
            continue
        result.append(ch)
        if ch in ".?!":
            start = True
    return "".join(result)
''', '''
assert capitalize_sentences("") == ""
assert capitalize_sentences("a") == "A"
assert capitalize_sentences("hello world. how are you? fine!") == "Hello world. How are you? Fine!"
assert capitalize_sentences("  a.b") == "  A.B"
assert capitalize_sentences("1a. b") == "1a. B"
assert capitalize_sentences("a..b") == "A..B"
assert capitalize_sentences("...") == "..."
assert capitalize_sentences("a. \\n b") == "A. \\n B"
assert capitalize_sentences("ABC. DEF") == "ABC. DEF"
assert capitalize_sentences("x. " * 50000) == "X. " * 50000
''')

# ---------------- parent 14: encode ----------------
add(14, '''def decode_vowel_digits(message):
    """
    Write a function that decodes a message produced by this encoding: swap the case of all
    letters, then replace every vowel of the swapped text with a digit using this table:
    a->1 e->2 i->3 o->4 u->5 A->6 E->7 I->8 O->9 U->0.
    Assume the original message has only letters and spaces. Decoding must return the original message.

    Examples:
    >>> decode_vowel_digits('T7ST')
    'test'
    >>> decode_vowel_digits('tH8S 8S 6 M7SS6G7')
    'This is a message'
    """
''', '''
    back = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u",
            "6": "A", "7": "E", "8": "I", "9": "O", "0": "U"}
    return "".join(back.get(ch, ch).swapcase() for ch in message)
''', '''
assert decode_vowel_digits("") == ""
assert decode_vowel_digits(" ") == " "
assert decode_vowel_digits("T7ST") == "test"
assert decode_vowel_digits("tH8S 8S 6 M7SS6G7") == "This is a message"
assert decode_vowel_digits("1") == "A"
assert decode_vowel_digits("0") == "u"
assert decode_vowel_digits("xyz") == "XYZ"
def encode(message):
    table = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5", "A": "6", "E": "7", "I": "8", "O": "9", "U": "0"}
    return "".join(table.get(ch.swapcase(), ch.swapcase()) for ch in message)
assert encode("test") == "T7ST"
import random
random.seed(7)
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ  "
for _ in range(300):
    m = "".join(random.choice(letters) for _ in range(random.randint(0, 30)))
    assert decode_vowel_digits(encode(m)) == m, m
assert decode_vowel_digits("1" * 100000) == "A" * 100000
''')

add(14, '''def caesar_vowels(message, k):
    """
    Write a function that takes a message and an integer k, and encodes it by replacing every
    vowel (a, e, i, o, u, in lower case or upper case) with the vowel that is k places further in
    the cyclic order a -> e -> i -> o -> u -> a, keeping the case of the letter. All other
    characters stay the same. k can be negative or larger than 5.

    Examples:
    >>> caesar_vowels('hello', 1)
    'hillu'
    >>> caesar_vowels('AEIOU', -1)
    'UAEIO'
    """
''', '''
    lower = "aeiou"
    upper = "AEIOU"
    out = []
    for ch in message:
        if ch in lower:
            out.append(lower[(lower.index(ch) + k) % 5])
        elif ch in upper:
            out.append(upper[(upper.index(ch) + k) % 5])
        else:
            out.append(ch)
    return "".join(out)
''', '''
assert caesar_vowels("", 3) == ""
assert caesar_vowels("hello", 0) == "hello"
assert caesar_vowels("hello", 1) == "hillu"
assert caesar_vowels("hello", 5) == "hello"
assert caesar_vowels("hello", -5) == "hello"
assert caesar_vowels("AEIOU", -1) == "UAEIO"
assert caesar_vowels("aeiou", 6) == "eioua"
assert caesar_vowels("Quiet Day", 2) == "Qeuot Diy"
assert caesar_vowels("xyz 123!", 4) == "xyz 123!"
assert caesar_vowels("aA", 10**18 + 1) == "eE"
assert caesar_vowels("u", -10**18) == "u"
assert caesar_vowels("ae" * 50000, 7) == "io" * 50000
''')

add(14, '''def rot13_letters(message):
    """
    Write a function that takes a message and encodes it with ROT13: every letter is replaced
    with the letter 13 places ahead in the english alphabet (cyclic), keeping the case. All other
    characters (digits, spaces, punctuation) stay the same.

    Examples:
    >>> rot13_letters('Hello, World!')
    'Uryyb, Jbeyq!'
    >>> rot13_letters('abc xyz')
    'nop klm'
    """
''', '''
    out = []
    for ch in message:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + 13) % 26 + 97))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + 13) % 26 + 65))
        else:
            out.append(ch)
    return "".join(out)
''', '''
assert rot13_letters("") == ""
assert rot13_letters("Hello, World!") == "Uryyb, Jbeyq!"
assert rot13_letters("abc xyz") == "nop klm"
assert rot13_letters("n") == "a"
assert rot13_letters("Z") == "M"
assert rot13_letters("123 !?") == "123 !?"
assert rot13_letters("\\u00e9") == "\\u00e9"
import string
assert rot13_letters(rot13_letters(string.printable)) == string.printable
assert rot13_letters(string.ascii_lowercase) == "nopqrstuvwxyzabcdefghijklm"
assert rot13_letters("a" * 100000) == "n" * 100000
''')

add(14, '''def encode_runs(message):
    """
    Write a function that takes a message of letters and encodes it by run-length encoding:
    every maximal run of the same character is replaced by the character followed by the length
    of the run, but only when the run is longer than 1. The comparison is case-sensitive.
    Assume the message contains no digits.

    Examples:
    >>> encode_runs('aaabcc')
    'a3bc2'
    >>> encode_runs('abc')
    'abc'
    >>> encode_runs('')
    ''
    """
''', '''
    out = []
    i = 0
    n = len(message)
    while i < n:
        j = i
        while j < n and message[j] == message[i]:
            j += 1
        out.append(message[i] + (str(j - i) if j - i > 1 else ""))
        i = j
    return "".join(out)
''', '''
assert encode_runs("") == ""
assert encode_runs("a") == "a"
assert encode_runs("aa") == "a2"
assert encode_runs("aaabcc") == "a3bc2"
assert encode_runs("abc") == "abc"
assert encode_runs("aAaA") == "aAaA"
assert encode_runs("aaAA") == "a2A2"
assert encode_runs("a" * 10) == "a10"
assert encode_runs("a" * 100000) == "a100000"
assert encode_runs("ab" * 50000) == "ab" * 50000
assert encode_runs("  x") == " 2x"
''')

# ---------------- parent 15: count_up_to ----------------
add(15, '''def primes_between(a, b):
    """Implement a function that takes two non-negative integers a and b and returns a list of
    the prime numbers p with a <= p <= b in ascending order. If a > b return an empty list.
    The value b can be as large as 10**6.
    for example:
    primes_between(2, 10) => [2,3,5,7]
    primes_between(14, 16) => []
    primes_between(10, 2) => []
    primes_between(0, 1) => []
    """
''', '''
    if a > b or b < 2:
        return []
    sieve = bytearray([1]) * (b + 1)
    sieve[0] = 0
    if b >= 1:
        sieve[1] = 0
    for i in range(2, int(b ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, b + 1, i)))
    return [i for i in range(max(a, 0), b + 1) if sieve[i]]
''', '''
assert primes_between(0, 0) == []
assert primes_between(0, 1) == []
assert primes_between(0, 2) == [2]
assert primes_between(2, 2) == [2]
assert primes_between(3, 3) == [3]
assert primes_between(4, 4) == []
assert primes_between(2, 10) == [2, 3, 5, 7]
assert primes_between(14, 16) == []
assert primes_between(10, 2) == []
assert primes_between(1, 30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert primes_between(90, 100) == [97]
assert len(primes_between(0, 10 ** 6)) == 78498
assert primes_between(10 ** 6 - 20, 10 ** 6) == [999983]
assert primes_between(999983, 999983) == [999983]
''')

add(15, '''def count_primes_up_to(n):
    """Implement a function that takes a non-negative integer n and returns the number of
    prime numbers that are less than or equal to n. The value n can be as large as 2 * 10**6.
    for example:
    count_primes_up_to(10) => 4
    count_primes_up_to(2) => 1
    count_primes_up_to(1) => 0
    count_primes_up_to(0) => 0
    """
''', '''
    if n < 2:
        return 0
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return sum(sieve)
''', '''
assert count_primes_up_to(0) == 0
assert count_primes_up_to(1) == 0
assert count_primes_up_to(2) == 1
assert count_primes_up_to(3) == 2
assert count_primes_up_to(4) == 2
assert count_primes_up_to(10) == 4
assert count_primes_up_to(100) == 25
assert count_primes_up_to(1000) == 168
assert count_primes_up_to(10 ** 5) == 9592
assert count_primes_up_to(10 ** 6) == 78498
assert count_primes_up_to(2 * 10 ** 6) == 148933
''')

add(15, '''def count_up_to_twin(n):
    """Implement a function that takes a non-negative integer n and returns a list of the
    twin prime pairs (p, p + 2) where both numbers are prime and p + 2 <= n, in ascending
    order, as a list of tuples.
    for example:
    count_up_to_twin(5) => [(3, 5)]
    count_up_to_twin(20) => [(3, 5), (5, 7), (11, 13), (17, 19)]
    count_up_to_twin(4) => []
    count_up_to_twin(0) => []
    """
''', '''
    if n < 5:
        return []
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return [(p, p + 2) for p in range(3, n - 1) if sieve[p] and sieve[p + 2]]
''', '''
assert count_up_to_twin(0) == []
assert count_up_to_twin(1) == []
assert count_up_to_twin(4) == []
assert count_up_to_twin(5) == [(3, 5)]
assert count_up_to_twin(6) == [(3, 5)]
assert count_up_to_twin(7) == [(3, 5), (5, 7)]
assert count_up_to_twin(20) == [(3, 5), (5, 7), (11, 13), (17, 19)]
assert len(count_up_to_twin(10 ** 5)) == 1224
assert count_up_to_twin(10 ** 6)[-1] == (999959, 999961)
''')

add(15, '''def prime_gaps(n):
    """Implement a function that takes a non-negative integer n and returns the list of
    differences between consecutive prime numbers that are less than n.
    The list is empty when there are fewer than two such primes.
    for example:
    prime_gaps(10) => [1, 2, 2]
    prime_gaps(3) => []
    prime_gaps(4) => [1]
    prime_gaps(0) => []
    """
''', '''
    primes = []
    sieve = [True] * max(n, 2)
    for i in range(2, n):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, n, i):
                sieve[j] = False
    return [primes[i + 1] - primes[i] for i in range(len(primes) - 1)]
''', '''
assert prime_gaps(0) == []
assert prime_gaps(1) == []
assert prime_gaps(2) == []
assert prime_gaps(3) == []
assert prime_gaps(4) == [1]
assert prime_gaps(5) == [1]
assert prime_gaps(6) == [1, 2]
assert prime_gaps(10) == [1, 2, 2]
assert prime_gaps(30) == [1, 2, 2, 4, 2, 4, 2, 4, 6]
g = prime_gaps(10 ** 6)
assert len(g) == 78497 and max(g) == 114 and sum(g) == 999983 - 2
''')

add(15, '''def goldbach_pair(n):
    """Implement a function that takes an even integer n >= 4 and returns the tuple (p, q)
    of prime numbers with p <= q and p + q == n, choosing the pair with the smallest p.
    The value n can be as large as 10**6.
    for example:
    goldbach_pair(4) => (2, 2)
    goldbach_pair(10) => (3, 7)
    goldbach_pair(28) => (5, 23)
    """
''', '''
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    for p in range(2, n // 2 + 1):
        if sieve[p] and sieve[n - p]:
            return (p, n - p)
''', '''
assert goldbach_pair(4) == (2, 2)
assert goldbach_pair(6) == (3, 3)
assert goldbach_pair(8) == (3, 5)
assert goldbach_pair(10) == (3, 7)
assert goldbach_pair(28) == (5, 23)
assert goldbach_pair(100) == (3, 97)
assert goldbach_pair(10 ** 6) == (17, 999983)
for n in range(4, 300, 2):
    p, q = goldbach_pair(n)
    assert p <= q and p + q == n
    assert all(p % d for d in range(2, p)) and all(q % d for d in range(2, q))
''')

# ---------------- parent 16: make_a_pile ----------------
add(16, '''def make_a_pyramid(n):
    """
    Given a positive integer n, you have to make a pyramid of n levels of blocks.
    The first (top) level has 1 block, and every next level has 2 more blocks than the
    previous one. Return the number of blocks in each level in a list, where element at
    index i represents the number of blocks in the level (i+1).

    Examples:
    >>> make_a_pyramid(3)
    [1, 3, 5]
    >>> make_a_pyramid(1)
    [1]
    """
''', '''
    return [2 * i + 1 for i in range(n)]
''', '''
assert make_a_pyramid(1) == [1]
assert make_a_pyramid(2) == [1, 3]
assert make_a_pyramid(3) == [1, 3, 5]
assert make_a_pyramid(0) == []
assert make_a_pyramid(100000)[-1] == 199999
assert sum(make_a_pyramid(1000)) == 1000 ** 2
assert len(make_a_pyramid(100000)) == 100000
''')

add(16, '''def make_a_pile_step(n, k):
    """
    Given positive integers n and k, make a pile of n levels of stones.
    The first level has n stones. The number of stones in every next level is the number
    of stones of the previous level plus k. Return the number of stones in each level
    in a list, where element at index i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile_step(3, 2)
    [3, 5, 7]
    >>> make_a_pile_step(4, 1)
    [4, 5, 6, 7]
    """
''', '''
    return [n + k * i for i in range(n)]
''', '''
assert make_a_pile_step(1, 1) == [1]
assert make_a_pile_step(1, 100) == [1]
assert make_a_pile_step(3, 2) == [3, 5, 7]
assert make_a_pile_step(4, 1) == [4, 5, 6, 7]
assert make_a_pile_step(3, 0) == [3, 3, 3]
assert make_a_pile_step(2, 10 ** 18) == [2, 2 + 10 ** 18]
assert make_a_pile_step(100000, 3)[-1] == 100000 + 3 * 99999
assert len(make_a_pile_step(100000, 3)) == 100000
''')

add(16, '''def make_a_pile_alternating(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones. The number of stones in the next level is:
        - the previous level plus 1 if the index of the previous level (1-based) is odd.
        - the previous level plus 3 if the index of the previous level (1-based) is even.
    Return the number of stones in each level in a list.

    Examples:
    >>> make_a_pile_alternating(4)
    [4, 5, 8, 9]
    >>> make_a_pile_alternating(1)
    [1]
    """
''', '''
    result = []
    stones = n
    for i in range(1, n + 1):
        result.append(stones)
        stones += 1 if i % 2 == 1 else 3
    return result
''', '''
assert make_a_pile_alternating(1) == [1]
assert make_a_pile_alternating(2) == [2, 3]
assert make_a_pile_alternating(3) == [3, 4, 7]
assert make_a_pile_alternating(4) == [4, 5, 8, 9]
assert make_a_pile_alternating(5) == [5, 6, 9, 10, 13]
r = make_a_pile_alternating(100000)
assert len(r) == 100000 and r[-1] == 100000 + 199997
assert all(r[i + 1] - r[i] == (1 if i % 2 == 0 else 3) for i in range(len(r) - 1))
''')

add(16, '''def pile_total(n):
    """
    Given a positive integer n, a pile has n levels of stones. The first level has n stones
    and each next level has 2 stones more than the previous one. Return the total number of
    stones in the whole pile. n can be as large as 10**18, so do not build the list.

    Examples:
    >>> pile_total(3)
    15
    >>> pile_total(1)
    1
    """
''', '''
    return n * n + n * (n - 1)
''', '''
assert pile_total(1) == 1
assert pile_total(2) == 6
assert pile_total(3) == 15
assert pile_total(4) == 28
assert pile_total(10 ** 18) == 2 * 10 ** 36 - 10 ** 18
for n in range(1, 200):
    assert pile_total(n) == sum(n + 2 * i for i in range(n))
''')

add(16, '''def level_of_stone(n, s):
    """
    A pile has n levels of stones. The first level has n stones and each next level has
    2 stones more than the previous one. Stones are numbered 1, 2, 3, ... starting from the
    first level, then the second level and so on. Return the 1-based level that contains the
    stone with the number s, or -1 if s is smaller than 1 or larger than the total number of stones.
    n and s can be as large as 10**18.

    Examples:
    >>> level_of_stone(3, 3)
    1
    >>> level_of_stone(3, 4)
    2
    >>> level_of_stone(3, 16)
    -1
    """
''', '''
    total = n * n + n * (n - 1)
    if s < 1 or s > total:
        return -1
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        upto = mid * n + mid * (mid - 1)
        if upto >= s:
            hi = mid
        else:
            lo = mid + 1
    return lo
''', '''
assert level_of_stone(1, 1) == 1
assert level_of_stone(1, 2) == -1
assert level_of_stone(3, 0) == -1
assert level_of_stone(3, -4) == -1
assert level_of_stone(3, 3) == 1
assert level_of_stone(3, 4) == 2
assert level_of_stone(3, 8) == 2
assert level_of_stone(3, 9) == 3
assert level_of_stone(3, 15) == 3
assert level_of_stone(3, 16) == -1
n = 10 ** 18
total = n * n + n * (n - 1)
assert level_of_stone(n, total) == n
assert level_of_stone(n, total + 1) == -1
assert level_of_stone(n, n) == 1
assert level_of_stone(n, n + 1) == 2
for n in range(1, 12):
    s = 1
    for lvl in range(1, n + 1):
        for _ in range(n + 2 * (lvl - 1)):
            assert level_of_stone(n, s) == lvl, (n, s)
            s += 1
''')

# ---------------- parent 17: words_string ----------------
add(17, '''def words_by_delimiters(s, delimiters):
    """
    You will be given a string of words separated by any of the characters in the string
    delimiters (and/or by spaces). Your task is to split the string into words and return a
    list of the words. Empty words are dropped.

    For example:
    words_by_delimiters("Hi;my,name is John", ";,") == ["Hi", "my", "name", "is", "John"]
    words_by_delimiters("a--b", "-") == ["a", "b"]
    words_by_delimiters("", ",") == []
    """
''', '''
    for d in delimiters:
        s = s.replace(d, " ")
    return s.split()
''', '''
assert words_by_delimiters("", ",") == []
assert words_by_delimiters("   ", ",") == []
assert words_by_delimiters(",,,", ",") == []
assert words_by_delimiters("Hi;my,name is John", ";,") == ["Hi", "my", "name", "is", "John"]
assert words_by_delimiters("a--b", "-") == ["a", "b"]
assert words_by_delimiters("a.b", "") == ["a.b"]
assert words_by_delimiters("a,b", ".") == ["a,b"]
assert words_by_delimiters("a\\tb\\nc", ",") == ["a", "b", "c"]
assert words_by_delimiters("x|y|z", "|") == ["x", "y", "z"]
assert words_by_delimiters("a,b " * 50000, ",") == ["a", "b"] * 50000
''')

add(17, '''def count_words_in_string(s):
    """
    You will be given a string of words separated by commas and/or spaces. Return a dictionary
    that maps every word (case-insensitive, converted to lower case) to the number of times it
    appears. The keys must appear in the order of their first occurrence.

    For example:
    count_words_in_string("Hi, hi, my name") == {"hi": 2, "my": 1, "name": 1}
    count_words_in_string("") == {}
    """
''', '''
    result = {}
    for word in s.replace(",", " ").split():
        w = word.lower()
        result[w] = result.get(w, 0) + 1
    return result
''', '''
assert count_words_in_string("") == {}
assert count_words_in_string(",,, ,") == {}
assert count_words_in_string("Hi, hi, my name") == {"hi": 2, "my": 1, "name": 1}
assert list(count_words_in_string("b, a, B, c")) == ["b", "a", "c"]
assert count_words_in_string("A a A") == {"a": 3}
assert count_words_in_string("one,two,three,one") == {"one": 2, "two": 1, "three": 1}
assert count_words_in_string("x " * 100000) == {"x": 100000}
assert count_words_in_string("Word,word,WORD") == {"word": 3}
''')

add(17, '''def split_keep_quoted(s):
    """
    You will be given a string of words separated by spaces. Words wrapped in double quotes
    may contain spaces and must stay together as a single word; the quotes are removed from the result.
    Assume that quotes are always balanced and that a quoted part is always surrounded by spaces
    or by the borders of the string. Return the list of words.

    For example:
    split_keep_quoted('a "b c" d') == ['a', 'b c', 'd']
    split_keep_quoted('"x y"') == ['x y']
    split_keep_quoted('') == []
    """
''', '''
    result = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == " ":
            i += 1
        elif s[i] == '"':
            j = s.index('"', i + 1)
            result.append(s[i + 1:j])
            i = j + 1
        else:
            j = i
            while j < n and s[j] != " ":
                j += 1
            result.append(s[i:j])
            i = j
    return result
''', '''
assert split_keep_quoted("") == []
assert split_keep_quoted("   ") == []
assert split_keep_quoted("a") == ["a"]
assert split_keep_quoted('a "b c" d') == ["a", "b c", "d"]
assert split_keep_quoted('"x y"') == ["x y"]
assert split_keep_quoted('""') == [""]
assert split_keep_quoted('a  b') == ["a", "b"]
assert split_keep_quoted('" a  b " c') == [" a  b ", "c"]
assert split_keep_quoted('"a" "b"') == ["a", "b"]
assert split_keep_quoted('"a b" ' * 30000) == ["a b"] * 30000
assert split_keep_quoted("w " * 100000) == ["w"] * 100000
''')

add(17, '''def words_with_positions(s):
    """
    You will be given a string of words separated by commas or spaces. Return a list of
    tuples (word, start) with every word and the 0-based index in the original string where
    this word starts, in order. Empty words are dropped.

    For example:
    words_with_positions("Hi, my") == [("Hi", 0), ("my", 4)]
    words_with_positions("  a,b") == [("a", 2), ("b", 4)]
    words_with_positions("") == []
    """
''', '''
    result = []
    start = None
    for i, ch in enumerate(s):
        if ch in ", \\t\\n":
            if start is not None:
                result.append((s[start:i], start))
                start = None
        elif start is None:
            start = i
    if start is not None:
        result.append((s[start:], start))
    return result
''', '''
assert words_with_positions("") == []
assert words_with_positions(",") == []
assert words_with_positions("a") == [("a", 0)]
assert words_with_positions("Hi, my") == [("Hi", 0), ("my", 4)]
assert words_with_positions("  a,b") == [("a", 2), ("b", 4)]
assert words_with_positions("a,,b,") == [("a", 0), ("b", 3)]
assert words_with_positions("abc") == [("abc", 0)]
assert words_with_positions("a\\tb") == [("a", 0), ("b", 2)]
r = words_with_positions("ab," * 50000)
assert len(r) == 50000 and r[-1] == ("ab", 3 * 49999)
''')

add(17, '''def longest_word(s):
    """
    You will be given a string of words separated by commas or spaces. Return the longest word.
    If several words have the same maximal length return the first one. If there are no words,
    return an empty string.

    For example:
    longest_word("Hi, my name is John") == "John"
    longest_word("aa, bb") == "aa"
    longest_word(",, ,") == ""
    """
''', '''
    best = ""
    for word in s.replace(",", " ").split():
        if len(word) > len(best):
            best = word
    return best
''', '''
assert longest_word("") == ""
assert longest_word(",, ,") == ""
assert longest_word("a") == "a"
assert longest_word("Hi, my name is John") == "name"
assert longest_word("aa, bb") == "aa"
assert longest_word("a bb ccc dd") == "ccc"
assert longest_word("abc,abd") == "abc"
assert longest_word("x" * 100000 + ",y") == "x" * 100000
assert longest_word("a, " * 50000) == "a"
''')

# ---------------- parent 18: f ----------------
add(18, '''def g(n):
    """ Implement the function g that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the
    sum of the squares of the numbers from 1 to i if i is odd,
    or the product of the numbers from 1 to i (the factorial) modulo 1000007 otherwise.
    i starts from 1.
    Example:
    g(5) == [1, 2, 14, 24, 55]
    """
''', '''
    result = []
    fact = 1
    squares = 0
    for i in range(1, n + 1):
        fact = fact * i % 1000007
        squares += i * i
        result.append(squares if i % 2 == 1 else fact)
    return result
''', '''
assert g(0) == []
assert g(1) == [1]
assert g(2) == [1, 2]
assert g(5) == [1, 2, 14, 24, 55]
r = g(10)
assert r[5] == 720 and r[7] == 40320 and r[9] == 3628800 % 1000007
r = g(100000)
assert len(r) == 100000
assert r[-2] == 99999 * 100000 * 199999 // 6
f = 1
for i in range(1, 100001):
    f = f * i % 1000007
assert r[-1] == f
''')

add(18, '''def tri_sums(n):
    """ Implement the function tri_sums that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is
    the sum of the numbers from 1 to i if i is odd, or the sum of the cubes of the numbers
    from 1 to i if i is even. i starts from 1.
    Example:
    tri_sums(5) == [1, 9, 6, 100, 15]
    """
''', '''
    result = []
    for i in range(1, n + 1):
        s = i * (i + 1) // 2
        result.append(s if i % 2 == 1 else s * s)
    return result
''', '''
assert tri_sums(0) == []
assert tri_sums(1) == [1]
assert tri_sums(2) == [1, 9]
assert tri_sums(5) == [1, 9, 6, 100, 15]
r = tri_sums(10 ** 5)
assert len(r) == 10 ** 5
assert r[-1] == (10 ** 5 * (10 ** 5 + 1) // 2) ** 2
assert r[-2] == 99999 * 100000 // 2
for n in range(1, 60):
    assert tri_sums(n)[-1] == (sum(range(1, n + 1)) if n % 2 else sum(i ** 3 for i in range(1, n + 1)))
''')

add(18, '''def running_factorials(n):
    """ Implement the function running_factorials that takes n as a parameter and
    returns a list of size n where the element at index i (starting from 1) is the factorial of i.
    Python integers are unbounded but to keep numbers small return the factorial of i modulo
    10**9 + 7. Once the factorial becomes divisible by the modulus the value stays 0 forever.
    Example:
    running_factorials(5) == [1, 2, 6, 24, 120]
    """
''', '''
    mod = 10 ** 9 + 7
    result = []
    f = 1
    for i in range(1, n + 1):
        f = f * i % mod
        result.append(f)
    return result
''', '''
assert running_factorials(0) == []
assert running_factorials(1) == [1]
assert running_factorials(5) == [1, 2, 6, 24, 120]
r = running_factorials(20)
assert r[-1] == 2432902008176640000 % (10 ** 9 + 7)
r = running_factorials(10 ** 6)
assert len(r) == 10 ** 6
assert 0 not in r[:10 ** 6]
''')

add(18, '''def fib_or_square(n):
    """ Implement the function fib_or_square that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the
    i-th Fibonacci number (1, 1, 2, 3, 5, ...) if i is even,
    or i squared if i is odd. i starts from 1.
    Example:
    fib_or_square(6) == [1, 1, 9, 3, 25, 8]
    """
''', '''
    result = []
    a, b = 1, 1
    for i in range(1, n + 1):
        result.append(a if i % 2 == 0 else i * i)
        a, b = b, a + b
    return result
''', '''
assert fib_or_square(0) == []
assert fib_or_square(1) == [1]
assert fib_or_square(2) == [1, 1]
assert fib_or_square(6) == [1, 1, 9, 3, 25, 8]
r = fib_or_square(200)
assert r[199] == 280571172992510140037611932413038677189525
assert r[198] == 199 ** 2
assert len(fib_or_square(10 ** 4)) == 10 ** 4
''')

add(18, '''def alternating_partial_sums(n):
    """ Implement the function alternating_partial_sums that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the
    alternating sum 1 - 2 + 3 - 4 + ... +/- i (odd numbers added, even numbers subtracted).
    i starts from 1.
    Example:
    alternating_partial_sums(5) == [1, -1, 2, -2, 3]
    """
''', '''
    result = []
    total = 0
    for i in range(1, n + 1):
        total += i if i % 2 == 1 else -i
        result.append(total)
    return result
''', '''
assert alternating_partial_sums(0) == []
assert alternating_partial_sums(1) == [1]
assert alternating_partial_sums(2) == [1, -1]
assert alternating_partial_sums(5) == [1, -1, 2, -2, 3]
r = alternating_partial_sums(10 ** 5)
assert r[-1] == -50000 and r[-2] == 50000
assert len(r) == 10 ** 5
for i in range(1, 100):
    assert alternating_partial_sums(i)[-1] == (i + 1) // 2 if i % 2 else -(i // 2)
''')

# ---------------- parent 19: exchange ----------------
add(19, '''def can_make_all_odd(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of integers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only odd numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between lst1 and lst2 to make
    all the elements of lst1 odd, return "YES". Otherwise, return "NO".
    Each exchange swaps one element of lst1 with one element of lst2.
    The lists may be empty; an empty lst1 is already all odd.
    For example:
    can_make_all_odd([2, 4], [1, 3]) => "YES"
    can_make_all_odd([2, 4], [1, 2]) => "NO"
    """
''', '''
    even_in_first = sum(1 for x in lst1 if x % 2 == 0)
    odd_in_second = sum(1 for x in lst2 if x % 2 != 0)
    return "YES" if even_in_first <= odd_in_second else "NO"
''', '''
assert can_make_all_odd([], []) == "YES"
assert can_make_all_odd([], [2]) == "YES"
assert can_make_all_odd([1], []) == "YES"
assert can_make_all_odd([2], []) == "NO"
assert can_make_all_odd([2, 4], [1, 3]) == "YES"
assert can_make_all_odd([2, 4], [1, 2]) == "NO"
assert can_make_all_odd([-2, 0], [-1, 5]) == "YES"
assert can_make_all_odd([-2, 0], [-1, -2]) == "NO"
assert can_make_all_odd([0], [-3]) == "YES"
assert can_make_all_odd([2] * 50000, [1] * 50000) == "YES"
assert can_make_all_odd([2] * 50001, [1] * 50000) == "NO"
''')

add(19, '''def can_sort_by_exchange(lst1, lst2):
    """You are given two lists of integers of the same length. In one exchange you swap the
    elements at the same index i of lst1 and lst2 (lst1[i] <-> lst2[i]). You may exchange any
    set of indices. Return "YES" if it is possible to make BOTH lists strictly increasing,
    otherwise return "NO". Empty lists are strictly increasing.
    For example:
    can_sort_by_exchange([1, 5], [2, 3]) => "YES"
    can_sort_by_exchange([2, 1], [2, 1]) => "NO"
    """
''', '''
    keep_ok, swap_ok = True, True
    pa, pb = float("-inf"), float("-inf")
    for i in range(len(lst1)):
        a, b = lst1[i], lst2[i]
        new_keep = (keep_ok and a > pa and b > pb) or (swap_ok and a > pb and b > pa)
        new_swap = (keep_ok and b > pa and a > pb) or (swap_ok and b > pb and a > pa)
        keep_ok, swap_ok = new_keep, new_swap
        pa, pb = a, b
        if not (keep_ok or swap_ok):
            return "NO"
    return "YES"
''', '''
assert can_sort_by_exchange([], []) == "YES"
assert can_sort_by_exchange([1], [1]) == "YES"
assert can_sort_by_exchange([1, 5], [2, 3]) == "YES"
assert can_sort_by_exchange([1, 2], [1, 2]) == "YES"
assert can_sort_by_exchange([2, 1], [2, 1]) == "NO"
assert can_sort_by_exchange([1, 3, 5], [2, 4, 6]) == "YES"
assert can_sort_by_exchange([5, 1], [1, 5]) == "NO"
assert can_sort_by_exchange([3, 2], [1, 4]) == "YES"
assert can_sort_by_exchange([1, 4], [3, 2]) == "YES"
assert can_sort_by_exchange([3, 3], [1, 2]) == "NO"
assert can_sort_by_exchange([-5, -3], [-4, -6]) == "NO"
assert can_sort_by_exchange([-5, -3], [-4, -2]) == "YES"
import itertools, random
def brute(a, b):
    n = len(a)
    for mask in range(1 << n):
        x = [b[i] if mask >> i & 1 else a[i] for i in range(n)]
        y = [a[i] if mask >> i & 1 else b[i] for i in range(n)]
        if all(x[i] < x[i + 1] for i in range(n - 1)) and all(y[i] < y[i + 1] for i in range(n - 1)):
            return "YES"
    return "NO"
random.seed(11)
for _ in range(500):
    n = random.randint(0, 7)
    a = [random.randint(-3, 8) for _ in range(n)]
    b = [random.randint(-3, 8) for _ in range(n)]
    assert can_sort_by_exchange(a, b) == brute(a, b), (a, b)
n = 100000
assert can_sort_by_exchange(list(range(n)), list(range(n))) == "YES"
assert can_sort_by_exchange(list(range(n - 1)) + [n - 2], list(range(n - 1)) + [n - 2]) == "NO"
assert can_sort_by_exchange(list(range(0, 2 * n, 2)), list(range(1, 2 * n, 2))) == "YES"
''')

add(19, '''def min_exchanges_all_even(lst1, lst2):
    """Two lists of integers lst1 and lst2 are given. In one exchange you swap one element
    of lst1 with one element of lst2. Return the minimum number of exchanges needed to make
    all elements of lst1 even, or -1 if it is impossible.
    For example:
    min_exchanges_all_even([1, 2, 3], [4, 6, 8]) => 2
    min_exchanges_all_even([1, 3], [5, 7]) => -1
    min_exchanges_all_even([2, 4], [1]) => 0
    """
''', '''
    odd_in_first = sum(1 for x in lst1 if x % 2 != 0)
    even_in_second = sum(1 for x in lst2 if x % 2 == 0)
    return odd_in_first if odd_in_first <= even_in_second else -1
''', '''
assert min_exchanges_all_even([], []) == 0
assert min_exchanges_all_even([2, 4], [1]) == 0
assert min_exchanges_all_even([1, 2, 3], [4, 6, 8]) == 2
assert min_exchanges_all_even([1, 3], [5, 7]) == -1
assert min_exchanges_all_even([1], []) == -1
assert min_exchanges_all_even([-1, -3], [0, -2]) == 2
assert min_exchanges_all_even([0], [1]) == 0
assert min_exchanges_all_even([1] * 100000, [2] * 100000) == 100000
assert min_exchanges_all_even([1] * 100001, [2] * 100000) == -1
''')

add(19, '''def can_balance_sums(lst1, lst2):
    """You are given two lists of integers. In one exchange you swap one element of lst1 with
    one element of lst2. You may exchange at most ONE pair of elements. Return "YES" if it is
    possible (with zero or one exchange) to make sum(lst1) equal to sum(lst2), otherwise "NO".
    For example:
    can_balance_sums([1, 2], [3]) => "YES"
    can_balance_sums([1, 1], [5]) => "NO"
    can_balance_sums([2], [2]) => "YES"
    """
''', '''
    d = sum(lst1) - sum(lst2)
    if d == 0:
        return "YES"
    if d % 2 != 0:
        return "NO"
    need = d // 2
    seen = set(lst2)
    for x in lst1:
        if x - need in seen:
            return "YES"
    return "NO"
''', '''
assert can_balance_sums([], []) == "YES"
assert can_balance_sums([1], []) == "NO"
assert can_balance_sums([1, 2], [3]) == "YES"
assert can_balance_sums([1, 1], [5]) == "NO"
assert can_balance_sums([2], [2]) == "YES"
assert can_balance_sums([1, 5], [2, 2]) == "NO"
assert can_balance_sums([3, 1], [2, 0]) == "YES"
assert can_balance_sums([3], [4]) == "NO"
assert can_balance_sums([-1, 7], [0, 0]) == "NO"
import random
def brute(a, b):
    if sum(a) == sum(b):
        return "YES"
    for i in range(len(a)):
        for j in range(len(b)):
            if sum(a) - a[i] + b[j] == sum(b) - b[j] + a[i]:
                return "YES"
    return "NO"
random.seed(5)
for _ in range(500):
    a = [random.randint(-6, 6) for _ in range(random.randint(0, 5))]
    b = [random.randint(-6, 6) for _ in range(random.randint(0, 5))]
    assert can_balance_sums(a, b) == brute(a, b), (a, b)
assert can_balance_sums(list(range(100000)), list(range(100000))) == "YES"
assert can_balance_sums(list(range(100000)), [10 ** 9]) == "NO"
''')

add(19, '''def exchange_to_same_parity(lst1, lst2):
    """You are given two non-empty lists of integers. In one exchange you swap one element of
    lst1 with one element of lst2. Determine whether it is possible, with any number of
    exchanges, to make every element of lst1 have the same parity as the first
    element of lst2 (before any exchange). Return "YES" or "NO".
    For example:
    exchange_to_same_parity([1, 2], [3, 5]) => "YES"
    exchange_to_same_parity([1, 3, 4], [2, 3]) => "NO"
    """
''', '''
    target = lst2[0] % 2
    wrong = sum(1 for x in lst1 if x % 2 != target)
    good = sum(1 for x in lst2 if x % 2 == target)
    return "YES" if wrong <= good else "NO"
''', '''
assert exchange_to_same_parity([1, 2], [3, 5]) == "YES"
assert exchange_to_same_parity([1, 3, 4], [2, 3]) == "NO"
assert exchange_to_same_parity([2, 4], [2]) == "YES"
assert exchange_to_same_parity([1], [2]) == "YES"
assert exchange_to_same_parity([1, 3], [2]) == "NO"
assert exchange_to_same_parity([-1, 3], [-3]) == "YES"
assert exchange_to_same_parity([-2], [-1]) == "YES"
assert exchange_to_same_parity([0, 2, 4], [1, 3, 5]) == "YES"
assert exchange_to_same_parity([0, 2, 4, 6], [1, 3, 5]) == "NO"
assert exchange_to_same_parity([1] * 50000, [3] * 50000) == "YES"
assert exchange_to_same_parity([2] * 50001, [3] * 50000) == "NO"
''')

# ---------------- parent 20: maximum ----------------
add(20, '''def minimum(arr, k):
    """
    Given an array arr of integers and a non-negative integer k, return a sorted list
    of length k with the minimum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 2
        Output: [-4, -3]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [-4, 4]

    Note:
        1. The length of the array will be in the range of [1, 100000].
        2. The elements in the array will be in the range of [-10**9, 10**9].
        3. 0 <= k <= len(arr)
    """
''', '''
    return sorted(arr)[:k]
''', '''
assert minimum([1], 0) == []
assert minimum([1], 1) == [1]
assert minimum([-3, -4, 5], 2) == [-4, -3]
assert minimum([4, -4, 4], 2) == [-4, 4]
assert minimum([4, 4, 4], 2) == [4, 4]
assert minimum([5, 4, 3, 2, 1], 5) == [1, 2, 3, 4, 5]
assert minimum([10 ** 9, -10 ** 9], 1) == [-10 ** 9]
assert minimum(list(range(100000, 0, -1)), 3) == [1, 2, 3]
orig = [3, 1, 2]
minimum(orig, 2)
assert orig == [3, 1, 2]
''')

add(20, '''def kth_largest(arr, k):
    """
    Given a non-empty array arr of integers and a positive integer k, return the k-th largest
    element of the array (counting duplicates, so for [5, 5, 3] the 2nd largest is 5).

    Example 1:

        Input: arr = [3, 2, 1, 5, 6, 4], k = 2
        Output: 5

    Example 2:

        Input: arr = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
        Output: 4

    Note:
        1. The length of the array will be in the range of [1, 100000].
        2. 1 <= k <= len(arr)
    """
''', '''
    return sorted(arr, reverse=True)[k - 1]
''', '''
assert kth_largest([1], 1) == 1
assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert kth_largest([5, 5, 3], 2) == 5
assert kth_largest([5, 5, 3], 3) == 3
assert kth_largest([-1, -2, -3], 1) == -1
assert kth_largest([-1, -2, -3], 3) == -3
assert kth_largest(list(range(100000)), 100000) == 0
assert kth_largest(list(range(100000)), 1) == 99999
assert kth_largest([7] * 100000, 50000) == 7
''')

add(20, '''def top_k_frequent(arr, k):
    """
    Given an array arr of integers and a non-negative integer k, return a list with the k most
    frequent distinct values. Values with the same frequency are ordered by value, ascending.
    The result is ordered by frequency, descending.

    Example 1:

        Input: arr = [1, 1, 1, 2, 2, 3], k = 2
        Output: [1, 2]

    Example 2:

        Input: arr = [4, 5, 5, 4, 6], k = 3
        Output: [4, 5, 6]

    Note:
        1. 0 <= k <= number of distinct values in arr
    """
''', '''
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    order = sorted(counts, key=lambda v: (-counts[v], v))
    return order[:k]
''', '''
assert top_k_frequent([], 0) == []
assert top_k_frequent([1], 0) == []
assert top_k_frequent([1], 1) == [1]
assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert top_k_frequent([4, 5, 5, 4, 6], 3) == [4, 5, 6]
assert top_k_frequent([3, 2, 1], 2) == [1, 2]
assert top_k_frequent([-1, -1, -2, -2, 0], 2) == [-2, -1]
assert top_k_frequent([9, 9, 8], 1) == [9]
assert top_k_frequent(list(range(100000)) + [5] * 3, 1) == [5]
assert top_k_frequent(list(range(50000)) * 2, 2) == [0, 1]
''')

add(20, '''def sum_of_k_largest(arr, k):
    """
    Given an array arr of integers and a non-negative integer k, return the sum of the k largest
    numbers in arr (duplicates count separately). The sum of zero numbers is 0.

    Example 1:

        Input: arr = [-3, -4, 5], k = 2
        Output: 2

    Example 2:

        Input: arr = [4, -4, 4], k = 3
        Output: 4

    Note:
        1. 0 <= k <= len(arr) <= 100000
    """
''', '''
    if k == 0:
        return 0
    return sum(sorted(arr)[-k:])
''', '''
assert sum_of_k_largest([], 0) == 0
assert sum_of_k_largest([5], 0) == 0
assert sum_of_k_largest([5], 1) == 5
assert sum_of_k_largest([-3, -4, 5], 2) == 2
assert sum_of_k_largest([4, -4, 4], 3) == 4
assert sum_of_k_largest([1, 2, 3, 4], 4) == 10
assert sum_of_k_largest([-1, -2], 1) == -1
assert sum_of_k_largest(list(range(100000)), 100000) == 100000 * 99999 // 2
assert sum_of_k_largest(list(range(100000)), 2) == 99999 + 99998
assert sum_of_k_largest([10 ** 18] * 100, 100) == 10 ** 20
''')

add(20, '''def maximum_unique(arr, k):
    """
    Given an array arr of integers and a non-negative integer k, return a sorted list of the
    k largest DISTINCT values in arr. If arr has fewer than k distinct values, return all
    of them.

    Example 1:

        Input: arr = [4, -4, 4], k = 2
        Output: [-4, 4]

    Example 2:

        Input: arr = [3, 3, 2, 2, 1], k = 2
        Output: [2, 3]

    Note:
        1. The length of the array will be in the range of [0, 100000].
        2. 0 <= k
    """
''', '''
    if k == 0:
        return []
    return sorted(set(arr))[-k:]
''', '''
assert maximum_unique([], 0) == []
assert maximum_unique([], 3) == []
assert maximum_unique([1], 0) == []
assert maximum_unique([1], 1) == [1]
assert maximum_unique([4, -4, 4], 2) == [-4, 4]
assert maximum_unique([3, 3, 2, 2, 1], 2) == [2, 3]
assert maximum_unique([3, 3, 2, 2, 1], 10) == [1, 2, 3]
assert maximum_unique([5, 5, 5], 1) == [5]
assert maximum_unique(list(range(100000)) * 2, 3) == [99997, 99998, 99999]
assert maximum_unique([-1, -1, -2], 1) == [-1]
''')
