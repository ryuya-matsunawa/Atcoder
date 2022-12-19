from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
dict = defaultdict(list)

for i in range(m):
    u, v = map(int, input().split())
    dict[u-1].append(v-1)
    dict[v-1].append(u-1)


def c2(n):
    return n*(n-1)//2


ans = c2(n) - m
c = [-1] * n


def dfs(i, nc=0):
    if c[i] >= 0:
        return c[i] == nc
    c[i] = nc
    cvs[nc] += 1
    nc = (nc + 1) % 2
    for j in dict[i]:
        if not dfs(j, nc):
            return False
    return True


for i in range(n):
    if c[i] >= 0:
        continue
    cvs = [0] * 2
    if not dfs(i):
        print(0)
        exit()
    ans -= sum([c2(j) for j in cvs])

print(ans)
