N, K, D = map(int, input().split())
a = list(map(int, input().split()))

dp = [[[-1]*D for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(K+1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
            if j != K:
                dp[i+1][j+1][(k+a[i]) % D] = max(dp[i+1][j+1]
                                                 [(k+a[i]) % D], dp[i][j][k] + a[i])

print(dp[N][K][0])
