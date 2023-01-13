n = int(input())

p = list(map(int, input().split()))

cnt = 0
m = p[0]
for i in range(n):
    m = min(m, p[i])
    if m == p[i]:
        cnt += 1

print(cnt)
