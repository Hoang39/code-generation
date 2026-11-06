# parents: HumanEval/83 (starts_one_ends), /86 (anti_shuffle), /91 (is_bored), /93 (encode), /96 (count_up_to)
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------------------------------------------------------- HumanEval/83
add(83, '''def starts_and_ends_one(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that both start and end with 1.
    >>> starts_and_ends_one(1)
    1
    >>> starts_and_ends_one(3)
    10
    """
''', '''
    if n == 1:
        return 1
    return 10 ** (n - 2)
''', '''
def brute(n):
    return sum(1 for v in range(10 ** (n - 1), 10 ** n) if str(v)[0] == "1" and str(v)[-1] == "1")
assert starts_and_ends_one(1) == 1
assert starts_and_ends_one(2) == 1
assert starts_and_ends_one(3) == 10
assert starts_and_ends_one(4) == 100
assert starts_and_ends_one(5) == 1000
assert starts_and_ends_one(10) == 10 ** 8
assert starts_and_ends_one(19) == 10 ** 17
for n in range(1, 7):
    assert starts_and_ends_one(n) == brute(n), n
assert starts_and_ends_one(1000) == 10 ** 998
assert starts_and_ends_one(5000) == 10 ** 4998
assert isinstance(starts_and_ends_one(30), int)
assert starts_and_ends_one(7) == 100000
assert starts_and_ends_one(6) == 10000
''')

add(83, '''def neither_starts_nor_ends_one(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that neither start nor end with 1.
    >>> neither_starts_nor_ends_one(1)
    8
    >>> neither_starts_nor_ends_one(2)
    72
    """
''', '''
    if n == 1:
        return 8
    return 72 * 10 ** (n - 2)
''', '''
def brute(n):
    return sum(1 for v in range(10 ** (n - 1), 10 ** n) if str(v)[0] != "1" and str(v)[-1] != "1")
assert neither_starts_nor_ends_one(1) == 8
assert neither_starts_nor_ends_one(2) == 72
assert neither_starts_nor_ends_one(3) == 720
assert neither_starts_nor_ends_one(4) == 7200
assert neither_starts_nor_ends_one(5) == 72000
assert neither_starts_nor_ends_one(12) == 72 * 10 ** 10
for n in range(1, 7):
    assert neither_starts_nor_ends_one(n) == brute(n), n
assert neither_starts_nor_ends_one(500) == 72 * 10 ** 498
total = lambda n: 9 * 10 ** (n - 1)
assert neither_starts_nor_ends_one(7) == 7200000
assert neither_starts_nor_ends_one(8) == 72000000
assert neither_starts_nor_ends_one(9) == 720000000
for n in range(2, 40):
    assert neither_starts_nor_ends_one(n) + 18 * 10 ** (n - 2) == total(n)
assert neither_starts_nor_ends_one(1) + 1 == 9
assert neither_starts_nor_ends_one(6) == 720000
''')

add(83, '''def count_ending_with_one(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that end with 1.
    >>> count_ending_with_one(1)
    1
    >>> count_ending_with_one(2)
    9
    """
''', '''
    if n == 1:
        return 1
    return 9 * 10 ** (n - 2)
''', '''
def brute(n):
    return sum(1 for v in range(10 ** (n - 1), 10 ** n) if v % 10 == 1)
assert count_ending_with_one(1) == 1
assert count_ending_with_one(2) == 9
assert count_ending_with_one(3) == 90
assert count_ending_with_one(4) == 900
assert count_ending_with_one(5) == 9000
assert count_ending_with_one(15) == 9 * 10 ** 13
for n in range(1, 7):
    assert count_ending_with_one(n) == brute(n), n
assert count_ending_with_one(800) == 9 * 10 ** 798
assert count_ending_with_one(7) == 900000
assert count_ending_with_one(8) == 9000000
assert count_ending_with_one(9) == 90000000
assert count_ending_with_one(2) * 10 == 90
''')

add(83, '''def starts_or_ends_with_digit(n, d):
    """
    Given a positive integer n and a digit d (0 <= d <= 9), return the count of the numbers of
    n-digit positive integers that start or end with the digit d.
    A positive integer never starts with 0.
    >>> starts_or_ends_with_digit(2, 0)
    9
    >>> starts_or_ends_with_digit(2, 1)
    18
    """
''', '''
    if n == 1:
        return 1 if d != 0 else 0
    if d == 0:
        return 9 * 10 ** (n - 2)
    return 18 * 10 ** (n - 2)
''', '''
def brute(n, d):
    return sum(1 for v in range(10 ** (n - 1), 10 ** n) if str(v)[0] == str(d) or str(v)[-1] == str(d))
assert starts_or_ends_with_digit(1, 1) == 1
assert starts_or_ends_with_digit(1, 0) == 0
assert starts_or_ends_with_digit(1, 9) == 1
assert starts_or_ends_with_digit(2, 0) == 9
assert starts_or_ends_with_digit(2, 1) == 18
assert starts_or_ends_with_digit(3, 0) == 90
assert starts_or_ends_with_digit(3, 7) == 180
assert starts_or_ends_with_digit(4, 5) == 1800
assert starts_or_ends_with_digit(4, 0) == 900
assert starts_or_ends_with_digit(20, 9) == 18 * 10 ** 18
for n in range(1, 6):
    for d in range(10):
        assert starts_or_ends_with_digit(n, d) == brute(n, d), (n, d)
assert starts_or_ends_with_digit(700, 0) == 9 * 10 ** 698
assert starts_or_ends_with_digit(700, 3) == 18 * 10 ** 698
''')

