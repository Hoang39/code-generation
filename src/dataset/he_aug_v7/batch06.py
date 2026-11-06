# parents: HumanEval/144 (simplify), /145 (order_by_points), /156 (int_to_mini_roman), /163 (generate_integers)
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------------------------------------------------------- HumanEval/144
add(144, '''def simplify_sum(x, n):
    """Return True if the expression x + n evaluates to a whole number and False otherwise.
    Both x and n are strings of the form <numerator>/<denominator> where both parts are
    positive whole numbers (no zero denominators).

    simplify_sum("1/2", "1/2") = True
    simplify_sum("1/3", "1/6") = False
    simplify_sum("3/4", "5/4") = True
    """
''', '''
    x1, x2 = map(int, x.split("/"))
    n1, n2 = map(int, n.split("/"))
    return (x1 * n2 + n1 * x2) % (x2 * n2) == 0
''', '''
from fractions import Fraction
import random
def ref(x, n):
    return (Fraction(x) + Fraction(n)).denominator == 1
assert simplify_sum("1/2", "1/2") is True
assert simplify_sum("1/3", "1/6") is False
assert simplify_sum("3/4", "5/4") is True
assert simplify_sum("1/1", "1/1") is True
assert simplify_sum("1/2", "1/3") is False
assert simplify_sum("2/3", "1/3") is True
assert simplify_sum("1/3", "1/3") is False
assert simplify_sum("5/3", "4/3") is True
assert simplify_sum("7/2", "3/2") is True
assert simplify_sum("7/2", "4/2") is False
assert simplify_sum("10/5", "6/3") is True
assert simplify_sum("1/4", "1/4") is False
assert simplify_sum("1/6", "5/6") is True
assert simplify_sum("1000000007/3", "2/3") is False
assert simplify_sum("1000000000/3", "2/3") is True
assert simplify_sum("1/999999999999", "999999999998/999999999999") is True
assert simplify_sum("1/999999999999", "999999999997/999999999999") is False
assert simplify_sum("123456789123456789/1", "987654321987654321/1") is True
random.seed(81)
for _ in range(2000):
    a, b, c, d = (random.randint(1, 30) for _ in range(4))
    x, n = "%d/%d" % (a, b), "%d/%d" % (c, d)
    assert simplify_sum(x, n) == ref(x, n), (x, n)
''')

add(144, '''def simplify_quotient(x, n):
    """Return True if the expression x / n evaluates to a whole number and False otherwise.
    Both x and n are strings of the form <numerator>/<denominator> where both parts are
    positive whole numbers (no zero denominators).

    simplify_quotient("1/2", "1/4") = True
    simplify_quotient("1/4", "1/2") = False
    simplify_quotient("6/5", "3/10") = True
    """
''', '''
    x1, x2 = map(int, x.split("/"))
    n1, n2 = map(int, n.split("/"))
    return (x1 * n2) % (x2 * n1) == 0
''', '''
from fractions import Fraction
import random
def ref(x, n):
    return (Fraction(x) / Fraction(n)).denominator == 1
assert simplify_quotient("1/2", "1/4") is True
assert simplify_quotient("1/4", "1/2") is False
assert simplify_quotient("6/5", "3/10") is True
assert simplify_quotient("1/1", "1/1") is True
assert simplify_quotient("1/2", "1/2") is True
assert simplify_quotient("3/1", "3/1") is True
assert simplify_quotient("2/1", "3/1") is False
assert simplify_quotient("6/1", "3/1") is True
assert simplify_quotient("3/1", "6/1") is False
assert simplify_quotient("5/7", "5/7") is True
assert simplify_quotient("10/3", "5/6") is True
assert simplify_quotient("5/6", "10/3") is False
assert simplify_quotient("7/2", "7/4") is True
assert simplify_quotient("1000000007/1", "1/1000000007") is True
assert simplify_quotient("1/1000000007", "1000000007/1") is False
assert simplify_quotient("999999999999/7", "999999999999/49") is True
assert simplify_quotient("4/6", "2/3") is True
random.seed(82)
for _ in range(2000):
    a, b, c, d = (random.randint(1, 30) for _ in range(4))
    x, n = "%d/%d" % (a, b), "%d/%d" % (c, d)
    assert simplify_quotient(x, n) == ref(x, n), (x, n)
''')

