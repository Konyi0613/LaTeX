Financial Computing HW1 - Refinancing a commercial property loan

Run (Python 3, no external packages):
    python3 HW_1.py V m n1 n2 n3 r1 r2 F alpha
Example:
    python3 HW_1.py 10000000 12 3 5 20 0.025 0.018 50000 0.01
    -> 60222.193744, 9031668.918858, 527518.711395, 0.243936

Method (i1 = r1/m, i2 = r2/m, N = (n3-n1)m, K = (n3-n2)m,
a(i,n) = (1-(1+i)^-n)/i is the annuity factor):
1. Payment after grace period: PMT_old = V / a(i1, N).
   The balance stays V during the interest-only period, so V is amortized over N periods.
2. Remaining balance at year n2 (just after that payment): B = PMT_old * a(i1, K),
   the present value of the K payments still owed on the old loan.
3. New payment PMT_new = B / a(i2, K). Both loans repay the same principal B,
   so interest saved = K * (PMT_old - PMT_new).
4. IRR: solve (PMT_old - PMT_new) * a(y, K) = F + alpha*B for y by bisection
   (the left side is strictly decreasing in y, so the root is unique);
   output m*y.
