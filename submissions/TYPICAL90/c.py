from itertools import combinations
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for i, j, k, l, m in combinations(A, 5):
    if i * j % P * k % P * l % P * m % P == Q:
        cnt += 1

print(cnt)
