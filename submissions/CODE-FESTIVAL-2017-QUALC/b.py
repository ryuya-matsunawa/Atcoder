n = int(input())
a = list(map(int, input().split()))

ans = 3 ** n
tmp = 1

for i in range(n):
    if a[i] % 2 == 0:
        tmp *= 2

ans -= tmp
print(ans)
