# parents: HumanEval/126 (is_sorted), /129 (minPath), /130 (tri), /132 (is_nested), /139 (special_factorial)
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------------------------------------------------------- HumanEval/126
add(126, '''def is_sorted_desc(lst):
    \'\'\'
    Given a list of numbers, return whether or not they are sorted
    in descending order. If list has more than 2 duplicates of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted_desc([5]) ➞ True
    is_sorted_desc([5, 4, 3, 2, 1]) ➞ True
    is_sorted_desc([5, 3, 4, 2, 1]) ➞ False
    is_sorted_desc([6, 5, 5, 4]) ➞ True
    is_sorted_desc([6, 5, 5, 5, 4]) ➞ False
    is_sorted_desc([]) ➞ True
    \'\'\'
''', '''
    count = dict()
    for x in lst:
        count[x] = count.get(x, 0) + 1
        if count[x] > 2:
            return False
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
''', '''
import itertools
def ref(l):
    return all(l.count(v) <= 2 for v in l) and l == sorted(l, reverse=True)
assert is_sorted_desc([]) is True
assert is_sorted_desc([5]) is True
assert is_sorted_desc([5, 4, 3, 2, 1]) is True
assert is_sorted_desc([5, 3, 4, 2, 1]) is False
assert is_sorted_desc([6, 5, 5, 4]) is True
assert is_sorted_desc([6, 5, 5, 5, 4]) is False
assert is_sorted_desc([1, 2, 3]) is False
assert is_sorted_desc([3, 3]) is True
assert is_sorted_desc([3, 3, 3]) is False
assert is_sorted_desc([3, 3, 2, 2, 1, 1]) is True
assert is_sorted_desc([3, 2, 3]) is False
assert is_sorted_desc([2, 2, 3]) is False
assert is_sorted_desc([0, 0]) is True
assert is_sorted_desc([10, 9, 0]) is True
assert is_sorted_desc([4, 4, 3, 3, 3]) is False
assert is_sorted_desc([5, 5, 4, 4, 5]) is False
for n in range(0, 8):
    for t in itertools.product(range(4), repeat=n):
        assert is_sorted_desc(list(t)) == ref(list(t)), t
assert is_sorted_desc(list(range(100000, 0, -1))) is True
assert is_sorted_desc(list(range(100000, 0, -1)) + [5]) is False
''')

add(126, '''def is_strictly_sorted(lst):
    \'\'\'
    Given a list of numbers, return whether or not they are sorted
    in strictly ascending order. If list has any duplicate numbers,
    return False. The list may contain negative integers.

    Examples
    is_strictly_sorted([5]) ➞ True
    is_strictly_sorted([1, 2, 3, 4, 5]) ➞ True
    is_strictly_sorted([1, 3, 2, 4, 5]) ➞ False
    is_strictly_sorted([1, 2, 2, 3]) ➞ False
    is_strictly_sorted([-3, -1, 0, 4]) ➞ True
    is_strictly_sorted([]) ➞ True
    \'\'\'
''', '''
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
''', '''
import itertools
assert is_strictly_sorted([]) is True
assert is_strictly_sorted([5]) is True
assert is_strictly_sorted([1, 2, 3, 4, 5]) is True
assert is_strictly_sorted([1, 3, 2, 4, 5]) is False
assert is_strictly_sorted([1, 2, 2, 3]) is False
assert is_strictly_sorted([-3, -1, 0, 4]) is True
assert is_strictly_sorted([-1, -1]) is False
assert is_strictly_sorted([0, 0]) is False
assert is_strictly_sorted([2, 1]) is False
assert is_strictly_sorted([-5, -6]) is False
assert is_strictly_sorted([1, 2, 3, 3]) is False
assert is_strictly_sorted([1, 1, 2, 3]) is False
assert is_strictly_sorted([-10 ** 18, 0, 10 ** 18]) is True
assert is_strictly_sorted([1, 2, 3, 1]) is False
for n in range(0, 7):
    for t in itertools.product(range(-1, 3), repeat=n):
        l = list(t)
        assert is_strictly_sorted(l) == (l == sorted(set(l))), t
assert is_strictly_sorted(list(range(200000))) is True
assert is_strictly_sorted(list(range(200000)) + [199999]) is False
''')

add(126, '''def is_sorted_limit(lst, limit):
    \'\'\'
    Given a list of numbers and a positive integer limit, return whether or not the numbers
    are sorted in ascending order (equal neighbours are allowed). If some number appears
    in the list more than limit times, return False. The list may contain negative integers.

    Examples
    is_sorted_limit([5], 1) ➞ True
    is_sorted_limit([1, 2, 2, 3], 1) ➞ False
    is_sorted_limit([1, 2, 2, 3], 2) ➞ True
    is_sorted_limit([1, 1, 1, 2], 2) ➞ False
    is_sorted_limit([3, 1, 2], 5) ➞ False
    is_sorted_limit([], 1) ➞ True
    \'\'\'
''', '''
    count = dict()
    for x in lst:
        count[x] = count.get(x, 0) + 1
        if count[x] > limit:
            return False
    return lst == sorted(lst)
''', '''
import itertools
def ref(l, k):
    return all(l.count(v) <= k for v in l) and l == sorted(l)
assert is_sorted_limit([], 1) is True
assert is_sorted_limit([5], 1) is True
assert is_sorted_limit([1, 2, 2, 3], 1) is False
assert is_sorted_limit([1, 2, 2, 3], 2) is True
assert is_sorted_limit([1, 1, 1, 2], 2) is False
assert is_sorted_limit([1, 1, 1, 2], 3) is True
assert is_sorted_limit([3, 1, 2], 5) is False
assert is_sorted_limit([-3, -3, -1], 2) is True
assert is_sorted_limit([-1, -3], 2) is False
assert is_sorted_limit([0, 0, 0, 0], 3) is False
assert is_sorted_limit([0, 0, 0, 0], 4) is True
assert is_sorted_limit([1, 2, 3, 1], 2) is False
assert is_sorted_limit([1, 1, 2, 2, 3, 3], 2) is True
assert is_sorted_limit([1, 1, 2, 2, 3, 3], 1) is False
for n in range(0, 7):
    for t in itertools.product(range(-1, 3), repeat=n):
        for k in (1, 2, 3):
            assert is_sorted_limit(list(t), k) == ref(list(t), k), (t, k)
assert is_sorted_limit([7] * 100000, 100000) is True
assert is_sorted_limit([7] * 100000, 99999) is False
''')

