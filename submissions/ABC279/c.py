H, W = map(int, input().split())

S = [[] for _ in range(W)]
T = [[] for _ in range(W)]

for _ in range(H):
    M = input()
    for i in range(W):
        S[i].append(M[i])

for _ in range(H):
    M = input()
    for i in range(W):
        T[i].append(M[i])

S.sort()
T.sort()

if S == T:
    print('Yes')
else:
    print('No')
