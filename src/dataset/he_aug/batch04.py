# parents 21-27
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------- parent 21: add_elements ----------------
add(21, '''def add_last_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with an even number of digits from the LAST k elements of arr.
    The minus sign is not a digit.

    Example:

        Input: arr = [111, 21, 3, 4000, 5, 66], k = 4
        Output: 4000 # 3, 4000, 5, 66 -> 4000 + 66 = 4066

    Constraints:
        1. 1 <= len(arr) <= 100000
        2. 1 <= k <= len(arr)
    """
''', '''
    return sum(x for x in arr[len(arr) - k:] if len(str(abs(x))) % 2 == 0)
''', '''
assert add_last_elements([10], 1) == 10
assert add_last_elements([5], 1) == 0
assert add_last_elements([0], 1) == 0
assert add_last_elements([111, 21, 3, 4000, 5, 66], 4) == 4066
assert add_last_elements([111, 21, 3, 4000, 5, 66], 6) == 4087
assert add_last_elements([111, 21, 3, 4000, 5, 66], 1) == 66
assert add_last_elements([-10, -123, -4567], 3) == -4577
assert add_last_elements([-5, -50], 1) == -50
assert add_last_elements([10 ** 9, 10 ** 8], 2) == 10 ** 9
assert add_last_elements([10] * 100000, 100000) == 10 ** 6
assert add_last_elements([10] * 100000, 1) == 10
''')

add(21, '''def sum_k_positive(arr, k):
    """
    Given an array of integers arr and a non-negative integer k, return the sum of the
    positive elements (strictly greater than 0) among the first k elements of arr.
    If k is larger than len(arr), use all elements.

    Example:

        Input: arr = [3, -1, 4, -5, 9], k = 4
        Output: 7 # 3 + 4

    Constraints:
        1. 0 <= len(arr) <= 100000
        2. 0 <= k
    """
''', '''
    return sum(x for x in arr[:k] if x > 0)
''', '''
assert sum_k_positive([], 0) == 0
assert sum_k_positive([], 5) == 0
assert sum_k_positive([3, -1, 4, -5, 9], 4) == 7
assert sum_k_positive([3, -1, 4, -5, 9], 5) == 16
assert sum_k_positive([3, -1, 4, -5, 9], 100) == 16
assert sum_k_positive([3, -1, 4, -5, 9], 0) == 0
assert sum_k_positive([0, 0, 0], 3) == 0
assert sum_k_positive([-1, -2], 2) == 0
assert sum_k_positive([10 ** 18] * 3, 3) == 3 * 10 ** 18
assert sum_k_positive([1] * 100000, 99999) == 99999
''')

add(21, '''def add_elements_by_digits(arr, k, d):
    """
    Given an array of integers arr, an integer k and an integer d >= 1, return the sum of the
    elements that have at most d digits (the minus sign is not a digit) from the first k
    elements of arr. If k is larger than len(arr), use all elements.

    Example:

        Input: arr = [111, 21, 3, 4000, 5], k = 5, d = 1
        Output: 8 # 3 + 5

    Constraints:
        1. 0 <= len(arr) <= 100000
        2. k >= 0
    """
''', '''
    return sum(x for x in arr[:k] if len(str(abs(x))) <= d)
''', '''
assert add_elements_by_digits([], 3, 1) == 0
assert add_elements_by_digits([111, 21, 3, 4000, 5], 5, 1) == 8
assert add_elements_by_digits([111, 21, 3, 4000, 5], 5, 2) == 29
assert add_elements_by_digits([111, 21, 3, 4000, 5], 5, 4) == 4140
assert add_elements_by_digits([111, 21, 3, 4000, 5], 2, 3) == 132
assert add_elements_by_digits([111, 21, 3, 4000, 5], 0, 3) == 0
assert add_elements_by_digits([111, 21, 3, 4000, 5], 50, 3) == 140
assert add_elements_by_digits([-5, -55, -555], 3, 2) == -60
assert add_elements_by_digits([0], 1, 1) == 0
assert add_elements_by_digits([123456789] * 100000, 100000, 9) == 123456789 * 100000
assert add_elements_by_digits([123456789] * 100000, 100000, 8) == 0
''')