add(126, '''def is_sorted_with_negatives(lst):
    \'\'\'
    Given a list of integers (they may be negative), return whether or not they are sorted
    in ascending order. If list has more than 2 duplicates of the same
    number, return False.

    Examples
    is_sorted_with_negatives([-5]) ➞ True
    is_sorted_with_negatives([-3, -2, 0, 4]) ➞ True
    is_sorted_with_negatives([0, -1, 2]) ➞ False
    is_sorted_with_negatives([-2, -2, 1]) ➞ True
    is_sorted_with_negatives([-2, -2, -2, 1]) ➞ False
    is_sorted_with_negatives([]) ➞ True
    \'\'\'
''', '''
    count = dict()
    for x in lst:
        count[x] = count.get(x, 0) + 1
        if count[x] > 2:
            return False
    return lst == sorted(lst)
''', '''
import itertools
def ref(l):
    return all(l.count(v) <= 2 for v in l) and l == sorted(l)
assert is_sorted_with_negatives([]) is True
assert is_sorted_with_negatives([-5]) is True
assert is_sorted_with_negatives([-3, -2, 0, 4]) is True
assert is_sorted_with_negatives([0, -1, 2]) is False
assert is_sorted_with_negatives([-2, -2, 1]) is True
assert is_sorted_with_negatives([-2, -2, -2, 1]) is False
assert is_sorted_with_negatives([-1, -2]) is False
assert is_sorted_with_negatives([-10, 10]) is True
assert is_sorted_with_negatives([0, 0]) is True
assert is_sorted_with_negatives([0, 0, 0]) is False
assert is_sorted_with_negatives([-1, 0, -1]) is False
assert is_sorted_with_negatives([-3, -3, -2, -2, -1, -1]) is True
assert is_sorted_with_negatives([1, 1, 1, 1]) is False
assert is_sorted_with_negatives([-10 ** 9, 10 ** 9]) is True
for n in range(0, 8):
    for t in itertools.product(range(-1, 3), repeat=n):
        assert is_sorted_with_negatives(list(t)) == ref(list(t)), t
assert is_sorted_with_negatives(list(range(-100000, 100000))) is True
assert is_sorted_with_negatives(list(range(-100000, 100000)) + [0]) is False
''')

add(126, '''def is_sorted_words(words):
    \'\'\'
    Given a list of lowercase words, return whether or not they are sorted
    in ascending alphabetical (lexicographic) order. If some word appears in the list
    more than 2 times, return False.

    Examples
    is_sorted_words(['pear']) ➞ True
    is_sorted_words(['apple', 'banana', 'cherry']) ➞ True
    is_sorted_words(['banana', 'apple']) ➞ False
    is_sorted_words(['a', 'a', 'b']) ➞ True
    is_sorted_words(['a', 'a', 'a', 'b']) ➞ False
    is_sorted_words(['a', 'ab', 'abc']) ➞ True
    is_sorted_words([]) ➞ True
    \'\'\'
''', '''
    count = dict()
    for w in words:
        count[w] = count.get(w, 0) + 1
        if count[w] > 2:
            return False
    return all(words[i] <= words[i + 1] for i in range(len(words) - 1))
''', '''
import itertools
def ref(l):
    return all(l.count(v) <= 2 for v in l) and l == sorted(l)
assert is_sorted_words([]) is True
assert is_sorted_words(["pear"]) is True
assert is_sorted_words(["apple", "banana", "cherry"]) is True
assert is_sorted_words(["banana", "apple"]) is False
assert is_sorted_words(["a", "a", "b"]) is True
assert is_sorted_words(["a", "a", "a", "b"]) is False
assert is_sorted_words(["a", "ab", "abc"]) is True
assert is_sorted_words(["abc", "ab"]) is False
assert is_sorted_words(["", "a"]) is True
assert is_sorted_words(["a", ""]) is False
assert is_sorted_words(["", ""]) is True
assert is_sorted_words(["b", "a", "b"]) is False
assert is_sorted_words(["z" * 1000, "z" * 1001]) is True
assert is_sorted_words(["ab", "b", "ba"]) is True
assert is_sorted_words(["10", "9"]) is True
assert is_sorted_words(["9", "10"]) is False
for n in range(0, 6):
    for t in itertools.product(["", "a", "ab", "b"], repeat=n):
        assert is_sorted_words(list(t)) == ref(list(t)), t
words = ["w%06d" % i for i in range(100000)]
assert is_sorted_words(words) is True
assert is_sorted_words(words[::-1]) is False
''')

