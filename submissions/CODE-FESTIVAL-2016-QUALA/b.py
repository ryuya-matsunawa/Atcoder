from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

dict = defaultdict(int)

for i in range(n):
    dict[i+1] = a[i]

cnt = 0
for i in range(n):
    if dict[a[i]] == i+1:
        cnt += 1

print(cnt//2)
