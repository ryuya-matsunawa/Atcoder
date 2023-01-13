from collections import defaultdict
n, m = map(int, input().split())

dict = defaultdict(int)

for i in range(n):
    k, *a = map(int, input().split())
    for j in a:
        dict[j] += 1

cnt = 0
for i in range(1, m+1):
    if dict[i] == n:
        cnt += 1

print(cnt)