# ---------------------------------------------------------------- HumanEval/129
add(129, '''def max_path(grid, k):
    """
    Given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly once,
    find the lexicographically largest list of values collected by a path of k cells.
    A path starts at any cell and each step moves to an edge-adjacent cell (cells may repeat).

    Example:

        Input: grid = [[1, 2], [3, 4]], k = 3
        Output: [4, 3, 4]
    """
''', '''
    n = len(grid)
    r, c = next((i, j) for i in range(n) for j in range(n) if grid[i][j] == n * n)
    near = [grid[i][j] for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)) if 0 <= i < n and 0 <= j < n]
    return [n * n if i % 2 == 0 else max(near) for i in range(k)]
''', '''
import random
def brute(grid, k):
    n = len(grid)
    best = None
    def go(r, c, path):
        nonlocal best
        path = path + [grid[r][c]]
        if len(path) == k:
            if best is None or path > best:
                best = path
            return
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < n and 0 <= cc < n:
                go(rr, cc, path)
    for i in range(n):
        for j in range(n):
            go(i, j, [])
    return best
assert max_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [9, 8, 9]
assert max_path([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == [9]
assert max_path([[1, 2], [3, 4]], 1) == [4]
assert max_path([[1, 2], [3, 4]], 2) == [4, 3]
assert max_path([[1, 2], [3, 4]], 3) == [4, 3, 4]
assert max_path([[1, 2], [3, 4]], 4) == [4, 3, 4, 3]
assert max_path([[4, 3], [2, 1]], 2) == [4, 3]
assert max_path([[1, 4], [3, 2]], 5) == [4, 2, 4, 2, 4]
assert max_path([[9, 1, 2], [3, 4, 5], [6, 7, 8]], 4) == [9, 3, 9, 3]
assert max_path([[1, 2, 3], [4, 9, 6], [7, 8, 5]], 3) == [9, 8, 9]
assert max_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [9]
assert max_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) == [9, 8]
random.seed(91)
for _ in range(120):
    n = random.randint(2, 4)
    vals = list(range(1, n * n + 1))
    random.shuffle(vals)
    g = [vals[i * n:(i + 1) * n] for i in range(n)]
    k = random.randint(1, 6)
    assert max_path(g, k) == brute(g, k), (g, k)
n = 300
g = [[i * n + j + 1 for j in range(n)] for i in range(n)]
r = max_path(g, 100000)
assert len(r) == 100000 and r[0] == n * n and r[1] == n * n - 1
''')

add(129, '''def min_path_from(grid, k, row, col):
    """
    Given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly once and
    a start cell (row, col), find the lexicographically smallest list of values collected by a
    path of k cells that starts at the start cell. Each step moves to an edge-adjacent cell
    (cells may repeat).

    Example:

        Input: grid = [[1, 2], [3, 4]], k = 3, row = 1, col = 1
        Output: [4, 2, 1]
    """
''', '''
    n = len(grid)
    r, c = row, col
    path = [grid[r][c]]
    for _ in range(k - 1):
        near = [(i, j) for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)) if 0 <= i < n and 0 <= j < n]
        r, c = min(near, key=lambda p: grid[p[0]][p[1]])
        path.append(grid[r][c])
    return path
''', '''
import random
def brute(grid, k, r0, c0):
    n = len(grid)
    best = None
    def go(r, c, path):
        nonlocal best
        path = path + [grid[r][c]]
        if len(path) == k:
            if best is None or path < best:
                best = path
            return
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < n and 0 <= cc < n:
                go(rr, cc, path)
    go(r0, c0, [])
    return best
assert min_path_from([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 1, 1) == [5, 2, 1, 2]
assert min_path_from([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1, 0, 1) == [9]
assert min_path_from([[1, 2], [3, 4]], 1, 1, 1) == [4]
assert min_path_from([[1, 2], [3, 4]], 2, 1, 1) == [4, 2]
assert min_path_from([[1, 2], [3, 4]], 3, 1, 1) == [4, 2, 1]
assert min_path_from([[1, 2], [3, 4]], 5, 1, 1) == [4, 2, 1, 2, 1]
assert min_path_from([[1, 2], [3, 4]], 3, 0, 0) == [1, 2, 1]
assert min_path_from([[9, 8, 7], [6, 1, 2], [3, 4, 5]], 4, 0, 0) == [9, 6, 1, 2]
assert min_path_from([[9, 8, 7], [6, 1, 2], [3, 4, 5]], 3, 2, 2) == [5, 2, 1]
assert min_path_from([[9, 8, 7], [6, 1, 2], [3, 4, 5]], 1, 2, 0) == [3]
assert min_path_from([[1, 3], [2, 4]], 4, 0, 1) == [3, 1, 2, 1]
random.seed(92)
for _ in range(150):
    n = random.randint(2, 4)
    vals = list(range(1, n * n + 1))
    random.shuffle(vals)
    g = [vals[i * n:(i + 1) * n] for i in range(n)]
    k = random.randint(1, 7)
    r, c = random.randrange(n), random.randrange(n)
    assert min_path_from(g, k, r, c) == brute(g, k, r, c), (g, k, r, c)
n = 300
g = [[i * n + j + 1 for j in range(n)] for i in range(n)]
r = min_path_from(g, 100000, n - 1, n - 1)
assert len(r) == 100000 and r[0] == n * n and r[-1] in (1, n + 1, 2)
''')

add(129, '''def min_path_sum(grid, k):
    """
    Given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly once,
    find the lexicographically smallest list of values collected by a path of k cells and
    return the sum of that list. A path starts at any cell and each step moves to an
    edge-adjacent cell (cells may repeat).

    Example:

        Input: grid = [[1, 2], [3, 4]], k = 3
        Output: 4
    """
''', '''
    n = len(grid)
    r, c = next((i, j) for i in range(n) for j in range(n) if grid[i][j] == 1)
    mn = min(grid[i][j] for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)) if 0 <= i < n and 0 <= j < n)
    return (k + 1) // 2 + (k // 2) * mn
''', '''
import random
def brute(grid, k):
    n = len(grid)
    best = None
    def go(r, c, path):
        nonlocal best
        path = path + [grid[r][c]]
        if len(path) == k:
            if best is None or path < best:
                best = path
            return
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < n and 0 <= cc < n:
                go(rr, cc, path)
    for i in range(n):
        for j in range(n):
            go(i, j, [])
    return sum(best)
assert min_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == 4
assert min_path_sum([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 4) == 10
assert min_path_sum([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == 1
assert min_path_sum([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 2) == 5
assert min_path_sum([[1, 2], [3, 4]], 1) == 1
assert min_path_sum([[1, 2], [3, 4]], 2) == 3
assert min_path_sum([[1, 2], [3, 4]], 10) == 5 + 5 * 2
assert min_path_sum([[4, 3], [2, 1]], 3) == 1 + 2 + 1
assert min_path_sum([[2, 4], [3, 1]], 4) == 1 + 3 + 1 + 3
assert min_path_sum([[1, 4], [3, 2]], 3) == 1 + 3 + 1
assert min_path_sum([[9, 8, 7], [6, 1, 2], [3, 4, 5]], 5) == 1 * 3 + 2 * 2
random.seed(93)
for _ in range(120):
    n = random.randint(2, 4)
    vals = list(range(1, n * n + 1))
    random.shuffle(vals)
    g = [vals[i * n:(i + 1) * n] for i in range(n)]
    k = random.randint(1, 7)
    assert min_path_sum(g, k) == brute(g, k), (g, k)
assert min_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10 ** 9) == 500000000 * 1 + 500000000 * 2
assert min_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10 ** 9 + 1) == 500000001 * 1 + 500000000 * 2
''')

