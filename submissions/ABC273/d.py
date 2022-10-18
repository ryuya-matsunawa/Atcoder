from collections import defaultdict
from bisect import bisect

H, W, h, w = map(int, input().split())
N = int(input())
R = defaultdict(list)
C = defaultdict(list)

for _ in range(N):
    r, c = map(int, input().split())
    R[r].append(c)
    C[c].append(r)

for r in R.keys():
    R[r].sort()

for c in C.keys():
    C[c].sort()

Q = int(input())
for _ in range(Q):
    d, l = input().split()
    l = int(l)
    if d == 'U':
        i = bisect(C[w], h)
        h = max(1, h-l)
        if i != 0:
            h = max(h, C[w][i - 1] + 1)
    elif d == 'D':
        i = bisect(C[w], h)
        h = min(H, h+l)
        if i != len(C[w]):
            h = min(h, C[w][i] - 1)
    elif d == 'L':
        i = bisect(R[h], w)
        w = max(1, w-l)
        if i != 0:
            w = max(w, R[h][i - 1] + 1)
    elif d == 'R':
        i = bisect(R[h], w)
        w = min(W, w+l)
        if i != len(R[h]):
            w = min(w, R[h][i] - 1)
    print(h, w)