add(21, '''def count_elements_with_digits(arr, d):
    """
    Given an array of integers arr and an integer d >= 1, return the number of elements
    that have exactly d digits. The minus sign is not a digit, and the number 0 has 1 digit.

    Example:

        Input: arr = [111, 21, 3, 4000, 5, -22], d = 2
        Output: 2 # 21 and -22

    Constraints:
        1. 0 <= len(arr) <= 100000
    """
''', '''
    return sum(1 for x in arr if len(str(abs(x))) == d)
''', '''
assert count_elements_with_digits([], 1) == 0
assert count_elements_with_digits([0], 1) == 1
assert count_elements_with_digits([0], 2) == 0
assert count_elements_with_digits([111, 21, 3, 4000, 5, -22], 2) == 2
assert count_elements_with_digits([111, 21, 3, 4000, 5, -22], 1) == 2
assert count_elements_with_digits([-9, 9, -10, 10], 1) == 2
assert count_elements_with_digits([10 ** 18, 10 ** 18 - 1], 19) == 1
assert count_elements_with_digits([10 ** 18, 10 ** 18 - 1], 18) == 1
assert count_elements_with_digits([5] * 100000, 1) == 100000
assert count_elements_with_digits([5] * 100000, 0) == 0
''')

add(21, '''def sum_of_digits_first_k(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return the sum of all the digits
    of the first k elements of arr. The minus sign is ignored.

    Example:

        Input: arr = [111, -21, 3, 4000], k = 3
        Output: 9 # 1+1+1 + 2+1 + 3

    Constraints:
        1. 1 <= len(arr) <= 100000
        2. 1 <= k <= len(arr)
    """
''', '''
    return sum(int(c) for x in arr[:k] for c in str(abs(x)))
''', '''
assert sum_of_digits_first_k([0], 1) == 0
assert sum_of_digits_first_k([-7], 1) == 7
assert sum_of_digits_first_k([111, -21, 3, 4000], 3) == 9
assert sum_of_digits_first_k([111, -21, 3, 4000], 4) == 13
assert sum_of_digits_first_k([111, -21, 3, 4000], 1) == 3
assert sum_of_digits_first_k([999999999999], 1) == 108
assert sum_of_digits_first_k([10 ** 30], 1) == 1
assert sum_of_digits_first_k([99] * 100000, 100000) == 18 * 100000
assert sum_of_digits_first_k([-1] * 100000, 50000) == 50000
''')

# ---------------- parent 22: valid_date ----------------
add(22, '''def valid_time(time):
    """You have to write a function which validates a given time string and
    returns True if the time is valid otherwise False.
    The time is valid if all of the following rules are satisfied:
    1. The time string is in the format: hh:mm:ss (exactly two digits each, separated by ':').
    2. The hours are between 00 and 23 inclusive.
    3. The minutes and the seconds are between 00 and 59 inclusive.
    4. The string contains nothing else (no spaces, no signs).

    for example:
    valid_time('12:30:45') => True
    valid_time('24:00:00') => False
    valid_time('1:30:45') => False
    valid_time('12:60:00') => False
    """
''', '''
    if len(time) != 8 or time[2] != ":" or time[5] != ":":
        return False
    parts = (time[0:2], time[3:5], time[6:8])
    for p in parts:
        if not all(c in "0123456789" for c in p):
            return False
    h, m, s = (int(p) for p in parts)
    return h <= 23 and m <= 59 and s <= 59
''', '''
assert valid_time("12:30:45") is True
assert valid_time("00:00:00") is True
assert valid_time("23:59:59") is True
assert valid_time("24:00:00") is False
assert valid_time("1:30:45") is False
assert valid_time("12:60:00") is False
assert valid_time("12:00:60") is False
assert valid_time("") is False
assert valid_time("12:30") is False
assert valid_time("12-30-45") is False
assert valid_time("12:30:45 ") is False
assert valid_time(" 2:30:45") is False
assert valid_time("+2:30:45") is False
assert valid_time("-1:30:45") is False
assert valid_time("1a:30:45") is False
assert valid_time("12:30:455") is False
assert valid_time("\\u0661\\u0662:30:45") is False
assert valid_time("12:3\\u00b2:45") is False
assert valid_time("12:30:4_") is False
assert valid_time("12:30:45:00") is False
assert valid_time("::::::::") is False
''')

