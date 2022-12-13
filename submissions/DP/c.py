N = int(input())

dp = [[-float('inf')]*3 for _ in range(N)]
l = list(map(int, input().split()))
dp[0] = l

for i in range(1, N):
    L = list(map(int, input().split()))
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            tmp = L[k] + dp[i-1][j]
            if dp[i][k] < tmp:
                dp[i][k] = tmp

print(max(dp[N-1]))