add(129, '''def grid_neighbors(grid, value):
    """
    Given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly once,
    return the sorted values of the cells that share an edge with the cell containing
    the given value (an empty list if it is not in the grid).

    Examples:

        Input: grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], value = 5
        Output: [2, 4, 6, 8]

        Input: grid = [[1, 2], [3, 4]], value = 4
        Output: [2, 3]
    """
''', '''
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == value:
                near = ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
                return sorted(grid[a][b] for a, b in near if 0 <= a < n and 0 <= b < n)
    return []
''', '''
import random
assert grid_neighbors([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [2, 4, 6, 8]
assert grid_neighbors([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 5) == [4, 9]
assert grid_neighbors([[1, 2], [3, 4]], 4) == [2, 3]
assert grid_neighbors([[1, 2], [3, 4]], 1) == [2, 3]
assert grid_neighbors([[1, 2], [3, 4]], 2) == [1, 4]
assert grid_neighbors([[1, 2], [3, 4]], 3) == [1, 4]
assert grid_neighbors([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [2, 4]
assert grid_neighbors([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == [6, 8]
assert grid_neighbors([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) == [1, 3, 5]
assert grid_neighbors([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 6) == [3, 5, 9]
assert grid_neighbors([[9, 8, 7], [6, 1, 2], [3, 4, 5]], 1) == [2, 4, 6, 8]
assert grid_neighbors([[1, 2], [3, 4]], 10) == []
random.seed(94)
for _ in range(200):
    n = random.randint(2, 6)
    vals = list(range(1, n * n + 1))
    random.shuffle(vals)
    g = [vals[i * n:(i + 1) * n] for i in range(n)]
    v = random.randint(1, n * n)
    pos = {g[i][j]: (i, j) for i in range(n) for j in range(n)}[v]
    exp = sorted(g[a][b] for a in range(n) for b in range(n) if abs(a - pos[0]) + abs(b - pos[1]) == 1)
    assert grid_neighbors(g, v) == exp
    assert 2 <= len(exp) <= 4
n = 400
g = [[i * n + j + 1 for j in range(n)] for i in range(n)]
assert grid_neighbors(g, 200 * n + 200 + 1) == sorted([199 * n + 201, 201 * n + 201, 200 * n + 200, 200 * n + 202])
''')

add(129, '''def find_cell(grid, value):
    """
    Given an N x N grid (N >= 2) that contains every integer from 1 to N * N exactly once,
    return a tuple (row, col) with the 0-indexed position of the cell containing the given value,
    or (-1, -1) if the value is not in the grid.

    Examples:

        Input: grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], value = 5
        Output: (1, 1)

        Input: grid = [[1, 2], [3, 4]], value = 7
        Output: (-1, -1)
    """
''', '''
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == value:
                return (i, j)
    return (-1, -1)
''', '''
import random
assert find_cell([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == (1, 1)
assert find_cell([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 2) == (2, 2)
assert find_cell([[1, 2], [3, 4]], 7) == (-1, -1)
assert find_cell([[1, 2], [3, 4]], 1) == (0, 0)
assert find_cell([[1, 2], [3, 4]], 2) == (0, 1)
assert find_cell([[1, 2], [3, 4]], 3) == (1, 0)
assert find_cell([[1, 2], [3, 4]], 4) == (1, 1)
assert find_cell([[1, 2], [3, 4]], 0) == (-1, -1)
assert find_cell([[1, 2], [3, 4]], -1) == (-1, -1)
assert find_cell([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == (2, 2)
assert find_cell([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 7) == (2, 0)
assert find_cell([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == (0, 2)
assert isinstance(find_cell([[1, 2], [3, 4]], 4), tuple)
random.seed(95)
for _ in range(200):
    n = random.randint(2, 7)
    vals = list(range(1, n * n + 1))
    random.shuffle(vals)
    g = [vals[i * n:(i + 1) * n] for i in range(n)]
    v = random.randint(0, n * n + 1)
    r, c = find_cell(g, v)
    if 1 <= v <= n * n:
        assert g[r][c] == v
    else:
        assert (r, c) == (-1, -1)
n = 500
g = [[i * n + j + 1 for j in range(n)] for i in range(n)]
assert find_cell(g, n * n) == (n - 1, n - 1)
assert find_cell(g, n * n + 1) == (-1, -1)
''')

# ---------------------------------------------------------------- HumanEval/130
add(130, '''def pell(n):
    """Pell numbers are a sequence that every mathematician has met in Diophantine equations.
    Pell sequence is defined by the recurrence:
    pell(0) = 0
    pell(1) = 1
    pell(n) = 2 * pell(n - 1) + pell(n - 2), if n >= 2.
    For example:
    pell(2) = 2 * 1 + 0 = 2
    pell(3) = 2 * 2 + 1 = 5
    You are given a non-negative integer number n, you have to a return a list of the
    first n + 1 numbers of the Pell sequence.
    Examples:
    pell(3) = [0, 1, 2, 5]
    """
''', '''
    if n == 0:
        return [0]
    ans = [0, 1]
    for i in range(2, n + 1):
        ans.append(2 * ans[-1] + ans[-2])
    return ans
''', '''
def ref(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return 2 * ref(k - 1) + ref(k - 2)
assert pell(0) == [0]
assert pell(1) == [0, 1]
assert pell(2) == [0, 1, 2]
assert pell(3) == [0, 1, 2, 5]
assert pell(4) == [0, 1, 2, 5, 12]
assert pell(5) == [0, 1, 2, 5, 12, 29]
assert pell(6) == [0, 1, 2, 5, 12, 29, 70]
assert pell(7)[-1] == 169
for n in range(0, 20):
    r = pell(n)
    assert r == [ref(i) for i in range(n + 1)], n
    assert len(r) == n + 1
    assert all(isinstance(x, int) for x in r)
big = pell(5000)
assert len(big) == 5001
assert big[-1] == 2 * big[-2] + big[-3]
assert 10 ** 1900 < big[5000] < 10 ** 1920
''')

