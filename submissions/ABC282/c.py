n = int(input())
s = list(input())

change = True
for i in range(n):
    if change and s[i] == ',':
        s[i] = '.'
    if s[i] == '"':
        change = not change

ans = ''.join(s)
print(ans)
