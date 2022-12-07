from collections import defaultdict
N, Q = map(int, input().split())

F = defaultdict(lambda: defaultdict(bool))

for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        F[a-1][b-1] = True
    if t == 2:
        F[a-1][b-1] = False
    if t == 3:
        if F[a-1][b-1] and F[b-1][a-1]:
            print('Yes')
        else:
            print('No')
