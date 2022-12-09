from collections import defaultdict
N, M = map(int, input().split())

dict = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

for i in range(1, N+1):
    print(len(dict[i]), *sorted(dict[i]))
