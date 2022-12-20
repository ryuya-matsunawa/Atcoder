from itertools import accumulate
N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

S = [0] + list(accumulate(A))
setS = set(S)

for i in range(len(S)):
    y = S[i] + P
    z = S[i] + P + Q
    w = S[i] + P + Q + R
    if y in setS and z in setS and w in setS:
        print('Yes')
        exit()

print('No')
