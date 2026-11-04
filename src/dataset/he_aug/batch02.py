# parents 6-10
PROBLEMS = []
def add(parent, prompt, body, tests):
    PROBLEMS.append(dict(parent=parent, prompt=prompt, body=body, tests=tests))

# ---------------- parent 6: poly / find_zero ----------------
add(6, '''def poly(xs: list, x: int):
    """ Evaluate polynomial with integer coefficients xs at integer point x.
    xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    An empty list is the zero polynomial.
    """
    return sum(coeff * x ** i for i, coeff in enumerate(xs))


def poly_derivative(xs: list) -> list:
    """ Return the coefficients of the derivative of the polynomial xs.
    The derivative of a constant polynomial (or an empty one) is [].
    >>> poly_derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> poly_derivative([7])
    []
    """
''', '''
    return [i * xs[i] for i in range(1, len(xs))]
''', '''
assert poly([], 5) == 0
assert poly([3], 100) == 3
assert poly([1, 2, 3], 2) == 17
assert poly_derivative([]) == []
assert poly_derivative([0]) == []
assert poly_derivative([1, 2]) == [2]
assert poly_derivative([0, 0, 0]) == [0, 0]
assert poly_derivative([-1, -2, -3]) == [-2, -6]
xs = list(range(1, 2001))
d = poly_derivative(xs)
assert len(d) == 1999 and d[-1] == 1999 * 2000
orig = [1, 2, 3]
poly_derivative(orig)
assert orig == [1, 2, 3]
assert poly(poly_derivative([0, 0, 1]), 7) == 14
''')

add(6, '''def poly(xs: list, x: float):
    """ Evaluate polynomial with coefficients xs at point x.
    xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum(coeff * x ** i for i, coeff in enumerate(xs))


def find_root_bisect(xs: list, lo: float, hi: float) -> float:
    """ Find x in [lo, hi] such that poly(xs, x) is zero, using bisection.
    It is guaranteed that poly(xs, lo) and poly(xs, hi) have opposite signs (or one of them is zero).
    The result must be accurate to within 1e-6.
    >>> round(find_root_bisect([-2, 0, 1], 0, 2), 4)
    1.4142
    >>> round(find_root_bisect([1, 2], -5, 5), 4)
    -0.5
    """
''', '''
    f_lo, f_hi = poly(xs, lo), poly(xs, hi)
    if f_lo == 0:
        return lo
    if f_hi == 0:
        return hi
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = poly(xs, mid)
        if f_mid == 0:
            return mid
        if (f_mid < 0) == (f_lo < 0):
            lo, f_lo = mid, f_mid
        else:
            hi = mid
    return (lo + hi) / 2
''', '''
assert abs(find_root_bisect([-2, 0, 1], 0, 2) - 2 ** 0.5) < 1e-6
assert abs(find_root_bisect([-2, 0, 1], -2, 0) + 2 ** 0.5) < 1e-6
assert find_root_bisect([-3, 1], 3, 10) == 3
assert find_root_bisect([-3, 1], -10, 3) == 3
assert abs(find_root_bisect([6, -5, 1], 2.5, 10) - 3) < 1e-6
assert abs(find_root_bisect([-6, 11, -6, 1], 0, 1.5) - 1) < 1e-6
assert abs(find_root_bisect([-6, 11, -6, 1], 2.5, 10) - 3) < 1e-6
assert abs(find_root_bisect([1, 0, 0, 1], -10, 10) + 1) < 1e-6
assert abs(find_root_bisect([-1e12, 1], 0, 1e13) - 1e12) < 1e-6
assert abs(find_root_bisect([1e-9, -1], -1, 1) - 1e-9) < 1e-6
assert abs(find_root_bisect([-1, 0, 0, 0, 0, 1], 0, 1e6) - 1) < 1e-6
''')

add(6, '''def poly_add(a: list, b: list) -> list:
    """ Add two polynomials given as coefficient lists (lowest degree first).
    The result must have no trailing zero coefficients; the zero polynomial is [].
    >>> poly_add([1, 2], [3, 4, 5])
    [4, 6, 5]
    >>> poly_add([1, 2], [-1, -2])
    []
    """
''', '''
    n = max(len(a), len(b))
    res = [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
    while res and res[-1] == 0:
        res.pop()
    return res
''', '''
assert poly_add([], []) == []
assert poly_add([], [1]) == [1]
assert poly_add([1], []) == [1]
assert poly_add([0], [0]) == []
assert poly_add([1, 2, 3], [-1, -2, -3]) == []
assert poly_add([1, 2, 3], [0, 0, -3]) == [1, 2]
assert poly_add([0, 0, 0, 5], [1]) == [1, 0, 0, 5]
assert poly_add([1] * 5000, [2] * 3000) == [3] * 3000 + [1] * 2000
a, b = [1, 2], [3]
poly_add(a, b)
assert a == [1, 2] and b == [3]
''')