add(22, '''def valid_date_iso(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date must be in the format yyyy-mm-dd (4 digits, 2 digits, 2 digits).
    It is valid if the month is between 1 and 12 and the day exists in that month.
    Leap years are taken into account: a year is a leap year if it is divisible by 4 but not
    by 100, or it is divisible by 400. Year 0000 is not valid.

    for example:
    valid_date_iso('2020-02-29') => True
    valid_date_iso('2019-02-29') => False
    valid_date_iso('1900-02-29') => False
    valid_date_iso('2000-02-29') => True
    valid_date_iso('2021-13-01') => False
    """
''', '''
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        return False
    y, m, d = date[0:4], date[5:7], date[8:10]
    for p in (y, m, d):
        if not all(c in "0123456789" for c in p):
            return False
    y, m, d = int(y), int(m), int(d)
    if y == 0 or m < 1 or m > 12 or d < 1:
        return False
    days = [31, 29 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return d <= days[m - 1]
''', '''
assert valid_date_iso("2020-02-29") is True
assert valid_date_iso("2019-02-29") is False
assert valid_date_iso("1900-02-29") is False
assert valid_date_iso("2000-02-29") is True
assert valid_date_iso("2100-02-29") is False
assert valid_date_iso("2021-13-01") is False
assert valid_date_iso("2021-00-10") is False
assert valid_date_iso("2021-01-00") is False
assert valid_date_iso("2021-01-32") is False
assert valid_date_iso("2021-04-31") is False
assert valid_date_iso("2021-04-30") is True
assert valid_date_iso("2021-12-31") is True
assert valid_date_iso("0000-01-01") is False
assert valid_date_iso("0001-01-01") is True
assert valid_date_iso("9999-12-31") is True
assert valid_date_iso("") is False
assert valid_date_iso("2021/01/01") is False
assert valid_date_iso("21-01-01") is False
assert valid_date_iso("2021-1-01") is False
assert valid_date_iso("2021-01-01 ") is False
assert valid_date_iso("2021-01-0a") is False
assert valid_date_iso("-021-01-01") is False
assert valid_date_iso("2021-+1-01") is False
assert valid_date_iso("2021-01-\\u0661\\u0662") is False
import datetime
for y in (1999, 2000, 2004, 1900, 2100):
    for m in range(1, 13):
        for d in range(1, 33):
            try:
                datetime.date(y, m, d)
                exp = True
            except ValueError:
                exp = False
            assert valid_date_iso("%04d-%02d-%02d" % (y, m, d)) is exp, (y, m, d)
''')

add(22, '''def valid_date_us(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date must be in the format: m/d/yyyy where the month and the day can have one or two
    digits (no sign, no spaces) and the year has exactly four digits.
    The month must be between 1 and 12 and the day between 1 and the number of days of the month
    (February always has at most 29 days here, ignore leap years).

    for example:
    valid_date_us('3/11/2000') => True
    valid_date_us('03/11/2000') => True
    valid_date_us('2/30/2000') => False
    valid_date_us('13/1/2000') => False
    valid_date_us('3-11-2000') => False
    """
''', '''
    parts = date.split("/")
    if len(parts) != 3:
        return False
    ms, ds, ys = parts
    if not (1 <= len(ms) <= 2 and 1 <= len(ds) <= 2 and len(ys) == 4):
        return False
    for p in parts:
        if not all(c in "0123456789" for c in p):
            return False
    m, d = int(ms), int(ds)
    if m < 1 or m > 12 or d < 1:
        return False
    limit = 29 if m == 2 else 30 if m in (4, 6, 9, 11) else 31
    return d <= limit
''', '''
assert valid_date_us("3/11/2000") is True
assert valid_date_us("03/11/2000") is True
assert valid_date_us("2/29/2001") is True
assert valid_date_us("2/30/2000") is False
assert valid_date_us("13/1/2000") is False
assert valid_date_us("0/1/2000") is False
assert valid_date_us("1/0/2000") is False
assert valid_date_us("00/10/2000") is False
assert valid_date_us("4/31/2000") is False
assert valid_date_us("4/30/2000") is True
assert valid_date_us("12/31/0000") is True
assert valid_date_us("3-11-2000") is False
assert valid_date_us("") is False
assert valid_date_us("//") is False
assert valid_date_us("3/11") is False
assert valid_date_us("3/11/2000/1") is False
assert valid_date_us("3/11/200") is False
assert valid_date_us("3/11/20000") is False
assert valid_date_us("003/11/2000") is False
assert valid_date_us("3/011/2000") is False
assert valid_date_us(" 3/11/2000") is False
assert valid_date_us("-3/11/2000") is False
assert valid_date_us("3/1x/2000") is False
assert valid_date_us("1/1/\\u0662\\u0660\\u0662\\u0660") is False
''')

add(22, '''def days_in_month(month, year):
    """Return the number of days in the given month (1-12) of the given year (year >= 1),
    taking leap years into account: a year is a leap year if it is divisible by 4 but not by 100,
    or it is divisible by 400.
    If the month is not between 1 and 12 (or the year is below 1), return -1.

    for example:
    days_in_month(2, 2020) => 29
    days_in_month(2, 1900) => 28
    days_in_month(4, 2021) => 30
    days_in_month(13, 2021) => -1
    """
''', '''
    if month < 1 or month > 12 or year < 1:
        return -1
    if month == 2:
        leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        return 29 if leap else 28
    return 30 if month in (4, 6, 9, 11) else 31
''', '''
assert days_in_month(1, 2021) == 31
assert days_in_month(2, 2020) == 29
assert days_in_month(2, 2021) == 28
assert days_in_month(2, 1900) == 28
assert days_in_month(2, 2000) == 29
assert days_in_month(2, 2100) == 28
assert days_in_month(2, 4) == 29
assert days_in_month(2, 1) == 28
assert days_in_month(4, 2021) == 30
assert days_in_month(6, 2021) == 30
assert days_in_month(9, 2021) == 30
assert days_in_month(11, 2021) == 30
assert days_in_month(12, 2021) == 31
assert days_in_month(0, 2021) == -1
assert days_in_month(13, 2021) == -1
assert days_in_month(-1, 2021) == -1
assert days_in_month(1, 0) == -1
assert days_in_month(1, -2000) == -1
assert days_in_month(2, 10 ** 18) == 29
assert days_in_month(2, 10 ** 18 + 1) == 28
import calendar
for y in range(1, 2500):
    for m in range(1, 13):
        assert days_in_month(m, y) == calendar.monthrange(y, m)[1]
''')

