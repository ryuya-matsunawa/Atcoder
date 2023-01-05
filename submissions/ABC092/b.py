n = int(input())
d, x = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    a = int(input())
    for j in range(1, d+1, a):
        cnt += 1
print(x+cnt)