add(6, '''def poly_mul(a: list, b: list) -> list:
    """ Multiply two polynomials given as coefficient lists (lowest degree first).
    The result must have no trailing zero coefficients; the zero polynomial is [].
    >>> poly_mul([1, 1], [1, 1])
    [1, 2, 1]
    >>> poly_mul([], [1, 2])
    []
    """
''', '''
    if not a or not b:
        return []
    res = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            res[i + j] += x * y
    while res and res[-1] == 0:
        res.pop()
    return res
''', '''
assert poly_mul([], []) == []
assert poly_mul([0], [1, 2]) == []
assert poly_mul([2], [3]) == [6]
assert poly_mul([-1, 1], [1, 1]) == [-1, 0, 1]
assert poly_mul([1, 2, 3], [0, 1]) == [0, 1, 2, 3]
assert poly_mul([1, 0, 0], [1]) == [1]
assert poly_mul([1, 1] * 1, [1, 1]) == [1, 2, 1]
r = [1]
for _ in range(10):
    r = poly_mul(r, [1, 1])
assert r == [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
big = poly_mul([1] * 400, [1] * 400)
assert len(big) == 799 and big[399] == 400 and big[0] == 1 and big[-1] == 1
assert poly_mul([10**18], [10**18]) == [10**36]
''')

add(6, '''def count_real_roots_quadratic(a: float, b: float, c: float) -> int:
    """ Return the number of distinct real roots of a*x^2 + b*x + c = 0.
    The coefficients may be zero: if a == 0 the equation is linear; if a == b == 0 then
    return 0 when c != 0, and -1 (infinitely many roots) when c == 0.
    >>> count_real_roots_quadratic(1, -3, 2)
    2
    >>> count_real_roots_quadratic(1, 2, 1)
    1
    >>> count_real_roots_quadratic(0, 0, 0)
    -1
    """
''', '''
    if a == 0:
        if b == 0:
            return -1 if c == 0 else 0
        return 1
    disc = b * b - 4 * a * c
    if disc > 0:
        return 2
    return 1 if disc == 0 else 0
''', '''
assert count_real_roots_quadratic(1, 0, 1) == 0
assert count_real_roots_quadratic(1, 0, -1) == 2
assert count_real_roots_quadratic(1, 0, 0) == 1
assert count_real_roots_quadratic(-1, 0, 0) == 1
assert count_real_roots_quadratic(0, 2, 3) == 1
assert count_real_roots_quadratic(0, 0, 5) == 0
assert count_real_roots_quadratic(0, 0, -5) == 0
assert count_real_roots_quadratic(0, 0, 0) == -1
assert count_real_roots_quadratic(2, 4, 2) == 1
assert count_real_roots_quadratic(1, -10**9, 1) == 2
assert count_real_roots_quadratic(10**9, 2 * 10**9, 10**9) == 1
assert count_real_roots_quadratic(0.5, 1, 0.5) == 1
assert count_real_roots_quadratic(-2, 3, -4) == 0
assert count_real_roots_quadratic(10**12, 10**12, 1) == 2
''')

# ---------------- parent 7: prime_fib ----------------
add(7, '''def nth_prime(n: int) -> int:
    """ Return the n-th prime number (n starts from 1). It is guaranteed that 1 <= n <= 20000.
    >>> nth_prime(1)
    2
    >>> nth_prime(2)
    3
    >>> nth_prime(6)
    13
    """
''', '''
    limit = 30
    while True:
        sieve = bytearray([1]) * (limit + 1)
        sieve[0:2] = b"\\x00\\x00"
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                sieve[i * i::i] = bytearray(len(range(i * i, limit + 1, i)))
        primes = [i for i in range(limit + 1) if sieve[i]]
        if len(primes) >= n:
            return primes[n - 1]
        limit *= 2
''', '''
assert [nth_prime(i) for i in range(1, 11)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert nth_prime(25) == 97
assert nth_prime(26) == 101
assert nth_prime(100) == 541
assert nth_prime(1000) == 7919
assert nth_prime(10000) == 104729
assert nth_prime(20000) == 224737
''')

