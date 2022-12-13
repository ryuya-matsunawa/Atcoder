N = int(input())
H = list(map(int, input().split()))
dp = [float('inf')] * N
dp[0], dp[1] = 0, abs(H[0]-H[1])

for i in range(2, N):
    # dp[i] := i-1番目から移動した時かi-2番目から移動した時の最小値
    dp[i] = min(dp[i-1] + abs(H[i] - H[i-1]), dp[i-2] + abs(H[i] - H[i-2]))

print(dp[N-1])
