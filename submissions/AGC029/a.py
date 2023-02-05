s = input()

ans = 0
wc = 0

for i in range(len(s)):
    if s[i] == 'B':
        continue
    if s[i] == 'W':
        ans += i - wc
        wc += 1

print(ans)
