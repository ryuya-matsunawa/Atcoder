n = int(input())

l = [int(input()) for _ in range(n)]

# dp[i][j] := i番目まで点数を選んだとき、合計点数をjにできるか
dp = [[False] * (sum(l) + 1) for _ in range(n + 1)]

dp[0][0] = True

for i in range(n):
    for j in range(sum(l) + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
            dp[i + 1][j + l[i]] = True

ans = 0
for i in range(sum(l) + 1):
    if dp[n][i] and i % 10 != 0:
        ans = max(ans, i)

print(ans)
