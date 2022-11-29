X, Y = map(int, input().split())

if Y-X > 0:
    a, b = (Y-X) // 10, (Y-X) % 10
    ans = a if b == 0 else a+1
else:
    ans = 0

print(ans)