add(7, '''def nth_prime_palindrome(n: int) -> int:
    """ Return the n-th number (n starts from 1) that is both prime and a palindrome in base 10.
    It is guaranteed that 1 <= n <= 40.
    >>> nth_prime_palindrome(1)
    2
    >>> nth_prime_palindrome(5)
    11
    >>> nth_prime_palindrome(6)
    101
    """
''', '''
    def is_prime(m):
        if m < 2:
            return False
        if m % 2 == 0:
            return m == 2
        i = 3
        while i * i <= m:
            if m % i == 0:
                return False
            i += 2
        return True

    count = 0
    m = 1
    while True:
        m += 1
        s = str(m)
        if s == s[::-1] and is_prime(m):
            count += 1
            if count == n:
                return m
''', '''
assert [nth_prime_palindrome(i) for i in range(1, 11)] == [2, 3, 5, 7, 11, 101, 131, 151, 181, 191]
assert nth_prime_palindrome(11) == 313
assert nth_prime_palindrome(20) == 929
assert nth_prime_palindrome(21) == 10301
assert nth_prime_palindrome(30) == 13831
assert nth_prime_palindrome(40) == 17471
''')

add(7, '''def nth_even_fib(n: int) -> int:
    """ Return the n-th even Fibonacci number (n starts from 1) in the sequence 1, 1, 2, 3, 5, 8, ...
    Fibonacci numbers grow fast, so the result can be very large (Python ints are unbounded).
    >>> nth_even_fib(1)
    2
    >>> nth_even_fib(2)
    8
    >>> nth_even_fib(3)
    34
    """
''', '''
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if a % 2 == 0 and a > 0:
            count += 1
            if count == n:
                return a
''', '''
assert [nth_even_fib(i) for i in range(1, 7)] == [2, 8, 34, 144, 610, 2584]
assert nth_even_fib(10) == 832040
assert nth_even_fib(30) == 2880067194370816120
f = [0, 1]
while len(f) < 3 * 5000 + 5:
    f.append(f[-1] + f[-2])
assert nth_even_fib(1000) == f[3 * 1000]
assert nth_even_fib(5000) == f[3 * 5000]
''')

add(7, '''def nth_lucas_prime(n: int) -> int:
    """ Return the n-th prime number in the Lucas sequence 2, 1, 3, 4, 7, 11, 18, 29, ...
    (L0 = 2, L1 = 1, L(k) = L(k-1) + L(k-2)). It is guaranteed that 1 <= n <= 12.
    >>> nth_lucas_prime(1)
    2
    >>> nth_lucas_prime(2)
    3
    >>> nth_lucas_prime(5)
    29
    """
''', '''
    def is_prime(m):
        if m < 2:
            return False
        i = 2
        while i * i <= m:
            if m % i == 0:
                return False
            i += 1
        return True

    a, b = 2, 1
    count = 0
    while True:
        if is_prime(a):
            count += 1
            if count == n:
                return a
        a, b = b, a + b
''', '''
exp = [2, 3, 7, 11, 29, 47, 199, 521, 2207, 3571, 9349, 3010349]
assert [nth_lucas_prime(i) for i in range(1, 13)] == exp
''')

add(7, '''def nth_twin_prime(n: int) -> int:
    """ Return the smaller member of the n-th pair of twin primes (p, p + 2), n starts from 1.
    It is guaranteed that 1 <= n <= 1000.
    >>> nth_twin_prime(1)
    3
    >>> nth_twin_prime(2)
    5
    >>> nth_twin_prime(4)
    17
    """
''', '''
    limit = 1000
    while True:
        sieve = [True] * (limit + 3)
        sieve[0] = sieve[1] = False
        for i in range(2, int((limit + 2) ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 3, i):
                    sieve[j] = False
        twins = [p for p in range(2, limit + 1) if sieve[p] and sieve[p + 2]]
        if len(twins) >= n:
            return twins[n - 1]
        limit *= 2
''', '''
assert [nth_twin_prime(i) for i in range(1, 9)] == [3, 5, 11, 17, 29, 41, 59, 71]
assert nth_twin_prime(10) == 107
ps = []
x = 3
def isp(m):
    if m < 2:
        return False
    i = 2
    while i * i <= m:
        if m % i == 0:
            return False
        i += 1
    return True
while len(ps) < 1000:
    if isp(x) and isp(x + 2):
        ps.append(x)
    x += 2
assert nth_twin_prime(100) == ps[99]
assert nth_twin_prime(1000) == ps[999]
''')

