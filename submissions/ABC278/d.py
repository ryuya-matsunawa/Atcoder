from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

base = 0

for g in range(1, Q+1):
    i, *q = map(int, input().split())
    if i == 1:
        base = q[0]
        A = defaultdict(int)
    elif i == 2:
        A[q[0]-1] += q[1]
    else:
        print(base + A[q[0]-1])
