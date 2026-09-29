import sys

def annuity_factor(i, n):
    if abs(i) < 1e-12:
        return float(n)
    try:
        return (1 - (1 + i) ** -n) / i
    except OverflowError:
        return float("inf")

def payment(principal, i, n):
    return principal / annuity_factor(i, n)

def solve_irr(c0, dpmt, K, tol=1e-15, max_iter=1000):
    if dpmt <= 0:
        return float("nan")
    if c0 <= 0:
        return float("inf")

    def f(y):
        return dpmt * annuity_factor(y, K) - c0

    lo, hi = -1 + 1e-12, 1.0
    if f(lo) <= 0:
        return float("nan")
    while f(hi) > 0:
        hi *= 2
        if hi > 1e12:
            return float("inf")
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        if mid == lo or mid == hi:
            break
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2

def main():
    V = float(sys.argv[1])
    m = int(sys.argv[2])
    n1, n2, n3 = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    r1, r2 = float(sys.argv[6]), float(sys.argv[7])
    F, alpha = float(sys.argv[8]), float(sys.argv[9])

    i1, i2 = r1 / m, r2 / m
    N = (n3 - n1) * m
    K = (n3 - n2) * m

    pmt_old = payment(V, i1, N)

    B = pmt_old * annuity_factor(i1, K)

    pmt_new = payment(B, i2, K)
    dpmt = pmt_old - pmt_new
    interest_saved = K * dpmt

    c0 = F + alpha * B
    irr = m * solve_irr(c0, dpmt, K)

    print(f"{pmt_old:.6f}, {B:.6f}, {interest_saved:.6f}, {irr:.6f}")

if __name__ == "__main__":
    main()
