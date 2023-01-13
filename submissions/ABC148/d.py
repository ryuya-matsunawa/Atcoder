n = int(input())
a = list(map(int, input().split()))

k = 1
cnt = 0

for i in range(n):
    if a[i] == k:
        k += 1
    else:
        cnt += 1

print(cnt if cnt != n else -1)
