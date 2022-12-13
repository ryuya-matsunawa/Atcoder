N, K = map(int, input().split())
H = list(map(int, input().split()))
dp = [float('inf')] * N
dp[0], dp[1] = 0, abs(H[1]-H[0])

for i in range(2, N):
    for j in range(1, K+1):
        if i-j >= 0:
            # dp[i] := i-1,i-2,...,i-K番目から移動した時の中から最小値
            tmp = dp[i-j] + abs(H[i] - H[i-j])
            if dp[i] > tmp:
                dp[i] = tmp

print(dp[N-1])
