Financial Computing HW2 - Pricing an FX-linked structured note (dual currency note)

Run (Python 3, no external packages):
    python3 B13902024_HW_2.py D T c S0 X rd rf sigma
Example:
    python3 B13902024_HW_2.py 1000000 1.0 0.06 32.0 31.5 0.015 0.005 0.12
    -> 1006065.998257, 13119.408633, 29.716981

Method (A = D(1+cT) is the principal plus coupon at maturity):
1. Payoff in domestic currency: A if S_T >= X, else (A/X) S_T, i.e.
   A - (A/X) max(X - S_T, 0). The note is a zero-coupon bond paying A
   minus A/X short European FX puts with strike X.
2. Fair value: V0 = A e^{-rd T} - (A/X) P, where P is the Garman-Kohlhagen put
   (Black-Scholes with dividend yield rf):
   P = X e^{-rd T} N(-x + sigma sqrt T) - S0 e^{-rf T} N(-x),
   x = [ln(S0/X) + (rd - rf + sigma^2/2) T] / (sigma sqrt T).
3. Delta: dV0/dS0 = -(A/X) dP/dS0 = (A/X) e^{-rf T} N(-x).
4. Breakeven: the payout exceeds D whenever S_T >= X (c > 0), so S_T* < X and
   (A/X) S_T* = D gives S_T* = X / (1 + cT).
