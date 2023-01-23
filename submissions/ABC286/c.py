import collections
n, a, b = map(int, input().split())
s = input()
sl = list(s)
l = collections.Counter(sl)

ans = []

for i in range(n//2):
    cnt = i*a
    for j in range(n//2):
        if s[j] != s[n-j-1]:
            cnt += b
    ans.append(cnt)
    ns = sl.pop(0)
    sl.append(ns)
    s = "".join(sl)

print(min(ans))