add(130, '''def padovan(n):
    """The Padovan sequence is defined by the recurrence:
    padovan(0) = 1
    padovan(1) = 1
    padovan(2) = 1
    padovan(n) = padovan(n - 2) + padovan(n - 3), if n >= 3.
    For example:
    padovan(3) = padovan(1) + padovan(0) = 2
    You are given a non-negative integer number n, you have to a return a list of the
    first n + 1 numbers of the Padovan sequence.
    Examples:
    padovan(5) = [1, 1, 1, 2, 2, 3]
    """
''', '''
    ans = [1, 1, 1]
    if n < 3:
        return ans[:n + 1]
    for i in range(3, n + 1):
        ans.append(ans[i - 2] + ans[i - 3])
    return ans
''', '''
def ref(k):
    if k < 3:
        return 1
    return ref(k - 2) + ref(k - 3)
assert padovan(0) == [1]
assert padovan(1) == [1, 1]
assert padovan(2) == [1, 1, 1]
assert padovan(3) == [1, 1, 1, 2]
assert padovan(4) == [1, 1, 1, 2, 2]
assert padovan(5) == [1, 1, 1, 2, 2, 3]
assert padovan(6) == [1, 1, 1, 2, 2, 3, 4]
assert padovan(9) == [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
assert padovan(10)[-1] == 12
for n in range(0, 25):
    r = padovan(n)
    assert r == [ref(i) for i in range(n + 1)], n
    assert len(r) == n + 1
big = padovan(10000)
assert len(big) == 10001
assert big[-1] == big[-3] + big[-4]
assert padovan(2) is not padovan(2)
''')

add(130, '''def look_ahead_seq(n):
    """Consider a sequence whose elements depend on their neighbours:
    seq(0) = 1
    seq(n) = 1 + n / 2, if n is even.
    seq(n) = seq(n - 1) + seq(n + 1), if n is odd.
    For example:
    seq(2) = 1 + (2 / 2) = 2
    seq(4) = 3
    seq(3) = seq(2) + seq(4) = 2 + 3 = 5
    You are given a non-negative integer number n, you have to a return a list of the
    first n + 1 numbers of the sequence.
    Examples:
    look_ahead_seq(3) = [1, 3, 2, 5]
    """
''', '''
    def even(i):
        return 1 + i // 2

    return [even(i) if i % 2 == 0 else even(i - 1) + even(i + 1) for i in range(n + 1)]
''', '''
def ref(k):
    if k == 0:
        return 1
    if k % 2 == 0:
        return 1 + k // 2
    return ref(k - 1) + ref(k + 1)
assert look_ahead_seq(0) == [1]
assert look_ahead_seq(1) == [1, 3]
assert look_ahead_seq(2) == [1, 3, 2]
assert look_ahead_seq(3) == [1, 3, 2, 5]
assert look_ahead_seq(4) == [1, 3, 2, 5, 3]
assert look_ahead_seq(5) == [1, 3, 2, 5, 3, 7]
assert look_ahead_seq(6) == [1, 3, 2, 5, 3, 7, 4]
assert look_ahead_seq(7)[-1] == 9
for n in range(0, 40):
    r = look_ahead_seq(n)
    assert r == [ref(i) for i in range(n + 1)], n
    assert len(r) == n + 1
    assert all(type(x) is int for x in r)
big = look_ahead_seq(200000)
assert len(big) == 200001 and big[200000] == 100001 and big[199999] == 100000 + 100001
''')

add(130, '''def tribonacci(n):
    """Tribonacci sequence is defined by the recurrence:
    tribonacci(0) = 0
    tribonacci(1) = 0
    tribonacci(2) = 1
    tribonacci(n) = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3), if n >= 3.
    For example:
    tribonacci(3) = 1 + 0 + 0 = 1
    You are given a non-negative integer number n, you have to a return a list of the
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tribonacci(5) = [0, 0, 1, 1, 2, 4]
    """
''', '''
    ans = [0, 0, 1]
    if n < 3:
        return ans[:n + 1]
    for i in range(3, n + 1):
        ans.append(ans[-1] + ans[-2] + ans[-3])
    return ans
''', '''
def ref(k):
    if k < 2:
        return 0
    if k == 2:
        return 1
    return ref(k - 1) + ref(k - 2) + ref(k - 3)
assert tribonacci(0) == [0]
assert tribonacci(1) == [0, 0]
assert tribonacci(2) == [0, 0, 1]
assert tribonacci(3) == [0, 0, 1, 1]
assert tribonacci(4) == [0, 0, 1, 1, 2]
assert tribonacci(5) == [0, 0, 1, 1, 2, 4]
assert tribonacci(6) == [0, 0, 1, 1, 2, 4, 7]
assert tribonacci(10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
for n in range(0, 22):
    r = tribonacci(n)
    assert r == [ref(i) for i in range(n + 1)], n
    assert len(r) == n + 1
big = tribonacci(3000)
assert len(big) == 3001 and big[-1] == big[-2] + big[-3] + big[-4]
a = tribonacci(2)
a.append(5)
assert tribonacci(2) == [0, 0, 1]
''')