add(83, '''def count_n_digit_palindromes(n):
    """
    Given a positive integer n, return the count of the n-digit positive integers
    that read the same from left to right and from right to left.
    >>> count_n_digit_palindromes(1)
    9
    >>> count_n_digit_palindromes(3)
    90
    """
''', '''
    return 9 * 10 ** ((n - 1) // 2)
''', '''
def brute(n):
    return sum(1 for v in range(10 ** (n - 1), 10 ** n) if str(v) == str(v)[::-1])
assert count_n_digit_palindromes(1) == 9
assert count_n_digit_palindromes(2) == 9
assert count_n_digit_palindromes(3) == 90
assert count_n_digit_palindromes(4) == 90
assert count_n_digit_palindromes(5) == 900
assert count_n_digit_palindromes(6) == 900
assert count_n_digit_palindromes(10) == 90000
assert count_n_digit_palindromes(11) == 900000
for n in range(1, 8):
    assert count_n_digit_palindromes(n) == brute(n), n
assert count_n_digit_palindromes(1001) == 9 * 10 ** 500
assert count_n_digit_palindromes(1000) == 9 * 10 ** 499
assert count_n_digit_palindromes(7) == 9000
''')

# ---------------------------------------------------------------- HumanEval/86
add(86, '''def sort_words_desc(s):
    """
    Write a function that takes a string and returns a version of it where all words
    (separated by space) are replaced by a new word where all the characters arranged in
    descending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    sort_words_desc('Hi') returns 'iH'
    sort_words_desc('hello') returns 'ollhe'
    sort_words_desc('Hello World!!!') returns 'olleH roldW!!!'
    """
''', '''
    words = s.split(" ")
    return " ".join("".join(sorted(w, reverse=True)) for w in words)
''', '''
assert sort_words_desc("") == ""
assert sort_words_desc("Hi") == "iH"
assert sort_words_desc("hello") == "ollhe"
assert sort_words_desc("a b c") == "a b c"
assert sort_words_desc("abc cba") == "cba cba"
assert sort_words_desc("  ab  ") == "  ba  "
assert sort_words_desc("a  b") == "a  b"
assert sort_words_desc(" ") == " "
assert sort_words_desc("ABab") == "baBA"
assert sort_words_desc("Hello World!!!") == "olleH roldW!!!"
assert sort_words_desc("12 21 3") == "21 21 3"
assert sort_words_desc("z" * 5 + "a" * 5) == "z" * 5 + "a" * 5
assert sort_words_desc("a" * 5 + "z" * 5) == "z" * 5 + "a" * 5
assert sort_words_desc("tab\\there") == "".join(sorted("tab\\there", reverse=True))
import random
random.seed(41)
for _ in range(300):
    t = "".join(random.choice("abAB1 !") for _ in range(random.randint(0, 20)))
    exp = " ".join("".join(sorted(w, key=ord, reverse=True)) for w in t.split(" "))
    r = sort_words_desc(t)
    assert r == exp
    assert len(r) == len(t) and [i for i, c in enumerate(r) if c == " "] == [i for i, c in enumerate(t) if c == " "]
assert sort_words_desc("ba " * 40000).count(" ") == 40000
''')

add(86, '''def reverse_each_word(s):
    """
    Write a function that takes a string and returns a version of it where every word
    (separated by space) is written backwards.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    reverse_each_word('Hi') returns 'iH'
    reverse_each_word('hello world') returns 'olleh dlrow'
    reverse_each_word('  a  bc ') returns '  a  cb '
    """
''', '''
    return " ".join(w[::-1] for w in s.split(" "))
''', '''
assert reverse_each_word("") == ""
assert reverse_each_word("Hi") == "iH"
assert reverse_each_word("hello world") == "olleh dlrow"
assert reverse_each_word("  a  bc ") == "  a  cb "
assert reverse_each_word(" ") == " "
assert reverse_each_word("   ") == "   "
assert reverse_each_word("abc") == "cba"
assert reverse_each_word("a b c") == "a b c"
assert reverse_each_word("ab\\ncd ef") == "dc\\nba fe"
assert reverse_each_word("Hello, World!") == ",olleH !dlroW"
assert reverse_each_word("racecar level") == "racecar level"
assert reverse_each_word("12 345") == "21 543"
assert reverse_each_word("x" * 100000) == "x" * 100000
assert reverse_each_word("ab " * 50000) == "ba " * 50000
import random
random.seed(42)
for _ in range(300):
    t = "".join(random.choice("ab c") for _ in range(random.randint(0, 20)))
    r = reverse_each_word(t)
    assert len(r) == len(t)
    assert reverse_each_word(r) == t
    assert [i for i, c in enumerate(r) if c == " "] == [i for i, c in enumerate(t) if c == " "]
''')

