s = input()

ans = ''
for i in range(len(s)):
    if s[i] == '1':
        ans += '0'
    else:
        ans += '1'

print(ans)
