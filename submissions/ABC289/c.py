from itertools import combinations
n, m = map(int, input().split())

l = []
nl = set(range(1, n+1))

for i in range(m):
    c = int(input())
    a = list(map(int, input().split()))
    l.append(a)

ans = 0

for i in range(1, m+1):
    combi = list(combinations(l, i))
    tmp = set()
    for j in combi:
        for k in j:
            for x in k:
                tmp.add(x)
        if tmp == nl:
            ans += 1
        tmp = set()

print(ans)
