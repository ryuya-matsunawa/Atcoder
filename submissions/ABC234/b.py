import itertools
N = int(input())

A = []

for _ in range(N):
    x, y = map(int, input().split())
    A.append((x, y))

combi = list(itertools.combinations(A, 2))

ans = 0
for (x1, y1), (x2, y2) in combi:
    l = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    if ans < l:
        ans = l

print(ans)
