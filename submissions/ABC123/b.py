l = [int(input()) for _ in range(5)]

c = [(l[i]-1) % 10 for i in range(5)]
last = c.index(min(c))

ans = 0
for i in range(5):
    if i == last:
        ans += l[i]
    else:
        if l[i] % 10 == 0:
            ans += l[i]
        else:
            ans += (l[i]//10+1)*10
print(ans)