# ---------------- parent 8: is_multiply_prime ----------------
add(8, '''def is_semiprime(n):
    """Return True if the given positive integer n is the product of exactly two primes
    (not necessarily different), and False otherwise. n can be as large as 10**12.
    Example:
    is_semiprime(15) == True
    is_semiprime(4) == True
    is_semiprime(8) == False
    """
''', '''
    if n < 4:
        return False
    count = 0
    i = 2
    while i * i <= n and count < 3:
        while n % i == 0:
            n //= i
            count += 1
        i += 1
    if n > 1:
        count += 1
    return count == 2
''', '''
assert is_semiprime(1) is False
assert is_semiprime(2) is False
assert is_semiprime(3) is False
assert is_semiprime(4) is True
assert is_semiprime(6) is True
assert is_semiprime(8) is False
assert is_semiprime(9) is True
assert is_semiprime(12) is False
assert is_semiprime(97) is False
assert is_semiprime(10**12) is False
assert is_semiprime(999983 * 999979) is True
assert is_semiprime(999999999989) is False
assert is_semiprime(999983 ** 2) is True
def brute(n):
    c, d = 0, 2
    while n > 1:
        while n % d == 0:
            n //= d
            c += 1
        d += 1
    return c == 2
for n in range(1, 400):
    assert is_semiprime(n) == brute(n), n
''')

add(8, '''def is_sphenic(n):
    """Return True if the given positive integer n is the product of exactly three
    DIFFERENT primes, and False otherwise.
    Example:
    is_sphenic(30) == True
    is_sphenic(60) == False
    is_sphenic(8) == False
    """
''', '''
    if n < 30:
        return False
    primes = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            if n % i == 0:
                return False
            primes.append(i)
        else:
            i += 1
    if n > 1:
        primes.append(n)
    return len(primes) == 3
''', '''
assert is_sphenic(1) is False
assert is_sphenic(2) is False
assert is_sphenic(30) is True
assert is_sphenic(42) is True
assert is_sphenic(60) is False
assert is_sphenic(8) is False
assert is_sphenic(105) is True
assert is_sphenic(2 * 2 * 3) is False
assert is_sphenic(2 * 3 * 3) is False
assert is_sphenic(2 * 3 * 5 * 7) is False
assert is_sphenic(1000003 * 1000033 * 2) is True
assert is_sphenic(2 * 3 * 999999937) is True
assert is_sphenic(2 * 2 * 999999937) is False
def brute(n):
    fs, d = [], 2
    while n > 1:
        if n % d == 0:
            fs.append(d)
            n //= d
        else:
            d += 1
    return len(fs) == 3 and len(set(fs)) == 3
for n in range(1, 600):
    assert is_sphenic(n) == brute(n), n
''')

add(8, '''def is_prime_power(n):
    """Return True if the positive integer n equals p**k for some prime p and integer k >= 1,
    and False otherwise. n can be as large as 10**12.
    Example:
    is_prime_power(8) == True
    is_prime_power(7) == True
    is_prime_power(12) == False
    is_prime_power(1) == False
    """
''', '''
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            return n == 1
        i += 1
    return True
''', '''
assert is_prime_power(0) is False
assert is_prime_power(1) is False
assert is_prime_power(2) is True
assert is_prime_power(4) is True
assert is_prime_power(6) is False
assert is_prime_power(9) is True
assert is_prime_power(10) is False
assert is_prime_power(2 ** 39) is True
assert is_prime_power(3 ** 25) is True
assert is_prime_power(999999999989) is True
assert is_prime_power(999983 ** 2) is True
assert is_prime_power(999983 * 999979) is False
assert is_prime_power(2 ** 20 * 3) is False
assert is_prime_power(10 ** 12) is False
''')

