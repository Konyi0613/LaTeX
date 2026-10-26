import sys
from math import erfc, exp, log, sqrt

def norm_cdf(z):
    return 0.5 * erfc(-z / sqrt(2))

def price_note(D, T, c, S0, X, rd, rf, sigma):
    A = D * (1 + c * T)
    vol = sigma * sqrt(T)

    if vol <= 0:
        F = S0 * exp((rd - rf) * T)
        value = exp(-rd * T) * A * min(1.0, F / X)
        delta = A / X * exp(-rf * T) if F < X else 0.0
        return value, delta

    x = (log(S0 / X) + (rd - rf + sigma * sigma / 2) * T) / vol
    put = X * exp(-rd * T) * norm_cdf(-x + vol) - S0 * exp(-rf * T) * norm_cdf(-x)

    value = A * exp(-rd * T) - A / X * put
    delta = A / X * exp(-rf * T) * norm_cdf(-x)
    return value, delta

def main():
    D, T, c, S0, X, rd, rf, sigma = map(float, sys.argv[1:9])

    value, delta = price_note(D, T, c, S0, X, rd, rf, sigma)
    breakeven = X / (1 + c * T)

    print(f"{value:.6f}, {delta:.6f}, {breakeven:.6f}")

if __name__ == "__main__":
    main()