add(22, '''def valid_phone(phone):
    """You have to write a function which validates a given phone number string and
    returns True if it is valid otherwise False.
    A valid phone number has the format (ddd) ddd-dddd where every d is a digit 0-9,
    for example '(123) 456-7890'. There is exactly one space after the closing bracket.
    The first digit of the area code (inside the brackets) and the first digit after the
    space must not be 0 or 1.

    for example:
    valid_phone('(234) 567-8901') => True
    valid_phone('(034) 567-8901') => False
    valid_phone('234-567-8901') => False
    valid_phone('(234)567-8901') => False
    """
''', '''
    if len(phone) != 14:
        return False
    if phone[0] != "(" or phone[4] != ")" or phone[5] != " " or phone[9] != "-":
        return False
    digits = phone[1:4] + phone[6:9] + phone[10:14]
    if not all(c in "0123456789" for c in digits):
        return False
    return phone[1] not in "01" and phone[6] not in "01"
''', '''
assert valid_phone("(234) 567-8901") is True
assert valid_phone("(999) 999-9999") is True
assert valid_phone("(234) 267-0000") is True
assert valid_phone("(034) 567-8901") is False
assert valid_phone("(134) 567-8901") is False
assert valid_phone("(234) 067-8901") is False
assert valid_phone("(234) 167-8901") is False
assert valid_phone("234-567-8901") is False
assert valid_phone("(234)567-8901") is False
assert valid_phone("(234)  567-8901") is False
assert valid_phone("") is False
assert valid_phone("(234) 567-890") is False
assert valid_phone("(234) 567-89012") is False
assert valid_phone("(234) 567 8901") is False
assert valid_phone("(23a) 567-8901") is False
assert valid_phone("[234) 567-8901") is False
assert valid_phone("(234) 567-8901\\n") is False
assert valid_phone("(234) 567-\\u0668901") is False
assert valid_phone("(+34) 567-8901") is False
''')

# ---------------- parent 23: is_sorted ----------------
add(23, '''def is_sorted_desc(lst):
    \'\'\'
    Given a list of integers, return whether or not they are sorted
    in descending order. Equal neighbours are allowed, but if any number appears
    more than twice, return False. An empty list or a list with one element is sorted.

    Examples
    is_sorted_desc([5]) ➞ True
    is_sorted_desc([5, 4, 3]) ➞ True
    is_sorted_desc([5, 4, 4, 3]) ➞ True
    is_sorted_desc([5, 4, 4, 4]) ➞ False
    is_sorted_desc([3, 4, 5]) ➞ False
    \'\'\'
''', '''
    counts = {}
    for x in lst:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > 2:
            return False
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
''', '''
assert is_sorted_desc([]) is True
assert is_sorted_desc([5]) is True
assert is_sorted_desc([5, 4, 3]) is True
assert is_sorted_desc([5, 4, 4, 3]) is True
assert is_sorted_desc([5, 4, 4, 4]) is False
assert is_sorted_desc([3, 4, 5]) is False
assert is_sorted_desc([4, 5, 4]) is False
assert is_sorted_desc([4, 4]) is True
assert is_sorted_desc([4, 4, 4]) is False
assert is_sorted_desc([0, -1, -1, -2]) is True
assert is_sorted_desc([1, 0, 1]) is False
assert is_sorted_desc([2, 2, 1, 1]) is True
assert is_sorted_desc(list(range(100000, 0, -1))) is True
assert is_sorted_desc(list(range(100000)) ) is False
assert is_sorted_desc([3, 3, 3, 2]) is False
assert is_sorted_desc([-1, -1, -2, -2, -3]) is True
''')