add(130, '''def jacobsthal(n):
    """Jacobsthal sequence is defined by the recurrence:
    jacobsthal(0) = 0
    jacobsthal(1) = 1
    jacobsthal(n) = jacobsthal(n - 1) + 2 * jacobsthal(n - 2), if n >= 2.
    For example:
    jacobsthal(2) = 1 + 2 * 0 = 1
    jacobsthal(3) = 1 + 2 * 1 = 3
    You are given a non-negative integer number n, you have to a return a list of the
    first n + 1 numbers of the Jacobsthal sequence.
    Examples:
    jacobsthal(5) = [0, 1, 1, 3, 5, 11]
    """
''', '''
    if n == 0:
        return [0]
    ans = [0, 1]
    for i in range(2, n + 1):
        ans.append(ans[-1] + 2 * ans[-2])
    return ans
''', '''
def ref(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return ref(k - 1) + 2 * ref(k - 2)
assert jacobsthal(0) == [0]
assert jacobsthal(1) == [0, 1]
assert jacobsthal(2) == [0, 1, 1]
assert jacobsthal(3) == [0, 1, 1, 3]
assert jacobsthal(4) == [0, 1, 1, 3, 5]
assert jacobsthal(5) == [0, 1, 1, 3, 5, 11]
assert jacobsthal(8) == [0, 1, 1, 3, 5, 11, 21, 43, 85]
for n in range(0, 22):
    r = jacobsthal(n)
    assert r == [ref(i) for i in range(n + 1)], n
    assert len(r) == n + 1
    assert all(3 * r[i] == 2 ** i - (-1) ** i for i in range(n + 1))
big = jacobsthal(5000)
assert 3 * big[-1] == 2 ** 5000 - 1
assert len(big) == 5001
''')

# ---------------------------------------------------------------- HumanEval/132
add(132, '''def max_nesting_depth(string):
    \'\'\'
    Create a function that takes a string as input which contains only square brackets.
    The function should return the maximal nesting depth of the brackets, where every '['
    increases the depth by one and every ']' decreases it by one, but the depth never goes
    below zero (a ']' without a matching '[' before it is ignored).

    max_nesting_depth('[[]]') ➞ 2
    max_nesting_depth('[][]') ➞ 1
    max_nesting_depth('') ➞ 0
    max_nesting_depth(']]][[[') ➞ 3
    max_nesting_depth('[[[]') ➞ 3
    \'\'\'
''', '''
    depth = best = 0
    for ch in string:
        if ch == "[":
            depth += 1
            best = max(best, depth)
        elif depth > 0:
            depth -= 1
    return best
''', '''
import itertools
def ref(s):
    stack = 0
    best = 0
    for ch in s:
        if ch == "[":
            stack += 1
        else:
            stack = max(0, stack - 1)
        best = max(best, stack)
    return best
assert max_nesting_depth("[[]]") == 2
assert max_nesting_depth("[][]") == 1
assert max_nesting_depth("") == 0
assert max_nesting_depth("]]][[[") == 3
assert max_nesting_depth("[[[]") == 3
assert max_nesting_depth("[") == 1
assert max_nesting_depth("]") == 0
assert max_nesting_depth("[]") == 1
assert max_nesting_depth("[[][[]]]") == 3
assert max_nesting_depth("][[]") == 2
assert max_nesting_depth("[]][[[]") == 3
assert max_nesting_depth("[[]][[]]") == 2
assert max_nesting_depth("[" * 100000) == 100000
assert max_nesting_depth("[" * 50000 + "]" * 50000) == 50000
assert max_nesting_depth("[]" * 100000) == 1
for n in range(0, 13):
    for t in itertools.product("[]", repeat=n):
        s = "".join(t)
        assert max_nesting_depth(s) == ref(s), s
''')

add(132, '''def is_balanced(string):
    \'\'\'
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if the brackets in the string form a valid
    sequence: every '[' is closed by a later ']' and every ']' closes an earlier '['.
    The empty string is valid.

    is_balanced('[[]]') ➞ True
    is_balanced('[]]]]]]][[[[[]') ➞ False
    is_balanced('[][]') ➞ True
    is_balanced('[') ➞ False
    is_balanced('][') ➞ False
    is_balanced('') ➞ True
    \'\'\'
''', '''
    depth = 0
    for ch in string:
        if ch == "[":
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                return False
    return depth == 0
''', '''
import itertools
def ref(s):
    while "[]" in s:
        s = s.replace("[]", "", 1)
    return s == ""
assert is_balanced("[[]]") is True
assert is_balanced("[]]]]]]][[[[[]") is False
assert is_balanced("[][]") is True
assert is_balanced("[") is False
assert is_balanced("]") is False
assert is_balanced("][") is False
assert is_balanced("") is True
assert is_balanced("[]") is True
assert is_balanced("[[]") is False
assert is_balanced("[]]") is False
assert is_balanced("[[][]]") is True
assert is_balanced("[[]][[") is False
assert is_balanced("]]][[[") is False
assert is_balanced("[" * 50000 + "]" * 50000) is True
assert is_balanced("[" * 50000 + "]" * 49999) is False
assert is_balanced("[]" * 100000) is True
for n in range(0, 13):
    for t in itertools.product("[]", repeat=n):
        s = "".join(t)
        assert is_balanced(s) == ref(s), s
''')

add(132, '''def has_nesting_depth(string, k):
    \'\'\'
    Create a function that takes a string of square brackets and a positive integer k.
    Return True if and only if the string contains a subsequence (skipping characters is
    allowed) equal to '[' * k + ']' * k.

    has_nesting_depth('[[]]', 2) ➞ True
    has_nesting_depth('[][]', 2) ➞ False
    has_nesting_depth('[[]][[', 2) ➞ True
    \'\'\'
''', '''
    opens = [i for i, ch in enumerate(string) if ch == "["]
    closes = [i for i, ch in enumerate(string) if ch == "]"]
    closes.reverse()
    pairs = 0
    for idx in opens:
        if pairs < len(closes) and idx < closes[pairs]:
            pairs += 1
    return pairs >= k
''', '''
import itertools
def is_subseq(pat, s):
    it = iter(s)
    return all(c in it for c in pat)
assert has_nesting_depth("[[]]", 2) is True
assert has_nesting_depth("[][]", 2) is False
assert has_nesting_depth("[[]][[", 2) is True
assert has_nesting_depth("[]]]]]]][[[[[]", 2) is False
assert has_nesting_depth("[[[]]]", 3) is True
assert has_nesting_depth("[[[]]]", 4) is False
assert has_nesting_depth("[]", 1) is True
assert has_nesting_depth("][", 1) is False
assert has_nesting_depth("", 1) is False
assert has_nesting_depth("[[", 1) is False
assert has_nesting_depth("]]", 1) is False
assert has_nesting_depth("[[[]", 1) is True
assert has_nesting_depth("[[[]", 2) is False
assert has_nesting_depth("[][][]", 3) is False
assert has_nesting_depth("[[][][]]", 2) is True
assert has_nesting_depth("[" * 50000 + "]" * 50000, 50000) is True
assert has_nesting_depth("[" * 50000 + "]" * 50000, 50001) is False
assert has_nesting_depth("[]" * 50000, 2) is True
assert has_nesting_depth("[]" * 50000, 50000) is False
for n in range(0, 11):
    for t in itertools.product("[]", repeat=n):
        s = "".join(t)
        for k in (1, 2, 3):
            assert has_nesting_depth(s, k) == is_subseq("[" * k + "]" * k, s), (s, k)
''')

