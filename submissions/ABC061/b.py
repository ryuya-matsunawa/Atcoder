from collections import defaultdict
n, m = map(int, input().split())

dict = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

for i in range(1, n+1):
    print(len(dict[i]))
