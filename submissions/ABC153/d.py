h = int(input())
cnt = 1
ans = 0
while h > 0:
    ans += cnt
    h //= 2
    cnt *= 2

print(ans)