add(132, '''def longest_balanced_subsequence(string):
    \'\'\'
    Create a function that takes a string as input which contains only square brackets.
    The function should return the length of the longest subsequence of the string
    (some characters may be skipped, the order is kept) that is a valid sequence of brackets:
    every '[' is closed by a later ']' and every ']' closes an earlier '['.

    longest_balanced_subsequence('[[]]') ➞ 4
    longest_balanced_subsequence('[]]]]]]][[[[[]') ➞ 4
    longest_balanced_subsequence('][') ➞ 0
    longest_balanced_subsequence('[[[') ➞ 0
    longest_balanced_subsequence('[]][[]') ➞ 4
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
    return 2 * pairs
''', '''
import itertools
def ref(s):
    n = len(s)
    best = 0
    for mask in range(1 << n):
        sub = [s[i] for i in range(n) if mask >> i & 1]
        d = 0
        ok = True
        for ch in sub:
            d += 1 if ch == "[" else -1
            if d < 0:
                ok = False
                break
        if ok and d == 0:
            best = max(best, len(sub))
    return best
assert longest_balanced_subsequence("[[]]") == 4
assert longest_balanced_subsequence("[]]]]]]][[[[[]") == 4
assert longest_balanced_subsequence("][") == 0
assert longest_balanced_subsequence("[[[") == 0
assert longest_balanced_subsequence("[]][[]") == 4
assert longest_balanced_subsequence("") == 0
assert longest_balanced_subsequence("[") == 0
assert longest_balanced_subsequence("]") == 0
assert longest_balanced_subsequence("[]") == 2
assert longest_balanced_subsequence("]]][[[") == 0
assert longest_balanced_subsequence("[[]") == 2
assert longest_balanced_subsequence("[]]") == 2
assert longest_balanced_subsequence("[" * 50000 + "]" * 49999) == 99998
assert longest_balanced_subsequence("][" * 50000) == 99998
for n in range(0, 10):
    for t in itertools.product("[]", repeat=n):
        s = "".join(t)
        assert longest_balanced_subsequence(s) == ref(s), s
''')

add(132, '''def first_unbalanced_index(string):
    \'\'\'
    Create a function that takes a string as input which contains only square brackets.
    The function should return -1 if the brackets form a valid sequence (every '[' is closed
    by a later ']' and every ']' closes an earlier '['). Otherwise it should return the index
    of the first ']' that has no matching '[' before it; if there is no such ']' but some '['
    stay unclosed at the end, it should return the length of the string.

    first_unbalanced_index('[[]]') ➞ -1
    first_unbalanced_index('[]]') ➞ 2
    first_unbalanced_index('[[]') ➞ 3
    first_unbalanced_index('][') ➞ 0
    first_unbalanced_index('') ➞ -1
    \'\'\'
''', '''
    depth = 0
    for i, ch in enumerate(string):
        if ch == "[":
            depth += 1
        else:
            if depth == 0:
                return i
            depth -= 1
    return -1 if depth == 0 else len(string)
''', '''
import itertools
def ref(s):
    for i in range(len(s)):
        pre = s[:i + 1]
        if pre.count("]") > pre.count("["):
            return i
    return -1 if s.count("[") == s.count("]") else len(s)
assert first_unbalanced_index("[[]]") == -1
assert first_unbalanced_index("[]]") == 2
assert first_unbalanced_index("[[]") == 3
assert first_unbalanced_index("][") == 0
assert first_unbalanced_index("") == -1
assert first_unbalanced_index("[") == 1
assert first_unbalanced_index("]") == 0
assert first_unbalanced_index("[]") == -1
assert first_unbalanced_index("[][]][") == 4
assert first_unbalanced_index("[[[[") == 4
assert first_unbalanced_index("]]]") == 0
assert first_unbalanced_index("[]]]") == 2
assert first_unbalanced_index("[]" * 50000 + "]") == 100000
assert first_unbalanced_index("[" * 100000) == 100000
assert first_unbalanced_index("[" * 50000 + "]" * 50000) == -1
for n in range(0, 13):
    for t in itertools.product("[]", repeat=n):
        s = "".join(t)
        assert first_unbalanced_index(s) == ref(s), s
''')

# ---------------------------------------------------------------- HumanEval/139
add(139, '''def factorial_sum(n):
    """The factorial sum is defined as:
    factorial_sum(n) = n! + (n-1)! + (n-2)! + ... + 1!
    where n > 0

    For example:
    >>> factorial_sum(4)
    33

    The function will receive an integer as input and should return the factorial
    sum of this integer.
    """
''', '''
    fac, ans = 1, 0
    for i in range(1, n + 1):
        fac *= i
        ans += fac
    return ans
''', '''
import math
assert factorial_sum(1) == 1
assert factorial_sum(2) == 3
assert factorial_sum(3) == 9
assert factorial_sum(4) == 33
assert factorial_sum(5) == 153
assert factorial_sum(6) == 873
assert factorial_sum(10) == 4037913
assert factorial_sum(20) == sum(math.factorial(i) for i in range(1, 21))
for n in range(1, 120):
    assert factorial_sum(n) == sum(math.factorial(i) for i in range(1, n + 1)), n
r = factorial_sum(1500)
assert r > math.factorial(1500) and r < 2 * math.factorial(1500)
assert factorial_sum(7) == 5913
assert isinstance(factorial_sum(3), int)
''')

