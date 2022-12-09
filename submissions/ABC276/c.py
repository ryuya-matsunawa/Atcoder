N = int(input())

P = list(map(int, input().split()))

A = []

for i in range(N-1, -1, -1):
    n = P[i]
    if len(A) == 0:
        A.append(n)
    else:
        if min(A) > n:
            A.insert(0, n)
        else:
            A.insert(0, n)
            break

P = [i for i in P if i not in A]
f = A[0]
minA = 0

for a in A:
    if minA < a < f:
        minA = a

index = A.index(minA)
A[index] = f
A = sorted(A[1:], reverse=True)
ans = P + [minA] + A
print(*ans)
