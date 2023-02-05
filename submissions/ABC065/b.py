from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())

dict = defaultdict(int)

for i in range(1, n+1):
    a = int(input())
    dict[i] = a

visited = [False] * (n+1)
ans = 0


def dfs(v):
    global ans
    if v == 2:
        return True
    ans += 1
    visited[v] = True
    if visited[dict[v]] == False:
        return dfs(dict[v])
    else:
        return False


if dfs(1):
    print(ans)
else:
    print(-1)