add(86, '''def sort_chars_keep_spaces(s):
    """
    Write a function that takes a string and returns a string where all non-space characters
    are rearranged in ascending order based on ascii value, while every space stays at its
    original position.

    For example:
    sort_chars_keep_spaces('Hi') returns 'Hi'
    sort_chars_keep_spaces('hello') returns 'ehllo'
    sort_chars_keep_spaces('c b a') returns 'a b c'
    sort_chars_keep_spaces('dcba  fe') returns 'abcd  ef'
    """
''', '''
    letters = sorted(ch for ch in s if ch != " ")
    it = iter(letters)
    return "".join(" " if ch == " " else next(it) for ch in s)
''', '''
assert sort_chars_keep_spaces("") == ""
assert sort_chars_keep_spaces(" ") == " "
assert sort_chars_keep_spaces("Hi") == "Hi"
assert sort_chars_keep_spaces("hello") == "ehllo"
assert sort_chars_keep_spaces("c b a") == "a b c"
assert sort_chars_keep_spaces("dcba  fe") == "abcd  ef"
assert sort_chars_keep_spaces("  ba") == "  ab"
assert sort_chars_keep_spaces("ba  ") == "ab  "
assert sort_chars_keep_spaces("Zz aA") == "AZ az"
assert sort_chars_keep_spaces("3 2 1 0") == "0 1 2 3"
assert sort_chars_keep_spaces("!a ~") == "!a ~"
assert sort_chars_keep_spaces("~ !") == "! ~"
assert sort_chars_keep_spaces("b" * 3 + " " + "a" * 3) == "aaa bbb"
import random
random.seed(43)
for _ in range(300):
    t = "".join(random.choice("abcAB ") for _ in range(random.randint(0, 20)))
    r = sort_chars_keep_spaces(t)
    assert len(r) == len(t)
    assert [i for i, c in enumerate(r) if c == " "] == [i for i, c in enumerate(t) if c == " "]
    assert r.replace(" ", "") == "".join(sorted(t.replace(" ", "")))
big = "zy " * 50000
r = sort_chars_keep_spaces(big)
assert r.count(" ") == 50000 and r.replace(" ", "") == "y" * 50000 + "z" * 50000
''')

add(86, '''def capitalize_words(s):
    """
    Write a function that takes a string and returns a version of it where every word
    (separated by space) starts with an upper case letter and all its other letters are in lower case.
    Note: You should keep the order of words and blank spaces in the sentence.
    Characters that are not letters stay unchanged.

    For example:
    capitalize_words('hI') returns 'Hi'
    capitalize_words('hello WORLD') returns 'Hello World'
    capitalize_words(' a  b ') returns ' A  B '
    """
''', '''
    words = s.split(" ")
    return " ".join(w[:1].upper() + w[1:].lower() for w in words)
''', '''
assert capitalize_words("") == ""
assert capitalize_words(" ") == " "
assert capitalize_words("hI") == "Hi"
assert capitalize_words("hello WORLD") == "Hello World"
assert capitalize_words(" a  b ") == " A  B "
assert capitalize_words("ABC") == "Abc"
assert capitalize_words("abc") == "Abc"
assert capitalize_words("a") == "A"
assert capitalize_words("1abc") == "1abc"
assert capitalize_words("!HELLO") == "!hello"
assert capitalize_words("it's mY liFe") == "It's My Life"
assert capitalize_words("a-b c_d") == "A-b C_d"
assert capitalize_words("x" * 100000) == "X" + "x" * 99999
assert capitalize_words("AB " * 40000) == "Ab " * 40000
import random
random.seed(44)
for _ in range(300):
    t = "".join(random.choice("abAB1 ") for _ in range(random.randint(0, 20)))
    exp = " ".join((w[0].upper() + w[1:].lower()) if w else "" for w in t.split(" "))
    assert capitalize_words(t) == exp
''')

add(86, '''def sort_words_alphabetically(s):
    """
    Write a function that takes a string and returns a version of it where the words
    (separated by space) are rearranged in ascending order based on ascii value, while the
    blank spaces stay exactly where they were, so every word slot keeps its length only
    if the words have the same length.

    For example:
    sort_words_alphabetically('b a') returns 'a b'
    sort_words_alphabetically('pear apple fig') returns 'apple fig pear'
    sort_words_alphabetically('  b   a ') returns '  a   b '
    sort_words_alphabetically('') returns ''
    """
''', '''
    parts = s.split(" ")
    words = sorted(p for p in parts if p)
    it = iter(words)
    return " ".join(next(it) if p else "" for p in parts)
''', '''
assert sort_words_alphabetically("") == ""
assert sort_words_alphabetically(" ") == " "
assert sort_words_alphabetically("a") == "a"
assert sort_words_alphabetically("b a") == "a b"
assert sort_words_alphabetically("pear apple fig") == "apple fig pear"
assert sort_words_alphabetically("  b   a ") == "  a   b "
assert sort_words_alphabetically("b  a") == "a  b"
assert sort_words_alphabetically("B a A b") == "A B a b"
assert sort_words_alphabetically("10 9 8") == "10 8 9"
assert sort_words_alphabetically("x x x") == "x x x"
assert sort_words_alphabetically("ab a") == "a ab"
assert sort_words_alphabetically("abc ab a") == "a ab abc"
assert sort_words_alphabetically("zz yy xx ww") == "ww xx yy zz"
import random
random.seed(45)
for _ in range(300):
    t = "".join(random.choice("abc ") for _ in range(random.randint(0, 20)))
    r = sort_words_alphabetically(t)
    assert r.split() == sorted(t.split())
    assert [w == "" for w in r.split(" ")] == [w == "" for w in t.split(" ")]
big = " ".join(str(i) for i in range(30000, 0, -1))
assert sort_words_alphabetically(big).split(" ") == sorted(str(i) for i in range(1, 30001))
''')

