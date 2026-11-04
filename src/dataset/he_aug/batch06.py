# fill: parent 14 (1 more), parent 25 (4 more)
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

add(14, '''def decode_runs(message):
    """
    Write a function that decodes a message encoded by run-length encoding: every character that is
    followed by a number is repeated that many times; a character without a number appears once.
    The numbers can have several digits and the original message contains no digits.

    Examples:
    >>> decode_runs('a3bc2')
    'aaabcc'
    >>> decode_runs('abc')
    'abc'
    >>> decode_runs('')
    ''
    """
''', '''
    out = []
    i = 0
    n = len(message)
    while i < n:
        ch = message[i]
        i += 1
        j = i
        while j < n and message[j].isdigit():
            j += 1
        out.append(ch * (int(message[i:j]) if j > i else 1))
        i = j
    return "".join(out)
''', '''
assert decode_runs("") == ""
assert decode_runs("a") == "a"
assert decode_runs("a2") == "aa"
assert decode_runs("a3bc2") == "aaabcc"
assert decode_runs("abc") == "abc"
assert decode_runs("a10") == "a" * 10
assert decode_runs("a100000") == "a" * 100000
assert decode_runs("a1") == "a"
assert decode_runs("a0b") == "b"
assert decode_runs(" 2x") == "  x"
assert decode_runs("ab" * 50000) == "ab" * 50000
def encode_runs(message):
    out, i = [], 0
    while i < len(message):
        j = i
        while j < len(message) and message[j] == message[i]:
            j += 1
        out.append(message[i] + (str(j - i) if j - i > 1 else ""))
        i = j
    return "".join(out)
import random
random.seed(8)
for _ in range(300):
    m = "".join(random.choice("aAbB .") for _ in range(random.randint(0, 25)))
    assert decode_runs(encode_runs(m)) == m, m
''')

add(25, '''def min_path_sum(grid):
    """
    Given a grid with N rows and M columns (N, M >= 1) of non-negative integers, find the minimum
    sum of the values on a path from the top-left cell to the bottom-right cell. In each step
    you can move only right or down. The first and the last cell are included in the sum.

    Examples:

        Input: grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        Output: 7  # 1 -> 3 -> 1 -> 1 -> 1

        Input: grid = [[5]]
        Output: 5
    """
''', '''
    n, m = len(grid), len(grid[0])
    dp = [0] * m
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[j] = grid[0][0]
            elif i == 0:
                dp[j] = dp[j - 1] + grid[i][j]
            elif j == 0:
                dp[j] = dp[j] + grid[i][j]
            else:
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    return dp[-1]
''', '''
assert min_path_sum([[5]]) == 5
assert min_path_sum([[0]]) == 0
assert min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
assert min_path_sum([[1, 2, 3]]) == 6
assert min_path_sum([[1], [2], [3]]) == 6
assert min_path_sum([[1, 2], [1, 1]]) == 3
assert min_path_sum([[0, 0], [0, 0]]) == 0
assert min_path_sum([[1, 100], [100, 1]]) == 102
assert min_path_sum([[10 ** 18, 10 ** 18], [10 ** 18, 10 ** 18]]) == 3 * 10 ** 18
assert min_path_sum([[1] * 500 for _ in range(500)]) == 999
assert min_path_sum([[1] * 100000]) == 100000
assert min_path_sum([[1]] * 100000) == 100000
g = [[(i * 31 + j * 17) % 10 for j in range(5)] for i in range(5)]
def brute(i, j):
    if i == len(g) - 1 and j == len(g[0]) - 1:
        return g[i][j]
    opts = []
    if i + 1 < len(g):
        opts.append(brute(i + 1, j))
    if j + 1 < len(g[0]):
        opts.append(brute(i, j + 1))
    return g[i][j] + min(opts)
assert min_path_sum(g) == brute(0, 0)
''')

add(25, '''def count_paths(n, m, blocked):
    """
    Given a grid with n rows and m columns (n, m >= 1) and a list blocked of (row, column) cells
    (0-based) that cannot be entered, return the number of different paths from the top-left
    cell (0, 0) to the bottom-right cell (n - 1, m - 1). In each step you can move only right or
    down. If the start or the end cell is blocked, return 0. The answer is returned modulo
    10**9 + 7.

    Examples:

        Input: n = 3, m = 3, blocked = [(1, 1)]
        Output: 2

        Input: n = 2, m = 2, blocked = []
        Output: 2
    """
''', '''
    mod = 10 ** 9 + 7
    bad = set(blocked)
    if (0, 0) in bad or (n - 1, m - 1) in bad:
        return 0
    dp = [0] * m
    dp[0] = 1
    for i in range(n):
        for j in range(m):
            if (i, j) in bad:
                dp[j] = 0
            elif j > 0:
                dp[j] = (dp[j] + dp[j - 1]) % mod
    return dp[-1] % mod
''', '''
assert count_paths(1, 1, []) == 1
assert count_paths(1, 1, [(0, 0)]) == 0
assert count_paths(2, 2, []) == 2
assert count_paths(3, 3, [(1, 1)]) == 2
assert count_paths(3, 3, []) == 6
assert count_paths(3, 3, [(0, 0)]) == 0
assert count_paths(3, 3, [(2, 2)]) == 0
assert count_paths(3, 3, [(0, 1), (1, 0)]) == 0
assert count_paths(1, 5, []) == 1
assert count_paths(1, 5, [(0, 3)]) == 0
assert count_paths(5, 1, [(2, 0)]) == 0
assert count_paths(4, 4, [(1, 1), (2, 2)]) == 4
assert count_paths(18, 18, []) == 2333606220 % (10 ** 9 + 7)
import math
assert count_paths(1000, 1000, []) == math.comb(1998, 999) % (10 ** 9 + 7)
assert count_paths(1, 100000, []) == 1
assert count_paths(300, 300, [(150, 150)]) == (math.comb(598, 299) - math.comb(300, 150) * math.comb(298, 149)) % (10 ** 9 + 7)
''')

