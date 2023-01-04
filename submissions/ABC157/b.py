a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())


def check(y, x):
    row = sum([a[y][i] for i in range(3)])
    col = sum([a[i][x] for i in range(3)])
    lcro = 1
    rcro = 1
    if y == x:
        lcro = sum([a[i][i] for i in range(3)])
    if y == 2-x:
        rcro = sum([a[i][2-i] for i in range(3)])
    return row and col and lcro and rcro


for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                a[i][j] = 0
                if check(i, j):
                    continue
                else:
                    print('Yes')
                    exit()

print('No')
