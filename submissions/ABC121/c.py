from collections import defaultdict
n, m = map(int, input().split())
A = set()
B = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split())
    A.add(a)
    B[a] += b

A = sorted(A)

ans = 0
nm = 0

for a in A:
    if nm + B[a] <= m:
        ans += a * B[a]
        nm += B[a]
    else:
        ans += a * (m - nm)
        break

print(ans)
