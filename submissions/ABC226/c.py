from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())

T = [0] * (N+1)
A = defaultdict(list)

for i in range(1, N+1):
    T[i], _, *L = list(map(int, input().split()))
    A[i] = L

visited = [False] * (N+1)


def dfs(i):
    visited[i] = True
    for n in A[i]:
        if visited[n]:
            continue
        visited[n] = True
        dfs(n)


dfs(N)

cnt = 0
for i in range(1, N+1):
    if visited[i]:
        cnt += T[i]

print(cnt)