add(144, '''def product_fraction(x, n):
    """Multiply the fractions x * n and return the result in lowest terms as a string
    <numerator>/<denominator> (a whole number has denominator 1). Both x and n are strings
    of the form <numerator>/<denominator> with positive whole numbers and no zero denominator.

    product_fraction("1/5", "5/1") = "1/1"
    product_fraction("1/6", "2/1") = "1/3"
    product_fraction("7/10", "10/2") = "7/2"
    """
''', '''
    from math import gcd

    x1, x2 = map(int, x.split("/"))
    n1, n2 = map(int, n.split("/"))
    num, den = x1 * n1, x2 * n2
    g = gcd(num, den)
    return str(num // g) + "/" + str(den // g)
''', '''
from fractions import Fraction
import random
def ref(x, n):
    f = Fraction(x) * Fraction(n)
    return "%d/%d" % (f.numerator, f.denominator)
assert product_fraction("1/5", "5/1") == "1/1"
assert product_fraction("1/6", "2/1") == "1/3"
assert product_fraction("7/10", "10/2") == "7/2"
assert product_fraction("1/1", "1/1") == "1/1"
assert product_fraction("2/4", "2/4") == "1/4"
assert product_fraction("3/4", "4/3") == "1/1"
assert product_fraction("6/1", "5/1") == "30/1"
assert product_fraction("1/2", "1/3") == "1/6"
assert product_fraction("10/3", "9/5") == "6/1"
assert product_fraction("12/18", "9/8") == "3/4"
assert product_fraction("100/1", "1/100") == "1/1"
assert product_fraction("1000000007/3", "3/1000000007") == "1/1"
assert product_fraction("999999999999/1", "1/999999999999") == "1/1"
assert product_fraction("10000000000/3", "3/20000000000") == "1/2"
assert product_fraction("8/12", "3/2") == "1/1"
assert product_fraction("5/5", "5/5") == "1/1"
assert product_fraction("2/3", "3/2") == "1/1"
random.seed(83)
for _ in range(2000):
    a, b, c, d = (random.randint(1, 40) for _ in range(4))
    x, n = "%d/%d" % (a, b), "%d/%d" % (c, d)
    assert product_fraction(x, n) == ref(x, n), (x, n)
''')

add(144, '''def fraction_less(x, n):
    """Your task is to implement a function that compares two fractions.
    The function returns True if x is strictly less than n and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    fraction_less("1/5", "1/4") = True
    fraction_less("1/4", "1/5") = False
    fraction_less("2/4", "1/2") = False
    """
''', '''
    x1, x2 = map(int, x.split("/"))
    n1, n2 = map(int, n.split("/"))
    return x1 * n2 < n1 * x2
''', '''
from fractions import Fraction
import random
assert fraction_less("1/5", "1/4") is True
assert fraction_less("1/4", "1/5") is False
assert fraction_less("2/4", "1/2") is False
assert fraction_less("1/2", "2/4") is False
assert fraction_less("1/1", "1/1") is False
assert fraction_less("1/3", "2/3") is True
assert fraction_less("2/3", "1/3") is False
assert fraction_less("3/1", "7/2") is True
assert fraction_less("7/2", "3/1") is False
assert fraction_less("1/1000000007", "1/1000000006") is True
assert fraction_less("1/1000000006", "1/1000000007") is False
assert fraction_less("999999999998/999999999999", "999999999999/1000000000000") is True
assert fraction_less("999999999999/1000000000000", "999999999998/999999999999") is False
assert fraction_less("10/3", "13/4") is False
assert fraction_less("13/4", "10/3") is True
assert fraction_less("5/10", "1/2") is False
random.seed(84)
for _ in range(3000):
    a, b, c, d = (random.randint(1, 25) for _ in range(4))
    x, n = "%d/%d" % (a, b), "%d/%d" % (c, d)
    assert fraction_less(x, n) == (Fraction(x) < Fraction(n)), (x, n)
''')

add(144, '''def is_reducible(x):
    """Your task is to implement a function that checks whether a fraction can be reduced.
    The function returns True if the numerator and the denominator of x have a common divisor
    greater than 1 and False otherwise. The argument x is a string representation of a fraction,
    and has the following format, <numerator>/<denominator> where both numerator and denominator
    are positive whole numbers.

    You can assume that x is a valid fraction and does not have zero as denominator.

    is_reducible("2/4") = True
    is_reducible("3/7") = False
    is_reducible("5/1") = False
    is_reducible("6/6") = True
    """
''', '''
    from math import gcd

    a, b = map(int, x.split("/"))
    return gcd(a, b) > 1
''', '''
from fractions import Fraction
import random
assert is_reducible("2/4") is True
assert is_reducible("3/7") is False
assert is_reducible("5/1") is False
assert is_reducible("6/6") is True
assert is_reducible("1/1") is False
assert is_reducible("1/2") is False
assert is_reducible("4/2") is True
assert is_reducible("2/2") is True
assert is_reducible("9/12") is True
assert is_reducible("13/26") is True
assert is_reducible("13/27") is False
assert is_reducible("1/1000000007") is False
assert is_reducible("1000000007/1000000007") is True
assert is_reducible("1000000007/2000000014") is True
assert is_reducible("999999999999/1000000000000") is False
assert is_reducible("100/1") is False
assert is_reducible("100/10") is True
assert is_reducible("35/64") is False
random.seed(85)
for _ in range(3000):
    a, b = random.randint(1, 60), random.randint(1, 60)
    s = "%d/%d" % (a, b)
    assert is_reducible(s) == (Fraction(a, b).denominator != b), s
''')