add(8, '''def is_product_of_k_primes(n, k):
    """Return True if the positive integer n is the product of exactly k primes
    (not necessarily different, counted with multiplicity), and False otherwise.
    Here k >= 1, and n can be as large as 10**12.
    Example:
    is_product_of_k_primes(12, 3) == True   # 2 * 2 * 3
    is_product_of_k_primes(12, 2) == False
    is_product_of_k_primes(1, 1) == False
    """
''', '''
    count = 0
    i = 2
    while i * i <= n and count <= k:
        while n % i == 0:
            n //= i
            count += 1
        i += 1
    if n > 1:
        count += 1
    return count == k
''', '''
assert is_product_of_k_primes(1, 1) is False
assert is_product_of_k_primes(2, 1) is True
assert is_product_of_k_primes(2, 2) is False
assert is_product_of_k_primes(12, 3) is True
assert is_product_of_k_primes(12, 2) is False
assert is_product_of_k_primes(2 ** 39, 39) is True
assert is_product_of_k_primes(2 ** 39, 38) is False
assert is_product_of_k_primes(2 ** 39, 40) is False
assert is_product_of_k_primes(999999999989, 1) is True
assert is_product_of_k_primes(999983 * 999979, 2) is True
assert is_product_of_k_primes(2 * 3 * 5 * 7 * 11 * 13, 6) is True
assert is_product_of_k_primes(2 * 3 * 5 * 7 * 11 * 13, 5) is False
def brute(n, k):
    c, d = 0, 2
    while n > 1:
        while n % d == 0:
            n //= d
            c += 1
        d += 1
    return c == k
for n in range(1, 200):
    for k in range(1, 8):
        assert is_product_of_k_primes(n, k) == brute(n, k), (n, k)
''')

add(8, '''def is_square_free(n):
    """Return True if the positive integer n is not divisible by the square of any prime
    (the number 1 is square-free), and False otherwise. n can be as large as 10**12.
    Example:
    is_square_free(30) == True
    is_square_free(12) == False
    is_square_free(1) == True
    """
''', '''
    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return False
        if n % i == 0:
            n //= i
        i += 1
    return True
''', '''
assert is_square_free(1) is True
assert is_square_free(2) is True
assert is_square_free(4) is False
assert is_square_free(6) is True
assert is_square_free(8) is False
assert is_square_free(9) is False
assert is_square_free(12) is False
assert is_square_free(30) is True
assert is_square_free(49) is False
assert is_square_free(999999999989) is True
assert is_square_free(999983 ** 2) is False
assert is_square_free(999983 * 999979) is True
assert is_square_free(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23) is True
assert is_square_free(2 ** 39) is False
assert is_square_free(10 ** 12) is False
for n in range(1, 500):
    assert is_square_free(n) == all(n % (d * d) for d in range(2, n + 1)), n
''')

# ---------------- parent 9: is_simple_power ----------------
add(9, '''def is_perfect_power(x):
    """Return True if the positive integer x can be written as a**b where a and b are
    integers, a >= 2 and b >= 2, and False otherwise. x can be as large as 10**18.
    For example:
    is_perfect_power(8) => True
    is_perfect_power(1) => False
    is_perfect_power(12) => False
    is_perfect_power(81) => True
    """
''', '''
    if x < 4:
        return False
    for b in range(2, x.bit_length() + 1):
        lo, hi = 2, 1 << (x.bit_length() // b + 1)
        while lo <= hi:
            mid = (lo + hi) // 2
            p = mid ** b
            if p == x:
                return True
            if p < x:
                lo = mid + 1
            else:
                hi = mid - 1
    return False
''', '''
assert is_perfect_power(0) is False
assert is_perfect_power(1) is False
assert is_perfect_power(2) is False
assert is_perfect_power(3) is False
assert is_perfect_power(4) is True
assert is_perfect_power(8) is True
assert is_perfect_power(9) is True
assert is_perfect_power(12) is False
assert is_perfect_power(16) is True
assert is_perfect_power(1024) is True
assert is_perfect_power(10 ** 18) is True
assert is_perfect_power(10 ** 18 + 1) is False
assert is_perfect_power(999999999999999989) is False
assert is_perfect_power(2 ** 59) is True
assert is_perfect_power(2 ** 59 + 1) is False
assert is_perfect_power(999999937 ** 2) is True
assert is_perfect_power(999983 ** 3) is True
assert is_perfect_power(999983 ** 3 - 1) is False
def brute(x):
    for a in range(2, 60):
        p = a * a
        while p <= x:
            if p == x:
                return True
            p *= a
    return False
for x in range(1, 3000):
    assert is_perfect_power(x) == brute(x), x
''')