add(23, '''def is_strictly_sorted(lst):
    \'\'\'
    Given a list of numbers (integers or floats), return True if they are sorted in strictly
    ascending order (no duplicates allowed), otherwise return False.
    An empty list or a list with one element is sorted. NaN is never sorted with anything.

    Examples
    is_strictly_sorted([1, 2, 3]) ➞ True
    is_strictly_sorted([1, 2, 2]) ➞ False
    is_strictly_sorted([1.5, 2, 2.5]) ➞ True
    is_strictly_sorted([]) ➞ True
    \'\'\'
''', '''
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
''', '''
assert is_strictly_sorted([]) is True
assert is_strictly_sorted([1]) is True
assert is_strictly_sorted([float("nan")]) is True
assert is_strictly_sorted([1, 2, 3]) is True
assert is_strictly_sorted([1, 2, 2]) is False
assert is_strictly_sorted([2, 1]) is False
assert is_strictly_sorted([1.5, 2, 2.5]) is True
assert is_strictly_sorted([-3, -2, -1, 0]) is True
assert is_strictly_sorted([1, float("nan")]) is False
assert is_strictly_sorted([float("-inf"), 0, float("inf")]) is True
assert is_strictly_sorted([float("inf"), float("inf")]) is False
assert is_strictly_sorted([1, 1.0]) is False
assert is_strictly_sorted(list(range(100000))) is True
assert is_strictly_sorted(list(range(100000)) + [99999]) is False
''')

add(23, '''def is_sorted_by_length(words):
    \'\'\'
    Given a list of strings, return whether or not they are sorted by length in ascending
    order (words with equal length are allowed next to each other). If the list contains the
    same string more than twice, return False. Comparison of repeated strings is
    case-sensitive.

    Examples
    is_sorted_by_length(['a', 'bb', 'ccc']) ➞ True
    is_sorted_by_length(['aa', 'b']) ➞ False
    is_sorted_by_length(['a', 'a', 'a']) ➞ False
    is_sorted_by_length([]) ➞ True
    \'\'\'
''', '''
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
        if counts[w] > 2:
            return False
    return all(len(words[i]) <= len(words[i + 1]) for i in range(len(words) - 1))
''', '''
assert is_sorted_by_length([]) is True
assert is_sorted_by_length(["a"]) is True
assert is_sorted_by_length(["a", "bb", "ccc"]) is True
assert is_sorted_by_length(["aa", "b"]) is False
assert is_sorted_by_length(["a", "a", "a"]) is False
assert is_sorted_by_length(["a", "a"]) is True
assert is_sorted_by_length(["a", "b", "c"]) is True
assert is_sorted_by_length(["", "a", "ab"]) is True
assert is_sorted_by_length(["a", ""]) is False
assert is_sorted_by_length(["a", "A", "a"]) is True
assert is_sorted_by_length(["x" * i for i in range(1, 1001)]) is True
assert is_sorted_by_length(["x" * i for i in range(1000, 0, -1)]) is False
assert is_sorted_by_length(["ab", "cd"] * 2) is True
assert is_sorted_by_length(["ab", "cd"] * 3) is False
''')

add(23, '''def is_rotated_sorted(lst):
    \'\'\'
    Given a list of integers with no duplicates, return True if the list is an ascending sorted
    list rotated by any number of positions (including zero), otherwise return False.
    An empty list and a list with one element return True.

    Examples
    is_rotated_sorted([3, 4, 5, 1, 2]) ➞ True
    is_rotated_sorted([1, 2, 3]) ➞ True
    is_rotated_sorted([2, 1, 3]) ➞ False
    is_rotated_sorted([]) ➞ True
    \'\'\'
''', '''
    drops = 0
    n = len(lst)
    for i in range(n):
        if lst[i] > lst[(i + 1) % n]:
            drops += 1
            if drops > 1:
                return False
    return True
''', '''
assert is_rotated_sorted([]) is True
assert is_rotated_sorted([1]) is True
assert is_rotated_sorted([2, 1]) is True
assert is_rotated_sorted([1, 2]) is True
assert is_rotated_sorted([3, 4, 5, 1, 2]) is True
assert is_rotated_sorted([1, 2, 3]) is True
assert is_rotated_sorted([2, 1, 3]) is False
assert is_rotated_sorted([2, 3, 1]) is True
assert is_rotated_sorted([3, 1, 2]) is True
assert is_rotated_sorted([1, 3, 2]) is False
assert is_rotated_sorted([-1, 5, -10, -5]) is True
assert is_rotated_sorted([-1, 5, -10, -12]) is False
assert is_rotated_sorted([-3, -2, 7, -9, -8]) is True
assert is_rotated_sorted(list(range(50000, 100000)) + list(range(50000))) is True
assert is_rotated_sorted(list(range(50000, 100000)) + list(range(49999, -1, -1))) is False
import itertools
for n in range(1, 7):
    base = list(range(n))
    rots = {tuple(base[i:] + base[:i]) for i in range(n)}
    for p in itertools.permutations(base):
        assert is_rotated_sorted(list(p)) == (p in rots), p
''')