# ---------------------------------------------------------------- HumanEval/145
add(145, '''def order_by_digit_count(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the number of their digits
    (the sign is not a digit, and 0 has one digit).
    Note: if there are several items with the same number of digits,
    order them based on their index in original list.

    For example:
    >>> order_by_digit_count([100, 5, -22, 7, 1000, -3]) == [5, 7, -3, -22, 100, 1000]
    >>> order_by_digit_count([]) == []
    """
''', '''
    return sorted(nums, key=lambda x: len(str(abs(x))))
''', '''
import random
assert order_by_digit_count([100, 5, -22, 7, 1000, -3]) == [5, 7, -3, -22, 100, 1000]
assert order_by_digit_count([]) == []
assert order_by_digit_count([0]) == [0]
assert order_by_digit_count([10, 0, -1]) == [0, -1, 10]
assert order_by_digit_count([-10, 10, 9, -9]) == [9, -9, -10, 10]
assert order_by_digit_count([99, 100, 1]) == [1, 99, 100]
assert order_by_digit_count([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
assert order_by_digit_count([-1000, 999, -99, 9]) == [9, -99, 999, -1000]
assert order_by_digit_count([10 ** 18, 10 ** 17, -10 ** 16]) == [-10 ** 16, 10 ** 17, 10 ** 18]
assert order_by_digit_count([22, 11, -33, 44]) == [22, 11, -33, 44]
assert order_by_digit_count([123, -45, 6, 7890]) == [6, -45, 123, 7890]
a = [30, 4, 200]
order_by_digit_count(a)
assert a == [30, 4, 200]
random.seed(86)
for _ in range(300):
    L = [random.randint(-2000, 2000) for _ in range(random.randint(0, 15))]
    r = order_by_digit_count(L)
    assert sorted(r) == sorted(L)
    exp = [v for _, _, v in sorted((len(str(abs(v))), i, v) for i, v in enumerate(L))]
    assert r == exp
big = [random.randint(-10 ** 9, 10 ** 9) for _ in range(100000)]
r = order_by_digit_count(big)
assert all(len(str(abs(r[i]))) <= len(str(abs(r[i + 1]))) for i in range(0, len(r) - 1, 97))
''')

add(145, '''def order_by_last_digit(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the last digit of their absolute value.
    Note: if there are several items with the same last digit,
    order them based on their index in original list.

    For example:
    >>> order_by_last_digit([19, 21, -13, 40, 5]) == [40, 21, -13, 5, 19]
    >>> order_by_last_digit([]) == []
    """
''', '''
    return sorted(nums, key=lambda x: abs(x) % 10)
''', '''
import random
assert order_by_last_digit([19, 21, -13, 40, 5]) == [40, 21, -13, 5, 19]
assert order_by_last_digit([]) == []
assert order_by_last_digit([0]) == [0]
assert order_by_last_digit([-1, 1, -11, 11]) == [-1, 1, -11, 11]
assert order_by_last_digit([-9, 19, 8, -18]) == [8, -18, -9, 19]
assert order_by_last_digit([10, 20, 30]) == [10, 20, 30]
assert order_by_last_digit([21, 12, 3]) == [21, 12, 3]
assert order_by_last_digit([-5, 5, 15, -15]) == [-5, 5, 15, -15]
assert order_by_last_digit([-10, 9]) == [-10, 9]
assert order_by_last_digit([-19, -20]) == [-20, -19]
assert order_by_last_digit([100, -101, 102]) == [100, -101, 102]
assert order_by_last_digit([10 ** 18 + 3, 10 ** 18 + 1]) == [10 ** 18 + 1, 10 ** 18 + 3]
a = [32, 11]
order_by_last_digit(a)
assert a == [32, 11]
random.seed(87)
for _ in range(300):
    L = [random.randint(-300, 300) for _ in range(random.randint(0, 15))]
    exp = [v for _, _, v in sorted((abs(v) % 10, i, v) for i, v in enumerate(L))]
    assert order_by_last_digit(L) == exp
big = [random.randint(-10 ** 9, 10 ** 9) for _ in range(100000)]
r = order_by_last_digit(big)
assert all(abs(r[i]) % 10 <= abs(r[i + 1]) % 10 for i in range(len(r) - 1))
''')

