from collections import defaultdict
N = int(input())

A = defaultdict(list)

for _ in range(N):
    L = list(map(int, input().split()))
    L = L[1:]
    A[len(L)].append(L)

for i in A:
    A[i] = list(map(list, set(map(tuple, A[i]))))

ans = 0
for i in A:
    ans += len(A[i])

print(ans)
