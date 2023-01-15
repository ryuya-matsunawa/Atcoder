s = input()

s1 = s2 = ""

ans = 0

for i in range(len(s)):
    s2 += s[i]
    if s1 != s2:
        ans += 1
        s1 = s2
        s2 = ""

print(ans)
