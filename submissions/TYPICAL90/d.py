from collections import defaultdict
H, W = map(int, input().split())
r = defaultdict(int)
c = defaultdict(int)
B = []

for i in range(H):
    l = list(map(int, input().split()))
    r[i] = sum(l)
    B.append(l)
    for j in range(W):
        c[j] += l[j]

for i in range(H):
    ans = [r[i]+c[j]-B[i][j] for j in range(W)]
    print(*ans)