# ---------------------------------------------------------------- HumanEval/91
add(91, '''def count_sentences(S):
    """
    You'll be given a string of words, and your task is to count the number
    of sentences. Sentences are delimited by '.', '?' or '!'.
    A sentence that is empty or contains only spaces is not counted.

    For example:
    >>> count_sentences("Hello world")
    1
    >>> count_sentences("The sky is blue. The sun is shining. I love this weather")
    3
    >>> count_sentences("")
    0
    """
''', '''
    sentences = S.replace("?", ".").replace("!", ".").split(".")
    return len([s for s in sentences if s.strip()])
''', '''
assert count_sentences("") == 0
assert count_sentences(" ") == 0
assert count_sentences("Hello world") == 1
assert count_sentences("The sky is blue. The sun is shining. I love this weather") == 3
assert count_sentences("Hi.") == 1
assert count_sentences("Hi!!") == 1
assert count_sentences("...") == 0
assert count_sentences("?!.") == 0
assert count_sentences("A. B? C!") == 3
assert count_sentences("A.B.C") == 3
assert count_sentences("A.  . B") == 2
assert count_sentences("  .  ") == 0
assert count_sentences("a\\nb. c") == 2
assert count_sentences("Wait... what?! Really") == 3
assert count_sentences(". a") == 1
assert count_sentences("x. " * 50000) == 50000
assert count_sentences("." * 100000) == 0
import random, re
random.seed(51)
for _ in range(300):
    t = "".join(random.choice("ab .?!") for _ in range(random.randint(0, 25)))
    assert count_sentences(t) == len([p for p in re.split(r"[.?!]", t) if p.strip()])
''')

add(91, '''def count_exclamations(S):
    """
    You'll be given a string of words, and your task is to count the number
    of sentences that end with '!'. Sentences are delimited by '.', '?' or '!'.
    A sentence that is empty or contains only spaces is not counted, so in "Hi!!"
    only the first '!' ends a sentence. A text after the last delimiter does not end with anything.

    For example:
    >>> count_exclamations("Hello world")
    0
    >>> count_exclamations("Wow! Really? Yes! No.")
    2
    >>> count_exclamations("Hi!!")
    1
    """
''', '''
    count = 0
    current = ""
    for ch in S:
        if ch in ".?!":
            if ch == "!" and current.strip():
                count += 1
            current = ""
        else:
            current += ch
    return count
''', '''
assert count_exclamations("") == 0
assert count_exclamations("!") == 0
assert count_exclamations("Hi!") == 1
assert count_exclamations("Hello world") == 0
assert count_exclamations("Wow! Really? Yes! No.") == 2
assert count_exclamations("Hi!!") == 1
assert count_exclamations("Hi! !") == 1
assert count_exclamations("Hi?!") == 0
assert count_exclamations("Hi.!") == 0
assert count_exclamations("a! b! c!") == 3
assert count_exclamations("a! b! c") == 2
assert count_exclamations("a!b!c!") == 3
assert count_exclamations("   !") == 0
assert count_exclamations("a ?") == 0
assert count_exclamations("What?! No!") == 1
assert count_exclamations("x! " * 50000) == 50000
assert count_exclamations("!" * 100000) == 0
import random, re
random.seed(52)
for _ in range(300):
    t = "".join(random.choice("ab .?!") for _ in range(random.randint(0, 25)))
    exp = 0
    for m in re.finditer(r"([^.?!]*)([.?!])", t):
        if m.group(2) == "!" and m.group(1).strip():
            exp += 1
    assert count_exclamations(t) == exp, t
''')

add(91, '''def count_sentences_starting_with(S, word):
    """
    You'll be given a string of words and a word, and your task is to count the number
    of sentences whose first word is exactly the given word (case sensitive, a longer word
    that only starts with the same letters does not count).
    Sentences are delimited by '.', '?' or '!'. Words are separated by whitespace.

    For example:
    >>> count_sentences_starting_with("I am here. It is nice. I like it", "I")
    2
    >>> count_sentences_starting_with("Hello world", "Hello")
    1
    >>> count_sentences_starting_with("", "I")
    0
    """
''', '''
    count = 0
    for sentence in S.replace("?", ".").replace("!", ".").split("."):
        words = sentence.split()
        if words and words[0] == word:
            count += 1
    return count
''', '''
assert count_sentences_starting_with("I am here. It is nice. I like it", "I") == 2
assert count_sentences_starting_with("Hello world", "Hello") == 1
assert count_sentences_starting_with("", "I") == 0
assert count_sentences_starting_with("I", "I") == 1
assert count_sentences_starting_with("I.", "I") == 1
assert count_sentences_starting_with("It is. Is it", "I") == 0
assert count_sentences_starting_with("i am. I am", "I") == 1
assert count_sentences_starting_with("  I am!   I do? I", "I") == 3
assert count_sentences_starting_with("We go. we stay. We", "We") == 2
assert count_sentences_starting_with("a b. a c. b a", "a") == 2
assert count_sentences_starting_with("a b. a c. b a", "b") == 1
assert count_sentences_starting_with("The the. the", "the") == 1
assert count_sentences_starting_with("x\\ty. x\\nz", "x") == 2
assert count_sentences_starting_with("Hi there! Hi?", "Hi") == 2
assert count_sentences_starting_with("..! ?", "I") == 0
assert count_sentences_starting_with("I. " * 50000, "I") == 50000
assert count_sentences_starting_with("Im. " * 50000, "I") == 0
import random, re
random.seed(53)
for _ in range(300):
    t = "".join(random.choice("Ia b.?!") for _ in range(random.randint(0, 25)))
    exp = sum(1 for p in re.split(r"[.?!]", t) if p.split()[:1] == ["I"])
    assert count_sentences_starting_with(t, "I") == exp, t
''')