add(9, '''def is_power_of_two(x):
    """Return True if the integer x is a power of two (1, 2, 4, 8, ...) and False
    otherwise. Zero and negative numbers are not powers of two.
    For example:
    is_power_of_two(1) => True
    is_power_of_two(64) => True
    is_power_of_two(0) => False
    is_power_of_two(6) => False
    """
''', '''
    return x > 0 and x & (x - 1) == 0
''', '''
assert is_power_of_two(1) is True
assert is_power_of_two(2) is True
assert is_power_of_two(3) is False
assert is_power_of_two(0) is False
assert is_power_of_two(-1) is False
assert is_power_of_two(-2) is False
assert is_power_of_two(-8) is False
assert is_power_of_two(2 ** 62) is True
assert is_power_of_two(2 ** 62 + 1) is False
assert is_power_of_two(2 ** 200) is True
assert is_power_of_two(2 ** 200 - 1) is False
assert is_power_of_two(6) is False
assert is_power_of_two(1023) is False
assert is_power_of_two(1024) is True
''')

add(9, '''def simple_power_exponent(x, n):
    """Return the integer exponent e >= 0 such that n**e == x, or -1 if there is no such exponent.
    Both x and n are positive integers. When n is 1, only x == 1 has an exponent (0).
    For example:
    simple_power_exponent(8, 2) => 3
    simple_power_exponent(1, 5) => 0
    simple_power_exponent(10, 2) => -1
    simple_power_exponent(5, 1) => -1
    """
''', '''
    if x == 1:
        return 0
    if n == 1:
        return -1
    e = 0
    p = 1
    while p < x:
        p *= n
        e += 1
    return e if p == x else -1
''', '''
assert simple_power_exponent(1, 1) == 0
assert simple_power_exponent(1, 7) == 0
assert simple_power_exponent(2, 1) == -1
assert simple_power_exponent(2, 2) == 1
assert simple_power_exponent(8, 2) == 3
assert simple_power_exponent(9, 3) == 2
assert simple_power_exponent(10, 2) == -1
assert simple_power_exponent(3, 2) == -1
assert simple_power_exponent(5, 10) == -1
assert simple_power_exponent(10 ** 18, 10) == 18
assert simple_power_exponent(2 ** 1000, 2) == 1000
assert simple_power_exponent(2 ** 1000 + 1, 2) == -1
assert simple_power_exponent(7 ** 300, 7) == 300
assert simple_power_exponent(10 ** 6, 10 ** 6) == 1
assert simple_power_exponent(10 ** 6, 10 ** 7) == -1
''')

add(9, '''def is_sum_of_two_powers(x, n):
    """Return True if the positive integer x equals n**a + n**b for some integers a >= 0 and
    b >= 0 (a and b may be equal), and False otherwise. Here n >= 2.
    For example:
    is_sum_of_two_powers(2, 2) => True    # 1 + 1
    is_sum_of_two_powers(10, 3) => True   # 1 + 9
    is_sum_of_two_powers(7, 2) => False
    is_sum_of_two_powers(1, 5) => False
    """
''', '''
    powers = []
    p = 1
    while p < x:
        powers.append(p)
        p *= n
    seen = set(powers)
    return any(x - p in seen for p in powers)
''', '''
assert is_sum_of_two_powers(1, 2) is False
assert is_sum_of_two_powers(2, 2) is True
assert is_sum_of_two_powers(3, 2) is True
assert is_sum_of_two_powers(4, 2) is True
assert is_sum_of_two_powers(7, 2) is False
assert is_sum_of_two_powers(10, 3) is True
assert is_sum_of_two_powers(5, 3) is False
assert is_sum_of_two_powers(6, 3) is True
assert is_sum_of_two_powers(2, 3) is True
assert is_sum_of_two_powers(18, 3) is True
assert is_sum_of_two_powers(1, 5) is False
assert is_sum_of_two_powers(2 ** 100 + 1, 2) is True
assert is_sum_of_two_powers(2 ** 100 + 2 ** 3, 2) is True
assert is_sum_of_two_powers(2 ** 100 + 3, 2) is False
assert is_sum_of_two_powers(10 ** 18 + 1, 10) is True
assert is_sum_of_two_powers(10 ** 18 + 2, 10) is False
def brute(x, n):
    ps = [n ** i for i in range(0, 12)]
    return any(a + b == x for a in ps for b in ps)
for n in range(2, 6):
    for x in range(1, 400):
        assert is_sum_of_two_powers(x, n) == brute(x, n), (x, n)
''')

