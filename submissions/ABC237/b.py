H, W = map(int, input().split())

A = [[]] * H

for i in range(H):
    l = list(map(int, input().split()))
    A[i] = l

for l in list(map(list, zip(*A))):
    print(*l)
