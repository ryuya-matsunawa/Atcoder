N, T = map(int, input().split())
A = list(map(int, input().split()))

if T > sum(A):
    T %= sum(A)

for i, a in enumerate(A):
    if T - a < 0:
        print(i+1, T)
        exit()
    T -= a