add(91, '''def longest_sentence(S):
    """
    You'll be given a string of words, and your task is to find the sentence with the most words.
    Sentences are delimited by '.', '?' or '!'. Words are separated by whitespace.
    Return the sentence without the delimiter and without spaces around it. If several sentences
    have the same number of words, return the first one. Return an empty string if there are no words.

    For example:
    >>> longest_sentence("Hello world")
    'Hello world'
    >>> longest_sentence("Hi. The sky is blue! I love it")
    'The sky is blue'
    >>> longest_sentence("...")
    ''
    """
''', '''
    best = ""
    best_words = 0
    for sentence in S.replace("?", ".").replace("!", ".").split("."):
        n = len(sentence.split())
        if n > best_words:
            best_words = n
            best = sentence.strip()
    return best
''', '''
assert longest_sentence("") == ""
assert longest_sentence("...") == ""
assert longest_sentence("   ") == ""
assert longest_sentence("Hello world") == "Hello world"
assert longest_sentence("Hi. The sky is blue! I love it") == "The sky is blue"
assert longest_sentence("a b. c d. e") == "a b"
assert longest_sentence("a. b c. d e f") == "d e f"
assert longest_sentence("  spaced   out  words  . x") == "spaced   out  words"
assert longest_sentence("a!b?c.") == "a"
assert longest_sentence("one two. three four five? six") == "three four five"
assert longest_sentence("x") == "x"
assert longest_sentence(" . x . ") == "x"
assert longest_sentence("a\\tb c. d e") == "a\\tb c"
assert longest_sentence("one. two three. four five. six seven eight nine.") == "six seven eight nine"
assert longest_sentence("w " * 100000 + ". a") == ("w " * 100000).strip()
import random, re
random.seed(54)
for _ in range(300):
    t = "".join(random.choice("ab .?!") for _ in range(random.randint(0, 25)))
    parts = re.split(r"[.?!]", t)
    best, bn = "", 0
    for p in parts:
        if len(p.split()) > bn:
            bn, best = len(p.split()), p.strip()
    assert longest_sentence(t) == best, t
''')

add(91, '''def count_sentences_with_word(S, word):
    """
    You'll be given a string of words and a word, and your task is to count the number
    of sentences that contain the given word at least once (case sensitive, only whole words
    count, so "I" is not found inside "It"). Sentences are delimited by '.', '?' or '!'.
    Words are separated by whitespace.

    For example:
    >>> count_sentences_with_word("I am here. It is nice. Me and I", "I")
    2
    >>> count_sentences_with_word("Hello world", "world")
    1
    >>> count_sentences_with_word("", "I")
    0
    """
''', '''
    count = 0
    for sentence in S.replace("?", ".").replace("!", ".").split("."):
        if word in sentence.split():
            count += 1
    return count
''', '''
assert count_sentences_with_word("I am here. It is nice. Me and I", "I") == 2
assert count_sentences_with_word("Hello world", "world") == 1
assert count_sentences_with_word("", "I") == 0
assert count_sentences_with_word("I I I. I", "I") == 2
assert count_sentences_with_word("It is. Is it", "I") == 0
assert count_sentences_with_word("a b. b a! c", "b") == 2
assert count_sentences_with_word("a b. b a! c", "c") == 1
assert count_sentences_with_word("a b. b a! c", "d") == 0
assert count_sentences_with_word("world. worlds. hello world", "world") == 2
assert count_sentences_with_word("Cat. cat", "cat") == 1
assert count_sentences_with_word("x\\ty. y\\nx", "x") == 2
assert count_sentences_with_word("...", "a") == 0
assert count_sentences_with_word("a,b c", "a") == 0
assert count_sentences_with_word("a,b c", "a,b") == 1
assert count_sentences_with_word("go. " * 50000, "go") == 50000
assert count_sentences_with_word("going. " * 50000, "go") == 0
import random, re
random.seed(55)
for _ in range(300):
    t = "".join(random.choice("Ia b.?!") for _ in range(random.randint(0, 25)))
    exp = sum(1 for p in re.split(r"[.?!]", t) if "a" in p.split())
    assert count_sentences_with_word(t, "a") == exp, t
''')

# ---------------------------------------------------------------- HumanEval/93
add(93, '''def encode_vowels_back(message):
    """
    Write a function that takes a message, and encodes in such a
    way that it swaps case of all letters, replaces all vowels in
    the message with the letter that appears 2 places before that
    vowel in the english alphabet (the alphabet is cyclic, so 'a' goes to 'y').
    Assume only letters.

    Examples:
    >>> encode_vowels_back('test')
    'TCST'
    >>> encode_vowels_back('This is a message')
    'tHGS GS Y MCSSYGC'
    """
''', '''
    def switch_case(ch):
        return ch.swapcase()

    def vowel_change(ch):
        if ch in "aeiouAEIOU":
            base = ord("a") if ch.islower() else ord("A")
            return chr((ord(ch) - base - 2) % 26 + base)
        return ch

    return "".join(vowel_change(switch_case(ch)) for ch in message)
''', '''
assert encode_vowels_back("") == ""
assert encode_vowels_back("test") == "TCST"
assert encode_vowels_back("a") == "Y"
assert encode_vowels_back("A") == "y"
assert encode_vowels_back("e") == "C"
assert encode_vowels_back("i") == "G"
assert encode_vowels_back("o") == "M"
assert encode_vowels_back("u") == "S"
assert encode_vowels_back("AEIOU") == "ycgms"
assert encode_vowels_back("aeiou") == "YCGMS"
assert encode_vowels_back("xyz") == "XYZ"
assert encode_vowels_back("bcd") == "BCD"
assert encode_vowels_back("This is a message") == "tHGS GS Y MCSSYGC"
assert encode_vowels_back("Hello World") == "hCLLM wMRLD"
assert encode_vowels_back("Python") == "pYTHMN"
assert encode_vowels_back("QUEUE") == "qscsc"
vm = {"a": "y", "e": "c", "i": "g", "o": "m", "u": "s"}
import random
random.seed(61)
for _ in range(300):
    t = "".join(random.choice("abcdeiouAEIOUxyzXYZ ") for _ in range(random.randint(0, 20)))
    exp = ""
    for ch in t:
        sw = ch.swapcase()
        if sw in "aeiouAEIOU":
            sw = vm[sw.lower()] if sw.islower() else vm[sw.lower()].upper()
        exp += sw
    assert encode_vowels_back(t) == exp, t
assert len(encode_vowels_back("ab" * 100000)) == 200000
''')

