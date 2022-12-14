N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

V = 0
for i in range(N):
    V += wv[i][1]

dp = [[0]*(V+1) for _ in range(N+1)]
for v in range(1, V+1):
    dp[0][v] = W+1

for i in range(N):
    for j in range(V+1):
        if wv[i][1] <= j:
            dp[i+1][j] = min(dp[i][j], dp[i][j-wv[i][1]] + wv[i][0])
        else:
            dp[i+1][j] = dp[i][j]

ans = 0
for v in range(1, V+1):
    if dp[N][v] <= W:
        ans = max(ans, v)
print(ans)