add(25, '''def max_gold(grid):
    """
    Given a grid with N rows and M columns (N, M >= 1) of non-negative integers where each cell
    holds some gold. Start from any cell of the first column, and in each step move to the cell
    on the right: up-right, right or down-right (you cannot leave the grid). Return the maximum
    amount of gold collected when you reach the last column.

    Examples:

        Input: grid = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
        Output: 12  # 2 -> 6 -> 4

        Input: grid = [[7]]
        Output: 7
    """
''', '''
    n, m = len(grid), len(grid[0])
    cur = [grid[i][0] for i in range(n)]
    for j in range(1, m):
        nxt = []
        for i in range(n):
            best = cur[i]
            if i > 0:
                best = max(best, cur[i - 1])
            if i + 1 < n:
                best = max(best, cur[i + 1])
            nxt.append(best + grid[i][j])
        cur = nxt
    return max(cur)
''', '''
assert max_gold([[7]]) == 7
assert max_gold([[1, 3, 3], [2, 1, 4], [0, 6, 4]]) == 12
assert max_gold([[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]) == 16
assert max_gold([[1, 2, 3]]) == 6
assert max_gold([[1], [5], [3]]) == 5
assert max_gold([[0, 0], [0, 0]]) == 0
assert max_gold([[10, 1, 1], [1, 1, 1], [1, 1, 10]]) == 21
assert max_gold([[10 ** 18] * 3, [10 ** 18] * 3]) == 3 * 10 ** 18
assert max_gold([[1] * 100000]) == 100000
assert max_gold([[1]] * 100000) == 1
assert max_gold([[1] * 300 for _ in range(300)]) == 300
import random
random.seed(41)
def brute(g):
    n, m = len(g), len(g[0])
    def go(i, j):
        if j == m - 1:
            return g[i][j]
        return g[i][j] + max(go(a, j + 1) for a in (i - 1, i, i + 1) if 0 <= a < n)
    return max(go(i, 0) for i in range(n))
for _ in range(100):
    n, m = random.randint(1, 4), random.randint(1, 5)
    g = [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]
    assert max_gold(g) == brute(g), g
''')

add(25, '''def spiral_order(grid):
    """
    Given a grid with N rows and M columns (N, M >= 1), return the list of the values of the
    grid read in clockwise spiral order, starting from the top-left cell and moving right first.

    Examples:

        Input: grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

        Input: grid = [[1, 2], [3, 4], [5, 6]]
        Output: [1, 2, 4, 6, 5, 3]
    """
''', '''
    top, bottom = 0, len(grid) - 1
    left, right = 0, len(grid[0]) - 1
    result = []
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(grid[top][j])
        for i in range(top + 1, bottom + 1):
            result.append(grid[i][right])
        if top < bottom:
            for j in range(right - 1, left - 1, -1):
                result.append(grid[bottom][j])
        if left < right:
            for i in range(bottom - 1, top, -1):
                result.append(grid[i][left])
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    return result
''', '''
assert spiral_order([[1]]) == [1]
assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_order([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
assert spiral_order([[1, 2, 3, 4]]) == [1, 2, 3, 4]
assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]
assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
assert spiral_order([[1, 2, 3, 4, 5]]) == [1, 2, 3, 4, 5]
assert spiral_order([[0, 0]]) == [0, 0]
g = [[i * 400 + j for j in range(400)] for i in range(300)]
r = spiral_order(g)
assert len(r) == 120000 and sorted(r) == list(range(120000)) and r[0] == 0
assert spiral_order([[i] for i in range(100000)]) == list(range(100000))
assert spiral_order([list(range(100000))]) == list(range(100000))
for n in range(1, 7):
    for m in range(1, 7):
        gg = [[i * m + j for j in range(m)] for i in range(n)]
        assert sorted(spiral_order(gg)) == list(range(n * m))
''')