add(93, '''def encode_caesar(message, shift):
    """
    Write a function that takes a message and an integer shift, and encodes the message
    in such a way that every letter is replaced by the letter that appears shift places
    after it in the english alphabet. The alphabet is cyclic, the case of letters is kept,
    shift may be negative or larger than 26, and characters that are not letters stay unchanged.

    Examples:
    >>> encode_caesar('abc', 1)
    'bcd'
    >>> encode_caesar('Hello, World!', 3)
    'Khoor, Zruog!'
    >>> encode_caesar('xyz', -3)
    'uvw'
    """
''', '''
    res = []
    for ch in message:
        if "a" <= ch <= "z":
            res.append(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= ch <= "Z":
            res.append(chr((ord(ch) - ord("A") + shift) % 26 + ord("A")))
        else:
            res.append(ch)
    return "".join(res)
''', '''
assert encode_caesar("", 5) == ""
assert encode_caesar("abc", 1) == "bcd"
assert encode_caesar("Hello, World!", 3) == "Khoor, Zruog!"
assert encode_caesar("xyz", -3) == "uvw"
assert encode_caesar("xyz", 3) == "abc"
assert encode_caesar("XYZ", 3) == "ABC"
assert encode_caesar("abc", 0) == "abc"
assert encode_caesar("abc", 26) == "abc"
assert encode_caesar("abc", -26) == "abc"
assert encode_caesar("abc", 27) == "bcd"
assert encode_caesar("abc", -27) == "zab"
assert encode_caesar("abc", 52 * 1000 + 2) == "cde"
assert encode_caesar("a1 b2-c3", 1) == "b1 c2-d3"
assert encode_caesar("zZ", 1) == "aA"
assert encode_caesar("aA", -1) == "zZ"
assert encode_caesar("\\n\\t ~", 7) == "\\n\\t ~"
assert encode_caesar("é", 3) == "é"
import random
random.seed(62)
for _ in range(300):
    t = "".join(random.choice("abzAZ 1!") for _ in range(random.randint(0, 20)))
    k = random.randint(-100, 100)
    r = encode_caesar(t, k)
    assert len(r) == len(t)
    assert encode_caesar(r, -k) == t
    assert encode_caesar(t, k + 26) == r
assert encode_caesar("a" * 200000, 25) == "z" * 200000
''')

add(93, '''def mask_vowels(message):
    """
    Write a function that takes a message, and encodes in such a
    way that it swaps case of all letters and replaces all vowels
    (a, e, i, o, u in any case) in the message with the character '*'.
    Characters that are not letters stay unchanged.

    Examples:
    >>> mask_vowels('test')
    'T*ST'
    >>> mask_vowels('This is a message')
    'tH*S *S * M*SS*G*'
    """
''', '''
    res = []
    for ch in message:
        if ch in "aeiouAEIOU":
            res.append("*")
        else:
            res.append(ch.swapcase())
    return "".join(res)
''', '''
assert mask_vowels("") == ""
assert mask_vowels("test") == "T*ST"
assert mask_vowels("This is a message") == "tH*S *S * M*SS*G*"
assert mask_vowels("aeiou") == "*****"
assert mask_vowels("AEIOU") == "*****"
assert mask_vowels("bcd") == "BCD"
assert mask_vowels("BCD") == "bcd"
assert mask_vowels("Hello, World!") == "h*LL*, w*RLD!"
assert mask_vowels("123") == "123"
assert mask_vowels("y") == "Y"
assert mask_vowels("Y") == "y"
assert mask_vowels("*") == "*"
assert mask_vowels("Programming Is Fun") == "pR*GR*MM*NG *S f*N"
assert mask_vowels("AbEcIdOfU") == "*B*C*D*F*"
import random
random.seed(63)
for _ in range(300):
    t = "".join(random.choice("abcdeAEIOUxyz 1") for _ in range(random.randint(0, 20)))
    r = mask_vowels(t)
    assert len(r) == len(t)
    assert all((c == "*") == (o in "aeiouAEIOU") for c, o in zip(r, t))
    assert all(c == o.swapcase() for c, o in zip(r, t) if o not in "aeiouAEIOU")
assert mask_vowels("ab" * 100000) == "*B" * 100000
''')

add(93, '''def rotate_vowels(message):
    """
    Write a function that takes a message, and encodes in such a
    way that every vowel is replaced by the next vowel in the cycle
    a -> e -> i -> o -> u -> a. The case of every letter is kept and
    all other characters stay unchanged.

    Examples:
    >>> rotate_vowels('test')
    'tist'
    >>> rotate_vowels('This is a message')
    'Thos os e missegi'
    >>> rotate_vowels('Aeiou')
    'Eioua'
    """
''', '''
    nxt = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"}
    res = []
    for ch in message:
        low = ch.lower()
        if low in nxt and ch.isalpha():
            new = nxt[low]
            res.append(new.upper() if ch.isupper() else new)
        else:
            res.append(ch)
    return "".join(res)
''', '''
assert rotate_vowels("") == ""
assert rotate_vowels("test") == "tist"
assert rotate_vowels("This is a message") == "Thos os e missegi"
assert rotate_vowels("Aeiou") == "Eioua"
assert rotate_vowels("aeiou") == "eioua"
assert rotate_vowels("AEIOU") == "EIOUA"
assert rotate_vowels("u") == "a"
assert rotate_vowels("U") == "A"
assert rotate_vowels("bcd") == "bcd"
assert rotate_vowels("xyz XYZ") == "xyz XYZ"
assert rotate_vowels("123 !?") == "123 !?"
assert rotate_vowels("Hello World") == "Hillu Wurld"
assert rotate_vowels("rhythm") == "rhythm"
assert rotate_vowels("UuAa") == "AaEe"
import random
random.seed(64)
for _ in range(300):
    t = "".join(random.choice("abcdeiouAEIOUxyz 1") for _ in range(random.randint(0, 20)))
    r = rotate_vowels(t)
    assert len(r) == len(t)
    s = t
    for _ in range(5):
        s = rotate_vowels(s)
    assert s == t
    assert all(a == b for a, b in zip(r, t) if b not in "aeiouAEIOU")
    assert all(a in "aeiouAEIOU" for a, b in zip(r, t) if b in "aeiouAEIOU")
assert rotate_vowels("a" * 200000) == "e" * 200000
''')

