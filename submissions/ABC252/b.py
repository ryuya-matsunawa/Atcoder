N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_max = max(A)
A_index = [i for i, v in enumerate(A) if v == A_max]
B_in = any([i - 1 in A_index for i in B])
print("Yes" if B_in else "No")
