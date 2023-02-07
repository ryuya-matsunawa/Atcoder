n = int(input())
s = list(input())

ans = 0
for i in range(n):
    ls = set(s[:i])
    rs = set(s[i:])
    ans = max(ans, len(ls & rs))

print(ans)
