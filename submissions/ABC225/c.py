from math import ceil

N, M = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(N)]

i = ceil(B[0][0]/7)
j = B[0][0] % 7 or 7

A = [list(range((i - 1 + n) * 7 + j, (i - 1 + n) * 7 + j + M))
     for n in range(N)]

for l in A:
    for n in l[:-1]:
        if n % 7 == 0:
            print('No')
            exit()

if A == B:
    print('Yes')
else:
    print('No')