add(145, '''def order_by_points_desc(nums):
    """
    Write a function which sorts the given list of integers
    in descending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.

    For example:
    >>> order_by_points_desc([1, 11, -1, -11, -12]) == [11, 1, -12, -11, -1]
    >>> order_by_points_desc([]) == []
    """
''', '''
    def weight(x):
        digits = [int(c) for c in str(abs(x))]
        if x < 0:
            digits[0] = -digits[0]
        return sum(digits)
    return sorted(nums, key=lambda x: -weight(x))
''', '''
import random
def w(x):
    d = [int(c) for c in str(abs(x))]
    if x < 0:
        d[0] = -d[0]
    return sum(d)
assert order_by_points_desc([1, 11, -1, -11, -12]) == [11, 1, -12, -11, -1]
assert order_by_points_desc([]) == []
assert order_by_points_desc([0]) == [0]
assert order_by_points_desc([5, 14, 23]) == [5, 14, 23]
assert order_by_points_desc([-5, 5]) == [5, -5]
assert order_by_points_desc([-10, 10]) == [10, -10]
assert order_by_points_desc([-19, 19, 28]) == [19, 28, -19]
assert order_by_points_desc([-99, 99]) == [99, -99]
assert order_by_points_desc([-100, 0, 1]) == [1, 0, -100]
assert order_by_points_desc([-91, -81, -71]) == [-71, -81, -91]
assert order_by_points_desc([9, 18, 27, -36]) == [9, 18, 27, -36]
assert order_by_points_desc([1000, 1, -1000]) == [1000, 1, -1000]
a = [3, 1, 2]
order_by_points_desc(a)
assert a == [3, 1, 2]
random.seed(88)
for _ in range(300):
    L = [random.randint(-300, 300) for _ in range(random.randint(0, 15))]
    exp = [v for _, _, v in sorted((-w(v), i, v) for i, v in enumerate(L))]
    assert order_by_points_desc(L) == exp
big = [random.randint(-10 ** 9, 10 ** 9) for _ in range(50000)]
r = order_by_points_desc(big)
assert all(w(r[i]) >= w(r[i + 1]) for i in range(len(r) - 1))
''')

add(145, '''def order_by_abs_digit_sum(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of the digits of their absolute value
    (the sign is ignored, so -12 has the sum 3).
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_abs_digit_sum([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]
    >>> order_by_abs_digit_sum([]) == []
    """
''', '''
    return sorted(nums, key=lambda x: sum(int(c) for c in str(abs(x))))
''', '''
import random
def w(x):
    return sum(int(c) for c in str(abs(x)))
assert order_by_abs_digit_sum([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]
assert order_by_abs_digit_sum([]) == []
assert order_by_abs_digit_sum([0]) == [0]
assert order_by_abs_digit_sum([10, 0, -1]) == [0, 10, -1]
assert order_by_abs_digit_sum([-5, 5]) == [-5, 5]
assert order_by_abs_digit_sum([99, -9, 18, -81]) == [-9, 18, -81, 99]
assert order_by_abs_digit_sum([21, 12, -3, 30]) == [21, 12, -3, 30]
assert order_by_abs_digit_sum([100, 20, -3]) == [100, 20, -3]
assert order_by_abs_digit_sum([-1000, 1001, 2]) == [-1000, 1001, 2]
assert order_by_abs_digit_sum([-19, 10]) == [10, -19]
assert order_by_abs_digit_sum([111, -30, 12]) == [111, -30, 12]
assert order_by_abs_digit_sum([10 ** 18, 999999999999999999]) == [10 ** 18, 999999999999999999]
a = [30, 4, 200]
order_by_abs_digit_sum(a)
assert a == [30, 4, 200]
random.seed(89)
for _ in range(300):
    L = [random.randint(-300, 300) for _ in range(random.randint(0, 15))]
    exp = [v for _, _, v in sorted((w(v), i, v) for i, v in enumerate(L))]
    assert order_by_abs_digit_sum(L) == exp
big = [random.randint(-10 ** 9, 10 ** 9) for _ in range(50000)]
r = order_by_abs_digit_sum(big)
assert all(w(r[i]) <= w(r[i + 1]) for i in range(len(r) - 1))
''')

