N, W = map(int, input().split())

dp = [[0]*(W+1) for _ in range(N)]

for i in range(N):
    w, v = map(int, input().split())
    for j in range(W+1):
        if j - w >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]

print(max(dp[N-1]))
