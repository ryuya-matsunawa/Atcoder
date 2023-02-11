n, T = map(int, input().split())
t = list(map(int, input().split()))

tl = [[t[i], t[i]+T] for i in range(n)]

ans = T
for i in range(n-1):
    if tl[i][1] > tl[i+1][0]:
        ans += tl[i+1][0] - tl[i][0]
    else:
        ans += T

print(ans)