add(23, '''def is_sorted_matrix(rows):
    \'\'\'
    Given a list of lists of integers (a matrix, all rows have the same length), return True
    if every row is sorted in non-decreasing order AND the last element of every row is not
    greater than the first element of the next row. Otherwise return False.
    An empty matrix, or a matrix with empty rows, returns True.

    Examples
    is_sorted_matrix([[1, 2], [3, 4]]) ➞ True
    is_sorted_matrix([[1, 2], [2, 4]]) ➞ True
    is_sorted_matrix([[1, 5], [3, 4]]) ➞ False
    is_sorted_matrix([[3, 1]]) ➞ False
    \'\'\'
''', '''
    flat = [x for row in rows for x in row]
    return all(flat[i] <= flat[i + 1] for i in range(len(flat) - 1))
''', '''
assert is_sorted_matrix([]) is True
assert is_sorted_matrix([[]]) is True
assert is_sorted_matrix([[], []]) is True
assert is_sorted_matrix([[1]]) is True
assert is_sorted_matrix([[1, 2], [3, 4]]) is True
assert is_sorted_matrix([[1, 2], [2, 4]]) is True
assert is_sorted_matrix([[1, 5], [3, 4]]) is False
assert is_sorted_matrix([[3, 1]]) is False
assert is_sorted_matrix([[1, 2], [0, 4]]) is False
assert is_sorted_matrix([[-5, -4], [-4, 0], [0, 0]]) is True
assert is_sorted_matrix([[1], [2], [3], [2]]) is False
m = [list(range(i * 300, i * 300 + 300)) for i in range(300)]
assert is_sorted_matrix(m) is True
m[299][299] = -1
assert is_sorted_matrix(m) is False
''')

# ---------------- parent 24: intersection ----------------
add(24, '''def interval_union_length(interval1, interval2):
    """You are given two intervals, where each interval is a pair of integers.
    The given intervals are closed which means that the interval (start, end)
    includes both start and end. For each interval start <= end.
    Return the number of integer points that belong to at least one of the two intervals.

    [input/output] samples:
    interval_union_length((1, 2), (2, 3)) ==> 3
    interval_union_length((1, 2), (5, 6)) ==> 4
    interval_union_length((-3, 3), (-1, 1)) ==> 7
    """
''', '''
    (a, b), (c, d) = interval1, interval2
    total = (b - a + 1) + (d - c + 1)
    overlap = min(b, d) - max(a, c) + 1
    return total - max(overlap, 0)
''', '''
assert interval_union_length((1, 2), (2, 3)) == 3
assert interval_union_length((1, 2), (5, 6)) == 4
assert interval_union_length((-3, 3), (-1, 1)) == 7
assert interval_union_length((0, 0), (0, 0)) == 1
assert interval_union_length((0, 0), (1, 1)) == 2
assert interval_union_length((1, 5), (6, 10)) == 10
assert interval_union_length((1, 5), (5, 10)) == 10
assert interval_union_length((5, 10), (1, 5)) == 10
assert interval_union_length((-10 ** 18, 10 ** 18), (0, 1)) == 2 * 10 ** 18 + 1
assert interval_union_length((-10 ** 18, -10 ** 18), (10 ** 18, 10 ** 18)) == 2
assert interval_union_length((1, 3), (2, 4)) == 4
''')

add(24, '''def intersection_prime_points(interval1, interval2):
    """You are given two intervals, where each interval is a pair of integers.
    The given intervals are closed which means that the interval (start, end)
    includes both start and end. For each interval start <= end.
    Return the number of prime numbers that belong to BOTH intervals. Values can be
    negative and as large as 10**6.

    [input/output] samples:
    intersection_prime_points((1, 10), (5, 20)) ==> 2
    intersection_prime_points((-5, 1), (0, 3)) ==> 0
    intersection_prime_points((2, 2), (2, 2)) ==> 1
    """
''', '''
    lo = max(interval1[0], interval2[0], 2)
    hi = min(interval1[1], interval2[1])
    if lo > hi:
        return 0
    sieve = bytearray([1]) * (hi + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(hi ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, hi + 1, i)))
    return sum(sieve[lo:hi + 1])
''', '''
assert intersection_prime_points((1, 10), (5, 20)) == 2
assert intersection_prime_points((-5, 1), (0, 3)) == 0
assert intersection_prime_points((2, 2), (2, 2)) == 1
assert intersection_prime_points((-10, -2), (-10, -2)) == 0
assert intersection_prime_points((0, 1), (0, 1)) == 0
assert intersection_prime_points((1, 3), (3, 5)) == 1
assert intersection_prime_points((1, 3), (4, 5)) == 0
assert intersection_prime_points((4, 4), (4, 4)) == 0
assert intersection_prime_points((-100, 100), (-50, 50)) == 15
assert intersection_prime_points((0, 10 ** 6), (0, 10 ** 6)) == 78498
assert intersection_prime_points((999983, 10 ** 6), (999983, 10 ** 6)) == 1
assert intersection_prime_points((10 ** 6 - 5, 10 ** 6), (0, 10 ** 6)) == 0
assert intersection_prime_points((-10 ** 6, 10), (3, 7)) == 3
''')

