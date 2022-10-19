import itertools

H, W = map(int, input().split())

A = [[i for i in list(map(int, input().split()))] for _ in range(H)]

h = list(range(H))
w = list(range(W))
h_combi = list(itertools.combinations(h, 2))
w_combi = list(itertools.combinations(w, 2))

full = []

for i1, i2 in h_combi:
    for j1, j2 in w_combi:
        full.append((i1, i2, j1, j2))

for i1, i2, j1, j2 in full:
    if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
        print('No')
        exit()

print("Yes")
