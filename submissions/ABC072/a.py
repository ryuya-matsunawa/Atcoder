from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

dict = defaultdict(int)

d = [-1, 0, 1]

for i in range(n):
    for j in d:
        dict[a[i]+j] += 1

print(max(dict.values()))
