from itertools import accumulate
N = int(input())

f = [0]*(N+1)
s = [0]*(N+1)

for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        f[i+1] = p
    else:
        s[i+1] = p

F = list(accumulate(f))
S = list(accumulate(s))

Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    print(F[b]-F[a-1], S[b]-S[a-1])
