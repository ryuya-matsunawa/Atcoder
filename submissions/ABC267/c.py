from collections import defaultdict
from itertools import accumulate
N, M = map(int, input().split())
A = list(map(int, input().split()))

S0 = [0] + list(accumulate(A))
S1 = [0] + list(accumulate([(i+1) * A[i] for i in range(N)]))


def f(l, r):
    return (S1[r]-S1[l]) - l*(S0[r]-S0[l])


ans = [f(i-M, i) for i in range(M, N+1)]
print(max(ans))