add(93, '''def swap_and_reverse_words(message):
    """
    Write a function that takes a message, and encodes in such a
    way that it swaps case of all letters and writes every word
    (separated by single spaces) backwards. The order of the words is kept.
    Characters that are not letters stay unchanged.

    Examples:
    >>> swap_and_reverse_words('test')
    'TSET'
    >>> swap_and_reverse_words('This is a message')
    'SIHt SI A EGASSEM'
    """
''', '''
    return " ".join(word[::-1].swapcase() for word in message.split(" "))
''', '''
assert swap_and_reverse_words("") == ""
assert swap_and_reverse_words("test") == "TSET"
assert swap_and_reverse_words("This is a message") == "SIHt SI A EGASSEM"
assert swap_and_reverse_words("a") == "A"
assert swap_and_reverse_words("A b") == "a B"
assert swap_and_reverse_words("ab cd") == "BA DC"
assert swap_and_reverse_words(" ") == " "
assert swap_and_reverse_words("a  b") == "A  B"
assert swap_and_reverse_words(" ab ") == " BA "
assert swap_and_reverse_words("Hello, World!") == ",OLLEh !DLROw"
assert swap_and_reverse_words("123 abc") == "321 CBA"
assert swap_and_reverse_words("aBc") == "CbA"
assert swap_and_reverse_words("x" * 5 + " " + "Y" * 5) == "X" * 5 + " " + "y" * 5
import random
random.seed(65)
for _ in range(300):
    t = "".join(random.choice("abAB1 ") for _ in range(random.randint(0, 20)))
    r = swap_and_reverse_words(t)
    assert len(r) == len(t)
    assert swap_and_reverse_words(r) == t
    assert [i for i, c in enumerate(r) if c == " "] == [i for i, c in enumerate(t) if c == " "]
assert swap_and_reverse_words("ab " * 60000) == "BA " * 60000
''')

# ---------------------------------------------------------------- HumanEval/96
add(96, '''def count_primes_below(n):
    """Implement a function that takes a non-negative integer and returns the number
    of prime numbers that are less than n.
    for example:
    count_primes_below(5) => 2
    count_primes_below(11) => 4
    count_primes_below(0) => 0
    count_primes_below(20) => 8
    count_primes_below(1) => 0
    count_primes_below(2) => 0
    """
''', '''
    if n < 3:
        return 0
    sieve = bytearray([1]) * n
    sieve[0] = sieve[1] = 0
    i = 2
    while i * i < n:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n, i)))
        i += 1
    return sum(sieve)
''', '''
def slow(n):
    return sum(1 for k in range(2, n) if all(k % d for d in range(2, int(k ** 0.5) + 1)))
assert count_primes_below(0) == 0
assert count_primes_below(1) == 0
assert count_primes_below(2) == 0
assert count_primes_below(3) == 1
assert count_primes_below(4) == 2
assert count_primes_below(5) == 2
assert count_primes_below(6) == 3
assert count_primes_below(11) == 4
assert count_primes_below(12) == 5
assert count_primes_below(20) == 8
assert count_primes_below(100) == 25
assert count_primes_below(101) == 25
assert count_primes_below(102) == 26
assert count_primes_below(1000) == 168
assert count_primes_below(10 ** 4) == 1229
assert count_primes_below(10 ** 5) == 9592
assert count_primes_below(10 ** 6) == 78498
assert count_primes_below(10 ** 7) == 664579
for n in range(0, 600):
    assert count_primes_below(n) == slow(n), n
''')

add(96, '''def primes_between(a, b):
    """Implement a function that takes two non-negative integers a and b and returns an array
    of all prime numbers p with a <= p <= b in ascending order. If a is greater than b, return
    an empty array.
    for example:
    primes_between(2, 11) => [2,3,5,7,11]
    primes_between(8, 10) => []
    primes_between(0, 1) => []
    primes_between(10, 2) => []
    primes_between(13, 13) => [13]
    """
''', '''
    if a > b or b < 2:
        return []
    a = max(a, 2)
    sieve = bytearray([1]) * (b + 1)
    sieve[0] = sieve[1] = 0
    i = 2
    while i * i <= b:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, b + 1, i)))
        i += 1
    return [k for k in range(a, b + 1) if sieve[k]]
''', '''
def isp(k):
    return k > 1 and all(k % d for d in range(2, int(k ** 0.5) + 1))
assert primes_between(2, 11) == [2, 3, 5, 7, 11]
assert primes_between(8, 10) == []
assert primes_between(0, 1) == []
assert primes_between(0, 0) == []
assert primes_between(10, 2) == []
assert primes_between(13, 13) == [13]
assert primes_between(14, 14) == []
assert primes_between(0, 2) == [2]
assert primes_between(1, 3) == [2, 3]
assert primes_between(2, 2) == [2]
assert primes_between(3, 2) == []
assert primes_between(90, 100) == [97]
assert primes_between(1, 30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert primes_between(24, 28) == []
assert len(primes_between(0, 10 ** 6)) == 78498
assert primes_between(10 ** 6 - 100, 10 ** 6) == [999907, 999917, 999931, 999953, 999959, 999961, 999979, 999983]
for a in range(0, 40):
    for b in range(0, 60):
        assert primes_between(a, b) == [k for k in range(a, b + 1) if isp(k)], (a, b)
''')