add(145, '''def rank_by_points(nums):
    """
    Write a function which returns the list of indexes of the given list of integers
    arranged in ascending order according to the sum of the digits of the numbers
    at these indexes.
    Note: if there are several items with similar sum of their digits,
    order their indexes in ascending order.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.

    For example:
    >>> rank_by_points([1, 11, -1, -11, -12]) == [2, 3, 0, 4, 1]
    >>> rank_by_points([]) == []
    """
''', '''
    def weight(x):
        digits = [int(c) for c in str(abs(x))]
        if x < 0:
            digits[0] = -digits[0]
        return sum(digits)
    return sorted(range(len(nums)), key=lambda i: weight(nums[i]))
''', '''
import random
def w(x):
    d = [int(c) for c in str(abs(x))]
    if x < 0:
        d[0] = -d[0]
    return sum(d)
assert rank_by_points([1, 11, -1, -11, -12]) == [2, 3, 0, 4, 1]
assert rank_by_points([]) == []
assert rank_by_points([0]) == [0]
assert rank_by_points([5]) == [0]
assert rank_by_points([3, 2, 1]) == [2, 1, 0]
assert rank_by_points([1, 1, 1]) == [0, 1, 2]
assert rank_by_points([-5, 5, 0]) == [0, 2, 1]
assert rank_by_points([10, 1, 100]) == [0, 1, 2]
assert rank_by_points([-10, 10, -1]) == [0, 2, 1]
assert rank_by_points([9, -9, 99, -99]) == [1, 3, 0, 2]
assert rank_by_points([20, 11, 2]) == [0, 1, 2]
assert rank_by_points([-11, 11, 0]) == [0, 2, 1]
a = [3, 1, 2]
rank_by_points(a)
assert a == [3, 1, 2]
random.seed(90)
for _ in range(300):
    L = [random.randint(-300, 300) for _ in range(random.randint(0, 15))]
    r = rank_by_points(L)
    assert sorted(r) == list(range(len(L)))
    assert r == [i for _, i in sorted((w(v), i) for i, v in enumerate(L))]
big = [random.randint(-10 ** 9, 10 ** 9) for _ in range(50000)]
r = rank_by_points(big)
assert len(r) == 50000 and all(w(big[r[i]]) <= w(big[r[i + 1]]) for i in range(len(r) - 1))
''')

# ---------------------------------------------------------------- HumanEval/156
add(156, '''def roman_to_int(s):
    """
    Given a roman numeral as a lowercase string, obtain its integer equivalent.
    The roman numeral is valid and its value is between 1 and 3999.

    Examples:
    >>> roman_to_int('xix') == 19
    >>> roman_to_int('clii') == 152
    >>> roman_to_int('cdxxvi') == 426
    """
''', '''
    values = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    total = 0
    for i, ch in enumerate(s):
        v = values[ch]
        if i + 1 < len(s) and values[s[i + 1]] > v:
            total -= v
        else:
            total += v
    return total
''', '''
def to_roman(n):
    out = ""
    for v, r in ((1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"), (90, "xc"), (50, "l"), (40, "xl"), (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
        while n >= v:
            out += r
            n -= v
    return out
assert roman_to_int("i") == 1
assert roman_to_int("ii") == 2
assert roman_to_int("iii") == 3
assert roman_to_int("iv") == 4
assert roman_to_int("v") == 5
assert roman_to_int("ix") == 9
assert roman_to_int("xix") == 19
assert roman_to_int("clii") == 152
assert roman_to_int("cdxxvi") == 426
assert roman_to_int("xl") == 40
assert roman_to_int("xc") == 90
assert roman_to_int("cd") == 400
assert roman_to_int("cm") == 900
assert roman_to_int("m") == 1000
assert roman_to_int("mcmxciv") == 1994
assert roman_to_int("mmmcmxcix") == 3999
assert roman_to_int("mmxxiv") == 2024
assert roman_to_int("dccclxxxviii") == 888
for n in range(1, 4000):
    assert roman_to_int(to_roman(n)) == n, n
''')

add(156, '''def int_to_roman_upper(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in uppercase.
    Restrictions: 1 <= num <= 3999

    Examples:
    >>> int_to_roman_upper(19) == 'XIX'
    >>> int_to_roman_upper(152) == 'CLII'
    >>> int_to_roman_upper(1994) == 'MCMXCIV'
    """
''', '''
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return thousands[number // 1000] + hundreds[number % 1000 // 100] + tens[number % 100 // 10] + ones[number % 10]
''', '''
def back(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        if i + 1 < len(s) and values[s[i + 1]] > values[ch]:
            total -= values[ch]
        else:
            total += values[ch]
    return total
assert int_to_roman_upper(1) == "I"
assert int_to_roman_upper(4) == "IV"
assert int_to_roman_upper(9) == "IX"
assert int_to_roman_upper(19) == "XIX"
assert int_to_roman_upper(40) == "XL"
assert int_to_roman_upper(90) == "XC"
assert int_to_roman_upper(152) == "CLII"
assert int_to_roman_upper(400) == "CD"
assert int_to_roman_upper(426) == "CDXXVI"
assert int_to_roman_upper(900) == "CM"
assert int_to_roman_upper(1000) == "M"
assert int_to_roman_upper(1994) == "MCMXCIV"
assert int_to_roman_upper(2024) == "MMXXIV"
assert int_to_roman_upper(3000) == "MMM"
assert int_to_roman_upper(3888) == "MMMDCCCLXXXVIII"
assert int_to_roman_upper(3999) == "MMMCMXCIX"
for n in range(1, 4000):
    r = int_to_roman_upper(n)
    assert r == r.upper() and r.isalpha()
    assert back(r) == n, n
    assert "IIII" not in r and "XXXX" not in r and "CCCC" not in r and "VV" not in r
''')