add(9, '''def largest_power_below(n, limit):
    """Return the largest power n**e (e >= 0 integer) that is less than or equal to limit.
    It is guaranteed that n >= 2 and limit >= 1.
    For example:
    largest_power_below(2, 100) => 64
    largest_power_below(10, 10) => 10
    largest_power_below(3, 2) => 1
    """
''', '''
    p = 1
    while p * n <= limit:
        p *= n
    return p
''', '''
assert largest_power_below(2, 1) == 1
assert largest_power_below(2, 2) == 2
assert largest_power_below(2, 3) == 2
assert largest_power_below(2, 100) == 64
assert largest_power_below(3, 2) == 1
assert largest_power_below(3, 27) == 27
assert largest_power_below(3, 26) == 9
assert largest_power_below(10, 10) == 10
assert largest_power_below(10, 99999) == 10000
assert largest_power_below(2, 2 ** 100) == 2 ** 100
assert largest_power_below(2, 2 ** 100 - 1) == 2 ** 99
assert largest_power_below(10 ** 9, 10 ** 18) == 10 ** 18
assert largest_power_below(10 ** 9, 10 ** 18 - 1) == 10 ** 9
assert largest_power_below(10 ** 18, 5) == 1
''')

# ---------------- parent 10: numerical_letter_grade ----------------
add(10, '''def percent_to_grade(scores):
    """Convert a list of percentage scores to letter grades using this table
    (check from the top, the first matching row wins):
        score >= 90   'A'
        score >= 80   'B'
        score >= 70   'C'
        score >= 60   'D'
        otherwise     'F'
    A score outside the range [0, 100] gets the grade 'INVALID'.

    Example:
    percent_to_grade([95, 80, 79.9, 12]) ==> ['A', 'B', 'C', 'F']
    """
''', '''
    result = []
    for s in scores:
        if s < 0 or s > 100:
            result.append("INVALID")
        elif s >= 90:
            result.append("A")
        elif s >= 80:
            result.append("B")
        elif s >= 70:
            result.append("C")
        elif s >= 60:
            result.append("D")
        else:
            result.append("F")
    return result
''', '''
assert percent_to_grade([]) == []
assert percent_to_grade([100, 90, 89.99, 80, 79.99, 70, 69.99, 60, 59.99, 0]) == ["A", "A", "B", "B", "C", "C", "D", "D", "F", "F"]
assert percent_to_grade([-0.01, 100.01, -5, 101]) == ["INVALID"] * 4
assert percent_to_grade([0.0]) == ["F"]
assert percent_to_grade([100.0]) == ["A"]
assert percent_to_grade([float("inf"), float("-inf")]) == ["INVALID", "INVALID"]
assert percent_to_grade([90] * 50000) == ["A"] * 50000
''')

add(10, '''def gpa_from_letters(letters):
    """Given a list of letter grades, return the average grade points rounded to 2 decimals.
    Points: 'A' 4.0, 'B' 3.0, 'C' 2.0, 'D' 1.0, 'F' 0.0. A '+' suffix adds 0.3 and
    a '-' suffix subtracts 0.3, except that 'A+' stays 4.0 and 'F+' / 'F-' stay 0.0.
    For an empty list return 0.0.

    Example:
    gpa_from_letters(['A', 'B+', 'C-']) ==> 3.0
    """
''', '''
    if not letters:
        return 0.0
    base = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    total = 0.0
    for g in letters:
        pts = base[g[0]]
        if len(g) > 1 and g[0] != "F":
            if g[1] == "+":
                pts = min(4.0, pts + 0.3)
            elif g[1] == "-":
                pts -= 0.3
        total += pts
    return round(total / len(letters), 2)
''', '''
assert gpa_from_letters([]) == 0.0
assert gpa_from_letters(["A"]) == 4.0
assert gpa_from_letters(["A+"]) == 4.0
assert gpa_from_letters(["A-"]) == 3.7
assert gpa_from_letters(["F+", "F-", "F"]) == 0.0
assert gpa_from_letters(["A", "B+", "C-"]) == 3.0
assert gpa_from_letters(["D-"]) == 0.7
assert gpa_from_letters(["D+"]) == 1.3
assert gpa_from_letters(["A", "F"]) == 2.0
assert gpa_from_letters(["B", "B", "C"]) == 2.67
assert gpa_from_letters(["A-", "B+"]) == 3.5
assert gpa_from_letters(["C+"] * 100000) == 2.3
''')

