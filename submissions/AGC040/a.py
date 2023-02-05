s = input().replace('><', '>0<').split('0')
ans = 0

for i in s:
    s, t = i.count('<'), i.count('>')
    ans += s*(s-1)//2 + t*(t-1)//2 + max(s, t)

print(ans)