add(156, '''def roman_length(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string
    and return the number of characters in it.
    Restrictions: 1 <= num <= 3999

    Examples:
    >>> roman_length(19) == 3
    >>> roman_length(152) == 4
    >>> roman_length(3888) == 15
    """
''', '''
    lens = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]
    return lens[number // 1000 % 10] + lens[number // 100 % 10] + lens[number // 10 % 10] + lens[number % 10]
''', '''
def to_roman(n):
    out = ""
    for v, r in ((1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"), (90, "xc"), (50, "l"), (40, "xl"), (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
        while n >= v:
            out += r
            n -= v
    return out
assert roman_length(1) == 1
assert roman_length(2) == 2
assert roman_length(3) == 3
assert roman_length(4) == 2
assert roman_length(8) == 4
assert roman_length(9) == 2
assert roman_length(19) == 3
assert roman_length(40) == 2
assert roman_length(152) == 4
assert roman_length(426) == 6
assert roman_length(1000) == 1
assert roman_length(1994) == 7
assert roman_length(3000) == 3
assert roman_length(3888) == 15
assert roman_length(3999) == 9
assert roman_length(2000) == 2
for n in range(1, 4000):
    assert roman_length(n) == len(to_roman(n)), n
assert max(roman_length(n) for n in range(1, 4000)) == 15
''')

add(156, '''def int_to_additive_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string written
    without the subtractive notation (so 4 is 'iiii' and 9 is 'viiii'), and return it in lowercase.
    The greatest possible symbols are used first (m = 1000, d = 500, c = 100, l = 50, x = 10, v = 5, i = 1).
    Restrictions: 1 <= num <= 3999

    Examples:
    >>> int_to_additive_roman(19) == 'xviiii'
    >>> int_to_additive_roman(152) == 'clii'
    """
''', '''
    result = ""
    for value, symbol in ((1000, "m"), (500, "d"), (100, "c"), (50, "l"), (10, "x"), (5, "v"), (1, "i")):
        result += symbol * (number // value)
        number %= value
    return result
''', '''
values = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
assert int_to_additive_roman(1) == "i"
assert int_to_additive_roman(4) == "iiii"
assert int_to_additive_roman(5) == "v"
assert int_to_additive_roman(9) == "viiii"
assert int_to_additive_roman(14) == "xiiii"
assert int_to_additive_roman(19) == "xviiii"
assert int_to_additive_roman(40) == "xxxx"
assert int_to_additive_roman(90) == "lxxxx"
assert int_to_additive_roman(152) == "clii"
assert int_to_additive_roman(426) == "ccccxxvi"
assert int_to_additive_roman(900) == "dcccc"
assert int_to_additive_roman(1994) == "mdcccclxxxxiiii"
assert int_to_additive_roman(3999) == "mmm" + "dcccc" + "lxxxx" + "viiii"
assert int_to_additive_roman(4000 - 1000) == "mmm"
for n in range(1, 4000):
    r = int_to_additive_roman(n)
    assert sum(values[c] for c in r) == n, n
    assert list(r) == sorted(r, key=lambda c: -values[c])
    assert r.count("i") <= 4 and r.count("x") <= 4 and r.count("c") <= 4 and r.count("m") <= 3
    assert r.count("v") <= 1 and r.count("l") <= 1 and r.count("d") <= 1
''')

