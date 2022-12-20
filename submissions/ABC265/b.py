from collections import defaultdict
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
n = 1

xy = defaultdict(int)
for _ in range(M):
    x, y = map(int, input().split())
    xy[x] = y

for i in range(N-1):
    if T - A[i] <= 0:
        print('No')
        exit()
    T -= A[i]
    n += 1
    T += xy[n]

print('Yes')