add(24, '''def merge_intervals(intervals):
    """You are given a list of closed intervals, each one is a pair of integers (start, end)
    with start <= end. Merge all intervals that overlap or share a point, and return the
    merged intervals as a sorted list of tuples. Intervals such as (1, 2) and (3, 4) do not
    share a point and are NOT merged (only integer endpoints matter, touching means equal).
    The input must not be modified.

    [input/output] samples:
    merge_intervals([(1, 3), (2, 6), (8, 10)]) ==> [(1, 6), (8, 10)]
    merge_intervals([(1, 4), (4, 5)]) ==> [(1, 5)]
    merge_intervals([]) ==> []
    """
''', '''
    result = []
    for start, end in sorted(intervals):
        if result and start <= result[-1][1]:
            if end > result[-1][1]:
                result[-1] = (result[-1][0], end)
        else:
            result.append((start, end))
    return result
''', '''
assert merge_intervals([]) == []
assert merge_intervals([(1, 1)]) == [(1, 1)]
assert merge_intervals([(1, 3), (2, 6), (8, 10)]) == [(1, 6), (8, 10)]
assert merge_intervals([(1, 4), (4, 5)]) == [(1, 5)]
assert merge_intervals([(1, 2), (3, 4)]) == [(1, 2), (3, 4)]
assert merge_intervals([(5, 6), (1, 2)]) == [(1, 2), (5, 6)]
assert merge_intervals([(1, 10), (2, 3), (4, 5)]) == [(1, 10)]
assert merge_intervals([(1, 5), (1, 3)]) == [(1, 5)]
assert merge_intervals([(-5, -1), (-3, 2)]) == [(-5, 2)]
assert merge_intervals([(1, 1), (1, 1)]) == [(1, 1)]
orig = [(5, 6), (1, 2)]
merge_intervals(orig)
assert orig == [(5, 6), (1, 2)]
big = [(i * 2, i * 2 + 1) for i in range(100000)]
assert merge_intervals(big) == big
big = [(i, i + 1) for i in range(100000)]
assert merge_intervals(big) == [(0, 100000)]
''')

add(24, '''def intersection_of_lists(list1, list2):
    """You are given two lists of closed intervals, each interval is a pair of integers (start, end)
    with start <= end. Inside every list the intervals are sorted and do not overlap.
    Return the list of all intersections between an interval of the first list and an interval
    of the second list, sorted. Single-point intersections are included as (x, x).

    [input/output] samples:
    intersection_of_lists([(0, 2), (5, 10)], [(1, 5), (8, 12)]) ==> [(1, 2), (5, 5), (8, 10)]
    intersection_of_lists([], [(1, 2)]) ==> []
    """
''', '''
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        lo = max(list1[i][0], list2[j][0])
        hi = min(list1[i][1], list2[j][1])
        if lo <= hi:
            result.append((lo, hi))
        if list1[i][1] < list2[j][1]:
            i += 1
        else:
            j += 1
    return result
''', '''
assert intersection_of_lists([], []) == []
assert intersection_of_lists([], [(1, 2)]) == []
assert intersection_of_lists([(1, 2)], []) == []
assert intersection_of_lists([(0, 2), (5, 10)], [(1, 5), (8, 12)]) == [(1, 2), (5, 5), (8, 10)]
assert intersection_of_lists([(1, 3)], [(4, 5)]) == []
assert intersection_of_lists([(1, 10)], [(2, 3), (5, 6)]) == [(2, 3), (5, 6)]
assert intersection_of_lists([(2, 3), (5, 6)], [(1, 10)]) == [(2, 3), (5, 6)]
assert intersection_of_lists([(1, 1)], [(1, 1)]) == [(1, 1)]
assert intersection_of_lists([(-5, -1)], [(-3, 0)]) == [(-3, -1)]
import random
random.seed(9)
def gen():
    pts = sorted(random.sample(range(-30, 30), random.randint(0, 10) * 2))
    return [(pts[i], pts[i + 1]) for i in range(0, len(pts), 2)]
for _ in range(300):
    a, b = gen(), gen()
    exp = []
    for x in a:
        for y in b:
            lo, hi = max(x[0], y[0]), min(x[1], y[1])
            if lo <= hi:
                exp.append((lo, hi))
    assert intersection_of_lists(a, b) == sorted(exp), (a, b)
a = [(i * 4, i * 4 + 2) for i in range(100000)]
b = [(i * 4 + 1, i * 4 + 3) for i in range(100000)]
assert len(intersection_of_lists(a, b)) == 100000
''')

