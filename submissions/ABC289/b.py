n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []


def dfs(v):
    if v in ans:
        return
    if v in a:
        dfs(v+1)
        ans.append(v)
        return
    ans.append(v)


for i in range(1, n+1):
    dfs(i)
print(*ans)