add(10, '''def count_grades(grades):
    """Given a list of letter grades (each one of 'A', 'B', 'C', 'D', 'F'), return a dictionary
    that maps every letter present in the list to the number of times it appears.
    The keys of the dictionary must be in the order 'A', 'B', 'C', 'D', 'F'.

    Example:
    count_grades(['B', 'A', 'B']) ==> {'A': 1, 'B': 2}
    """
''', '''
    result = {}
    for letter in "ABCDF":
        c = grades.count(letter)
        if c:
            result[letter] = c
    return result
''', '''
assert count_grades([]) == {}
assert count_grades(["A"]) == {"A": 1}
assert count_grades(["F", "D", "C", "B", "A"]) == {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}
assert list(count_grades(["F", "D", "C", "B", "A", "A"])) == ["A", "B", "C", "D", "F"]
assert list(count_grades(["F", "B"])) == ["B", "F"]
assert count_grades(["C"] * 100000) == {"C": 100000}
g = ["A", "B"] * 25000
assert count_grades(g) == {"A": 25000, "B": 25000}
''')

add(10, '''def classify_bmi(weight, height):
    """Given weight in kilograms and height in meters, return the BMI category (BMI = weight / height**2):
        BMI < 18.5          'Underweight'
        18.5 <= BMI < 25    'Normal'
        25 <= BMI < 30      'Overweight'
        BMI >= 30           'Obese'
    If weight or height is not positive, return 'Invalid'.

    Example:
    classify_bmi(70, 1.75) ==> 'Normal'
    """
''', '''
    if weight <= 0 or height <= 0:
        return "Invalid"
    bmi = weight / height ** 2
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"
''', '''
assert classify_bmi(70, 1.75) == "Normal"
assert classify_bmi(0, 1.75) == "Invalid"
assert classify_bmi(70, 0) == "Invalid"
assert classify_bmi(-70, 1.75) == "Invalid"
assert classify_bmi(70, -1.75) == "Invalid"
assert classify_bmi(50, 2) == "Underweight"
assert classify_bmi(74, 2) == "Normal"
assert classify_bmi(99, 2) == "Normal"
assert classify_bmi(100, 2) == "Overweight"
assert classify_bmi(25, 1) == "Overweight"
assert classify_bmi(30, 1) == "Obese"
assert classify_bmi(18.5, 1) == "Normal"
assert classify_bmi(18.4999, 1) == "Underweight"
assert classify_bmi(29.99, 1) == "Overweight"
assert classify_bmi(1e9, 1e-3) == "Obese"
assert classify_bmi(1e-9, 1e9) == "Underweight"
''')

add(10, '''def classify_temperatures(temps):
    """Given a list of temperatures in Celsius, return a list of labels using this table:
        temp > 35      'hot'
        temp > 25      'warm'
        temp > 10      'mild'
        temp > 0       'cool'
        temp == 0      'freezing'
        temp < 0       'frozen'
    The table is checked from the top and the first matching row wins.

    Example:
    classify_temperatures([36, 25, 10.5, 0, -3]) ==> ['hot', 'mild', 'mild', 'freezing', 'frozen']
    """
''', '''
    labels = []
    for t in temps:
        if t > 35:
            labels.append("hot")
        elif t > 25:
            labels.append("warm")
        elif t > 10:
            labels.append("mild")
        elif t > 0:
            labels.append("cool")
        elif t == 0:
            labels.append("freezing")
        else:
            labels.append("frozen")
    return labels
''', '''
assert classify_temperatures([]) == []
assert classify_temperatures([36, 35, 25.01, 25, 10.5, 10, 0.1, 0, -0.1]) == ["hot", "warm", "warm", "mild", "mild", "cool", "cool", "freezing", "frozen"]
assert classify_temperatures([0.0, -0.0]) == ["freezing", "freezing"]
assert classify_temperatures([float("inf"), float("-inf")]) == ["hot", "frozen"]
assert classify_temperatures([100, 1000000]) == ["hot", "hot"]
assert classify_temperatures([-273.15]) == ["frozen"]
assert classify_temperatures([5] * 100000) == ["cool"] * 100000
''')
