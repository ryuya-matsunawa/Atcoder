from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

dict = defaultdict(int)

for i, a in enumerate(A):
    dict[2*(i+1)] = a
    dict[2*(i+1)+1] = a

dict[1] = 0
ans = defaultdict(int)
ans[1] = 0
for i in range(2, 2*N+2):
    ans[i] = ans[dict[i]] + 1

for i in range(1, 2*N+2):
    print(ans[i])
