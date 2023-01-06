from itertools import combinations
n = int(input())

l = []

for _ in range(n):
    x, y = map(int, input().split())
    l.append([x, y])

c = list(combinations(l, 2))
cnt = 0

for a, b in c:
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    if -1.0 <= (y2-y1)/(x2-x1) <= 1.0:
        cnt += 1

print(cnt)
