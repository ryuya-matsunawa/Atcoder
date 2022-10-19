from collections import defaultdict

N = int(input())

A = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for a in A:
    if len(A[a]) == N - 1:
        print('Yes')
        exit()

print('No')
