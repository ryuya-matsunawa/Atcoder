import collections
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
s = collections.Counter(s)
l = set(s)
t = collections.Counter(t)

ans = 0

for i in l:
    if s[i] - t[i] > ans:
        ans = max(ans, s[i] - t[i])

print(ans)
