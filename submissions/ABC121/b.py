n, m, c = map(int, input().split())
b = list(map(int, input().split()))

cnt = 0
for _ in range(n):
    a = list(map(int, input().split()))
    sum = 0
    for i in range(m):
        sum += a[i]*b[i]
    if sum + c > 0:
        cnt += 1

print(cnt)
