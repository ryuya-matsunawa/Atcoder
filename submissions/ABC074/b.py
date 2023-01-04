n = int(input())
k = int(input())
x = list(map(int, input().split()))

cnt = 0

for i in range(len(x)):
    cnt += min(x[i], k-x[i])*2

print(cnt)
