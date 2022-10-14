N = int(input())

A = [input() for _ in range(N)]

for i in range(N):
    for j in range(N - i):
        if i == N - j - 1:
            continue
        (Aij, Aji) = (A[i][N - j - 1], A[N - j - 1][i])
        if (Aij, Aji) in [('D', 'D'), ('W', 'L'), ('L', 'W')]:
            continue
        else:
            print('incorrect')
            exit()

print('correct')
