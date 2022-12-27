N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0

for i in range(N):
    cnt += abs(A[i]-B[i])

if K-cnt < 0:
    print('No')
    exit()

if (K-cnt) % 2 == 0:
    print('Yes')
else:
    print('No')
