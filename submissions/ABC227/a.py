N, K, A = map(int, input().split())
K -= 1

while K > 0:
    if A == N:
        A = 1
    else:
        A += 1
    K -= 1

print(A)
