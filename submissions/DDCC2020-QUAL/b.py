from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))

s = list(accumulate(a))
t = list(accumulate(a[::-1]))[::-1]

ans = 10**18

for i in range(n-1):
    ans = min(ans, abs(s[i] - t[i+1]))

print(ans)