add(156, '''def is_valid_roman(s):
    """
    Given a string, return True if it is a roman numeral written in the standard (shortest)
    form in lowercase, with a value between 1 and 3999, and False otherwise.
    For example 'iv' is valid, but 'iiii', 'vx', 'ic', 'IV' and the empty string are not.

    Examples:
    >>> is_valid_roman('xix') == True
    >>> is_valid_roman('iiii') == False
    >>> is_valid_roman('mcmxciv') == True
    >>> is_valid_roman('') == False
    """
''', '''
    thousands = ["", "m", "mm", "mmm"]
    hundreds = ["", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]
    tens = ["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"]
    ones = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]
    if not s:
        return False
    for a in thousands:
        for b in hundreds:
            for c in tens:
                for d in ones:
                    if a + b + c + d == s:
                        return True
    return False
''', '''
import random
def to_roman(n):
    out = ""
    for v, r in ((1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"), (90, "xc"), (50, "l"), (40, "xl"), (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
        while n >= v:
            out += r
            n -= v
    return out
VALID = {to_roman(n) for n in range(1, 4000)}
assert is_valid_roman("xix") is True
assert is_valid_roman("iiii") is False
assert is_valid_roman("mcmxciv") is True
assert is_valid_roman("") is False
assert is_valid_roman("iv") is True
assert is_valid_roman("vx") is False
assert is_valid_roman("ic") is False
assert is_valid_roman("IV") is False
assert is_valid_roman("mmmm") is False
assert is_valid_roman("mmmcmxcix") is True
assert is_valid_roman("mmmm") is False
assert is_valid_roman("vv") is False
assert is_valid_roman("iix") is False
assert is_valid_roman("xxxx") is False
assert is_valid_roman("cmc") is False
assert is_valid_roman("im") is False
assert is_valid_roman("viv") is False
assert is_valid_roman(" i") is False
assert is_valid_roman("i ") is False
assert is_valid_roman("a") is False
for r in VALID:
    assert is_valid_roman(r) is True, r
random.seed(96)
for _ in range(3000):
    t = "".join(random.choice("ivxlcdm") for _ in range(random.randint(0, 8)))
    assert is_valid_roman(t) == (t in VALID), t
assert is_valid_roman("m" * 1000) is False
''')

# ---------------------------------------------------------------- HumanEval/163
add(163, '''def generate_odd_digits(a, b):
    """
    Given two positive integers a and b, return the odd digits between a
    and b, in ascending order.

    For example:
    generate_odd_digits(2, 8) => [3, 5, 7]
    generate_odd_digits(8, 2) => [3, 5, 7]
    generate_odd_digits(1, 1) => [1]
    generate_odd_digits(10, 14) => []
    """
''', '''
    lo, hi = min(a, b), max(a, b)
    return [d for d in (1, 3, 5, 7, 9) if lo <= d <= hi]
''', '''
assert generate_odd_digits(2, 8) == [3, 5, 7]
assert generate_odd_digits(8, 2) == [3, 5, 7]
assert generate_odd_digits(1, 1) == [1]
assert generate_odd_digits(10, 14) == []
assert generate_odd_digits(1, 9) == [1, 3, 5, 7, 9]
assert generate_odd_digits(9, 1) == [1, 3, 5, 7, 9]
assert generate_odd_digits(1, 100) == [1, 3, 5, 7, 9]
assert generate_odd_digits(100, 1) == [1, 3, 5, 7, 9]
assert generate_odd_digits(9, 9) == [9]
assert generate_odd_digits(9, 10) == [9]
assert generate_odd_digits(4, 4) == []
assert generate_odd_digits(2, 2) == []
assert generate_odd_digits(4, 6) == [5]
assert generate_odd_digits(10, 10 ** 18) == []
assert generate_odd_digits(10 ** 18, 1) == [1, 3, 5, 7, 9]
assert generate_odd_digits(7, 3) == [3, 5, 7]
for a in range(1, 25):
    for b in range(1, 25):
        exp = [d for d in range(min(a, b), max(a, b) + 1) if d < 10 and d % 2 == 1]
        assert generate_odd_digits(a, b) == exp, (a, b)
''')

add(163, '''def generate_even_digits_desc(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in descending order.

    For example:
    generate_even_digits_desc(2, 8) => [8, 6, 4, 2]
    generate_even_digits_desc(8, 2) => [8, 6, 4, 2]
    generate_even_digits_desc(3, 5) => [4]
    generate_even_digits_desc(10, 14) => []
    """
''', '''
    lo, hi = min(a, b), max(a, b)
    return [d for d in (8, 6, 4, 2) if lo <= d <= hi]
''', '''
assert generate_even_digits_desc(2, 8) == [8, 6, 4, 2]
assert generate_even_digits_desc(8, 2) == [8, 6, 4, 2]
assert generate_even_digits_desc(3, 5) == [4]
assert generate_even_digits_desc(10, 14) == []
assert generate_even_digits_desc(1, 100) == [8, 6, 4, 2]
assert generate_even_digits_desc(100, 1) == [8, 6, 4, 2]
assert generate_even_digits_desc(2, 2) == [2]
assert generate_even_digits_desc(1, 1) == []
assert generate_even_digits_desc(9, 9) == []
assert generate_even_digits_desc(8, 9) == [8]
assert generate_even_digits_desc(9, 20) == []
assert generate_even_digits_desc(5, 7) == [6]
assert generate_even_digits_desc(6, 6) == [6]
assert generate_even_digits_desc(10 ** 18, 5) == [8, 6]
assert generate_even_digits_desc(3, 4) == [4]
for a in range(1, 25):
    for b in range(1, 25):
        exp = [d for d in range(max(a, b), min(a, b) - 1, -1) if d < 10 and d % 2 == 0]
        assert generate_even_digits_desc(a, b) == exp, (a, b)
''')

