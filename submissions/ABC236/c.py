from collections import defaultdict

N, M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

ans = defaultdict(list)

for s in S:
    ans[s] = 'No'

for t in T:
    ans[t] = 'Yes'

for i in ans:
    print(ans[i])