add(96, '''def largest_prime_below(n):
    """Implement a function that takes a non-negative integer n and returns the largest prime
    number that is strictly less than n. If there is no such prime, return -1.
    for example:
    largest_prime_below(10) => 7
    largest_prime_below(3) => 2
    largest_prime_below(2) => -1
    largest_prime_below(0) => -1
    largest_prime_below(100) => 97
    """
''', '''
    def is_prime(m):
        if m < 2:
            return False
        if m % 2 == 0:
            return m == 2
        d = 3
        while d * d <= m:
            if m % d == 0:
                return False
            d += 2
        return True

    k = n - 1
    while k >= 2:
        if is_prime(k):
            return k
        k -= 1
    return -1
''', '''
assert largest_prime_below(0) == -1
assert largest_prime_below(1) == -1
assert largest_prime_below(2) == -1
assert largest_prime_below(3) == 2
assert largest_prime_below(4) == 3
assert largest_prime_below(5) == 3
assert largest_prime_below(6) == 5
assert largest_prime_below(10) == 7
assert largest_prime_below(14) == 13
assert largest_prime_below(100) == 97
assert largest_prime_below(98) == 97
assert largest_prime_below(97) == 89
assert largest_prime_below(1000) == 997
assert largest_prime_below(10 ** 6) == 999983
assert largest_prime_below(10 ** 9) == 999999937
assert largest_prime_below(10 ** 10) == 9999999967
assert largest_prime_below(1000000007) == 999999937
assert largest_prime_below(2 ** 31) == 2147483647
assert largest_prime_below(2 ** 31 - 1) == 2147483629
def isp(k):
    return k > 1 and all(k % d for d in range(2, int(k ** 0.5) + 1))
for n in range(0, 400):
    exp = max([k for k in range(2, n) if isp(k)], default=-1)
    assert largest_prime_below(n) == exp, n
''')

add(96, '''def twin_primes_below(n):
    """Implement a function that takes a non-negative integer n and returns an array of the pairs
    (p, p+2) where both p and p+2 are prime numbers and p+2 is less than n.
    The pairs are listed in ascending order.
    for example:
    twin_primes_below(14) => [(3, 5), (5, 7), (11, 13)]
    twin_primes_below(6) => [(3, 5)]
    twin_primes_below(5) => []
    twin_primes_below(0) => []
    """
''', '''
    if n < 6:
        return []
    sieve = bytearray([1]) * n
    sieve[0] = sieve[1] = 0
    i = 2
    while i * i < n:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n, i)))
        i += 1
    return [(p, p + 2) for p in range(2, n - 2) if sieve[p] and sieve[p + 2]]
''', '''
def isp(k):
    return k > 1 and all(k % d for d in range(2, int(k ** 0.5) + 1))
assert twin_primes_below(0) == []
assert twin_primes_below(1) == []
assert twin_primes_below(5) == []
assert twin_primes_below(6) == [(3, 5)]
assert twin_primes_below(14) == [(3, 5), (5, 7), (11, 13)]
assert twin_primes_below(13) == [(3, 5), (5, 7)]
assert twin_primes_below(7) == [(3, 5)]
assert twin_primes_below(8) == [(3, 5), (5, 7)]
assert twin_primes_below(100) == [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)]
assert len(twin_primes_below(10 ** 6)) == 8169
assert twin_primes_below(10 ** 6)[-1] == (999959, 999961)
for n in range(0, 300):
    exp = [(p, p + 2) for p in range(2, n) if p + 2 < n and isp(p) and isp(p + 2)]
    assert twin_primes_below(n) == exp, n
''')

add(96, '''def sum_primes_below(n):
    """Implement a function that takes a non-negative integer n and returns the sum
    of all prime numbers that are less than n.
    for example:
    sum_primes_below(5) => 5
    sum_primes_below(11) => 17
    sum_primes_below(0) => 0
    sum_primes_below(20) => 77
    sum_primes_below(2) => 0
    """
''', '''
    if n < 3:
        return 0
    sieve = bytearray([1]) * n
    sieve[0] = sieve[1] = 0
    i = 2
    while i * i < n:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n, i)))
        i += 1
    return sum(k for k in range(n) if sieve[k])
''', '''
def isp(k):
    return k > 1 and all(k % d for d in range(2, int(k ** 0.5) + 1))
assert sum_primes_below(0) == 0
assert sum_primes_below(1) == 0
assert sum_primes_below(2) == 0
assert sum_primes_below(3) == 2
assert sum_primes_below(4) == 5
assert sum_primes_below(5) == 5
assert sum_primes_below(6) == 10
assert sum_primes_below(11) == 17
assert sum_primes_below(12) == 28
assert sum_primes_below(20) == 77
assert sum_primes_below(100) == 1060
assert sum_primes_below(1000) == 76127
assert sum_primes_below(10 ** 5) == 454396537
assert sum_primes_below(2 * 10 ** 6) == 142913828922
for n in range(0, 300):
    assert sum_primes_below(n) == sum(k for k in range(n) if isp(k)), n
''')
