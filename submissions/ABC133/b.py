from itertools import combinations
n, d = map(int, input().split())

ans = 0

l = list(list(map(int, input().split())) for _ in range(n))

combi = list(combinations(l, 2))

for i in range(len(combi)):
    tmp = 0
    for j in range(d):
        tmp += (combi[i][0][j] - combi[i][1][j])**2
    tmp = tmp**(1/2)
    if tmp.is_integer():
        ans += 1

print(ans)