add(24, '''def is_prime_overlap(interval1, interval2):
    """You are given two intervals, where each interval is a pair of integers.
    The given intervals are closed which means that the interval (start, end)
    includes both start and end. For each interval start <= end.
    Return "YES" if the number of integer points shared by the two intervals is a prime number,
    otherwise return "NO". If the two intervals don't share a point, return "NO".

    [input/output] samples:
    is_prime_overlap((1, 3), (2, 4)) ==> "YES"
    is_prime_overlap((1, 2), (2, 3)) ==> "NO"
    is_prime_overlap((-3, -1), (-5, 5)) ==> "YES"
    """
''', '''
    lo = max(interval1[0], interval2[0])
    hi = min(interval1[1], interval2[1])
    n = hi - lo + 1
    if n < 2:
        return "NO"
    i = 2
    while i * i <= n:
        if n % i == 0:
            return "NO"
        i += 1
    return "YES"
''', '''
assert is_prime_overlap((1, 3), (2, 4)) == "YES"
assert is_prime_overlap((1, 2), (2, 3)) == "NO"
assert is_prime_overlap((-3, -1), (-5, 5)) == "YES"
assert is_prime_overlap((0, 0), (0, 0)) == "NO"
assert is_prime_overlap((0, 1), (0, 1)) == "YES"
assert is_prime_overlap((1, 4), (1, 4)) == "NO"
assert is_prime_overlap((1, 5), (1, 5)) == "YES"
assert is_prime_overlap((1, 2), (4, 5)) == "NO"
assert is_prime_overlap((5, 6), (1, 2)) == "NO"
assert is_prime_overlap((0, 10 ** 12 - 1), (0, 10 ** 12 + 5)) == "NO"
assert is_prime_overlap((0, 999999999988), (0, 10 ** 13)) == "YES"
assert is_prime_overlap((-10 ** 18, 10 ** 18), (0, 6)) == "YES"
assert is_prime_overlap((-10 ** 18, 10 ** 18), (0, 7)) == "NO"
assert is_prime_overlap((-10 ** 18, 10 ** 18), (0, 8)) == "NO"
''')

# ---------------- parent 25: minPath ----------------
add(25, '''def max_path_sum(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) of integers and a positive integer k,
    find the maximum sum of the values of a path of length k. You can start from any cell, and in
    each step you can move to any of the neighbor cells that share an edge with the
    current cell. A path of length k visits exactly k cells and cells may be visited more than once.
    You CANNOT go off the grid. Return that maximum sum.

    Examples:

        Input: grid = [[1, 2], [3, 4]], k = 3
        Output: 11  # 4 -> 3 -> 4 or 3 -> 4 -> 3 is 11, but 4 -> 2 -> 4 is 10

        Input: grid = [[-5, -1], [-9, -2]], k = 2
        Output: -3
    """
''', '''
    n = len(grid)
    best = [row[:] for row in grid]
    for _ in range(k - 1):
        nxt = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                m = None
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    a, b = i + di, j + dj
                    if 0 <= a < n and 0 <= b < n and (m is None or best[a][b] > m):
                        m = best[a][b]
                nxt[i][j] = grid[i][j] + (m if m is not None else float("-inf"))
        best = nxt
    return max(max(row) for row in best)
''', '''
assert max_path_sum([[1, 2], [3, 4]], 1) == 4
assert max_path_sum([[1, 2], [3, 4]], 2) == 7
assert max_path_sum([[1, 2], [3, 4]], 3) == 11
assert max_path_sum([[-5, -1], [-9, -2]], 2) == -3
assert max_path_sum([[-5, -1], [-9, -2]], 1) == -1
assert max_path_sum([[1, 2], [3, 4]], 4) == 14
assert max_path_sum([[1, -9, 1], [-9, -9, -9], [1, -9, 1]], 2) == -8
assert max_path_sum([[1, -9, 1], [-9, -9, -9], [1, -9, 1]], 1) == 1
assert max_path_sum([[0, 0], [0, 0]], 100) == 0
assert max_path_sum([[1, 2], [3, 4]], 1000) == 3500
g = [[(i * 7 + j * 3) % 10 - 5 for j in range(6)] for i in range(6)]
import itertools
def brute(g, k):
    n = len(g)
    best = None
    def go(i, j, left, s):
        nonlocal best
        if left == 0:
            best = s if best is None or s > best else best
            return
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            a, b = i + di, j + dj
            if 0 <= a < n and 0 <= b < n:
                go(a, b, left - 1, s + g[a][b])
    for i in range(n):
        for j in range(n):
            go(i, j, k - 1, g[i][j])
    return best
for k in range(1, 7):
    assert max_path_sum(g, k) == brute(g, k), k
big = [[1] * 30 for _ in range(30)]
assert max_path_sum(big, 1000) == 1000
''')
