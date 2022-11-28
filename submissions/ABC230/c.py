N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

k_min, k_max = max(1-A, 1-B), min(N-A, N-B)
l_min, l_max = max(1-A, B-N), min(N-A, B-1)

for n in range(P, Q+1):
    line = ['.']*(S-R+1)
    k = n-A
    if k_min <= k <= k_max and 0 <= B+k-R <= len(line)-1:
        line[B+k-R] = '#'
    if l_min <= k <= l_max and 0 <= B-k-R <= len(line)-1:
        line[B-k-R] = '#'
    ans = ''.join(line)
    print(ans)
