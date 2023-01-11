from collections import defaultdict
n, k, q = map(int, input().split())

dict = defaultdict(int)

for _ in range(q):
    a = int(input())
    dict[a] += 1

l = [k-q+dict[i+1] for i in range(n)]

for i in range(n):
    if l[i] <= 0:
        print('No')
    else:
        print('Yes')
