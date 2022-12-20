x, y, n = map(int, input().split())
ans = 0
if x*3 > y:
    ans += (n // 3) * y
    n = n % 3
ans += n * x
print(ans)