add(139, '''def double_factorial(n):
    """The double factorial is defined as:
    double_factorial(n) = n * (n-2) * (n-4) * ... down to 2 (if n is even) or down to 1 (if n is odd)
    where n >= 0 and the double factorial of 0 is 1

    For example:
    >>> double_factorial(5)
    15
    >>> double_factorial(6)
    48

    The function will receive an integer as input and should return the double
    factorial of this integer.
    """
''', '''
    ans = 1
    for i in range(n, 1, -2):
        ans *= i
    return ans
''', '''
import math
assert double_factorial(0) == 1
assert double_factorial(1) == 1
assert double_factorial(2) == 2
assert double_factorial(3) == 3
assert double_factorial(4) == 8
assert double_factorial(5) == 15
assert double_factorial(6) == 48
assert double_factorial(7) == 105
assert double_factorial(8) == 384
assert double_factorial(9) == 945
assert double_factorial(10) == 3840
assert double_factorial(15) == 2027025
def ref(k):
    if k <= 1:
        return 1
    return k * ref(k - 2)
for n in range(0, 200):
    assert double_factorial(n) == ref(n), n
for m in range(1, 300):
    assert double_factorial(2 * m) == 2 ** m * math.factorial(m)
    assert double_factorial(2 * m) * double_factorial(2 * m - 1) == math.factorial(2 * m)
assert double_factorial(2000) == 2 ** 1000 * math.factorial(1000)
''')

add(139, '''def special_factorial_mod(n, m):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial_mod(4, 1000)
    288
    >>> special_factorial_mod(4, 100)
    88

    The function will receive two integers n > 0 and m > 0 as input and should return
    the remainder of the division of the Brazilian factorial of n by m.
    """
''', '''
    fac, ans = 1 % m, 1 % m
    for i in range(2, n + 1):
        fac = fac * i % m
        ans = ans * fac % m
    return ans
''', '''
import math
def ref(n, m):
    p = 1
    for i in range(1, n + 1):
        p *= math.factorial(i)
    return p % m
assert special_factorial_mod(4, 1000) == 288
assert special_factorial_mod(4, 100) == 88
assert special_factorial_mod(1, 1) == 0
assert special_factorial_mod(1, 5) == 1
assert special_factorial_mod(2, 1) == 0
assert special_factorial_mod(2, 3) == 2
assert special_factorial_mod(3, 7) == 12 % 7
assert special_factorial_mod(5, 10 ** 9 + 7) == 34560
assert special_factorial_mod(10, 2) == 0
assert special_factorial_mod(6, 1000) == (1 * 2 * 6 * 24 * 120 * 720) % 1000
for n in range(1, 40):
    for m in (1, 2, 3, 7, 10, 97, 1000, 10 ** 9 + 7):
        assert special_factorial_mod(n, m) == ref(n, m), (n, m)
big = special_factorial_mod(200000, 10 ** 9 + 7)
assert 0 <= big < 10 ** 9 + 7
assert special_factorial_mod(10 ** 5, 1) == 0
import math
p = 1
for i in range(1, 2001):
    p = p * (math.factorial(i) % 998244353) % 998244353
assert special_factorial_mod(2000, 998244353) == p
''')

add(139, '''def primorial(n):
    """The primorial is defined as the product of all prime numbers that are
    not greater than n:
    primorial(n) = 2 * 3 * 5 * 7 * ... (all primes p <= n)
    where n >= 0 and the product of no numbers is 1

    For example:
    >>> primorial(10)
    210
    >>> primorial(1)
    1

    The function will receive an integer as input and should return the primorial
    of this integer.
    """
''', '''
    if n < 2:
        return 1
    sieve = [True] * (n + 1)
    ans = 1
    for i in range(2, n + 1):
        if sieve[i]:
            ans *= i
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return ans
''', '''
def isp(k):
    return k > 1 and all(k % d for d in range(2, int(k ** 0.5) + 1))
assert primorial(0) == 1
assert primorial(1) == 1
assert primorial(2) == 2
assert primorial(3) == 6
assert primorial(4) == 6
assert primorial(5) == 30
assert primorial(6) == 30
assert primorial(7) == 210
assert primorial(10) == 210
assert primorial(11) == 2310
assert primorial(13) == 30030
assert primorial(29) == 6469693230
for n in range(0, 300):
    exp = 1
    for k in range(2, n + 1):
        if isp(k):
            exp *= k
    assert primorial(n) == exp, n
assert primorial(100) == 2305567963945518424753102147331756070
assert primorial(10000) % 9973 == 0
assert primorial(10000) % 10007 != 0
''')

add(139, '''def hyperfactorial(n):
    """The hyperfactorial is defined as:
    hyperfactorial(n) = 1^1 * 2^2 * 3^3 * ... * n^n
    where n > 0

    For example:
    >>> hyperfactorial(3)
    108
    >>> hyperfactorial(4)
    27648

    The function will receive an integer as input and should return the hyperfactorial
    of this integer.
    """
''', '''
    ans = 1
    for i in range(2, n + 1):
        ans *= i ** i
    return ans
''', '''
assert hyperfactorial(1) == 1
assert hyperfactorial(2) == 4
assert hyperfactorial(3) == 108
assert hyperfactorial(4) == 27648
assert hyperfactorial(5) == 86400000
assert hyperfactorial(6) == 4031078400000
assert hyperfactorial(7) == 3319766398771200000
def ref(k):
    if k <= 1:
        return 1
    return k ** k * ref(k - 1)
for n in range(1, 60):
    assert hyperfactorial(n) == ref(n), n
assert hyperfactorial(300) % (299 ** 299) == 0
assert hyperfactorial(300) // hyperfactorial(299) == 300 ** 300
assert hyperfactorial(10) % 10 ** 10 == 0
assert hyperfactorial(8) == 55696437941726556979200000
assert hyperfactorial(9) == 21577941222941856209168026828800000
''')
