from collections import defaultdict
# n種類の硬貨があり、それぞれの硬貨の枚数は無限にある。
# これらの硬貨の中から何枚かを選び、その総額をちょうどx円にできるか判定せよ。
n, x = map(int, input().split())

# a円硬貨をb枚持っている
dict = defaultdict(int)
# 硬貨の種類
l = []

for i in range(n):
    a, b = map(int, input().split())
    dict[a] = b
    l.append(a)

# dp[i][j] = i番目までの硬貨をdict[i]枚まで使って、総額がj円になるかどうか
dp = [[False]*(x+1) for _ in range(n+1)]

# 0円にする方法は何も選ばない方法しかない
dp[0][0] = True

for i in range(n):
    for j in range(x+1):
        # i番目の硬貨を使わない場合
        if dp[i][j]:
            dp[i+1][j] = True
        # i番目の硬貨を使う場合
        for k in range(dict[l[i]]+1):
            if j - l[i]*k >= 0:
                if dp[i][j-l[i]*k]:
                    dp[i+1][j] = True

if dp[n][x]:
    print('Yes')
else:
    print('No')