add(163, '''def count_even_digits(a, b):
    """
    Given two positive integers a and b, return how many even digits there are between a
    and b inclusive. Only the digits 2, 4, 6 and 8 are counted.

    For example:
    count_even_digits(2, 8) => 4
    count_even_digits(8, 2) => 4
    count_even_digits(3, 5) => 1
    count_even_digits(10, 14) => 0
    """
''', '''
    lo, hi = min(a, b), max(a, b)
    return sum(1 for d in (2, 4, 6, 8) if lo <= d <= hi)
''', '''
assert count_even_digits(2, 8) == 4
assert count_even_digits(8, 2) == 4
assert count_even_digits(3, 5) == 1
assert count_even_digits(10, 14) == 0
assert count_even_digits(1, 1) == 0
assert count_even_digits(2, 2) == 1
assert count_even_digits(1, 10) == 4
assert count_even_digits(1, 100) == 4
assert count_even_digits(100, 1) == 4
assert count_even_digits(4, 4) == 1
assert count_even_digits(5, 5) == 0
assert count_even_digits(9, 9) == 0
assert count_even_digits(8, 100) == 1
assert count_even_digits(9, 100) == 0
assert count_even_digits(10 ** 18, 10 ** 18) == 0
assert count_even_digits(3, 3) == 0
for a in range(1, 25):
    for b in range(1, 25):
        exp = sum(1 for d in range(min(a, b), max(a, b) + 1) if d in (2, 4, 6, 8))
        assert count_even_digits(a, b) == exp, (a, b)
''')

add(163, '''def generate_prime_digits(a, b):
    """
    Given two positive integers a and b, return the prime digits between a
    and b, in ascending order.

    For example:
    generate_prime_digits(1, 10) => [2, 3, 5, 7]
    generate_prime_digits(10, 1) => [2, 3, 5, 7]
    generate_prime_digits(4, 6) => [5]
    generate_prime_digits(8, 14) => []
    """
''', '''
    lo, hi = min(a, b), max(a, b)
    return [d for d in (2, 3, 5, 7) if lo <= d <= hi]
''', '''
assert generate_prime_digits(1, 10) == [2, 3, 5, 7]
assert generate_prime_digits(10, 1) == [2, 3, 5, 7]
assert generate_prime_digits(4, 6) == [5]
assert generate_prime_digits(8, 14) == []
assert generate_prime_digits(1, 1) == []
assert generate_prime_digits(2, 2) == [2]
assert generate_prime_digits(2, 3) == [2, 3]
assert generate_prime_digits(3, 2) == [2, 3]
assert generate_prime_digits(7, 7) == [7]
assert generate_prime_digits(4, 4) == []
assert generate_prime_digits(6, 6) == []
assert generate_prime_digits(5, 7) == [5, 7]
assert generate_prime_digits(8, 9) == []
assert generate_prime_digits(1, 10 ** 18) == [2, 3, 5, 7]
assert generate_prime_digits(10 ** 18, 7) == [7]
for a in range(1, 25):
    for b in range(1, 25):
        exp = [d for d in range(min(a, b), max(a, b) + 1) if d in (2, 3, 5, 7)]
        assert generate_prime_digits(a, b) == exp, (a, b)
''')

add(163, '''def sum_even_digits(a, b):
    """
    Given two positive integers a and b, return the sum of the even digits between a
    and b. Only the digits 2, 4, 6 and 8 are summed, the sum of no digits is 0.

    For example:
    sum_even_digits(2, 8) => 20
    sum_even_digits(8, 2) => 20
    sum_even_digits(3, 5) => 4
    sum_even_digits(10, 14) => 0
    """
''', '''
    lo, hi = min(a, b), max(a, b)
    return sum(d for d in (2, 4, 6, 8) if lo <= d <= hi)
''', '''
assert sum_even_digits(2, 8) == 20
assert sum_even_digits(8, 2) == 20
assert sum_even_digits(3, 5) == 4
assert sum_even_digits(10, 14) == 0
assert sum_even_digits(1, 1) == 0
assert sum_even_digits(2, 2) == 2
assert sum_even_digits(1, 100) == 20
assert sum_even_digits(100, 1) == 20
assert sum_even_digits(4, 6) == 10
assert sum_even_digits(5, 5) == 0
assert sum_even_digits(8, 8) == 8
assert sum_even_digits(9, 9) == 0
assert sum_even_digits(7, 100) == 8
assert sum_even_digits(10 ** 18, 3) == 18
assert sum_even_digits(6, 7) == 6
for a in range(1, 25):
    for b in range(1, 25):
        exp = sum(d for d in range(min(a, b), max(a, b) + 1) if d in (2, 4, 6, 8))
        assert sum_even_digits(a, b) == exp, (a, b)
''')
