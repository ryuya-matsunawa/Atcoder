from itertools import permutations
n = int(input())

l = list(permutations(range(1, n+1), n))

ans = []

p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

for i in l:
    tmp = 0
    for j in range(n-1):
        tmp += ((p[i[j]-1][0]-p[i[j+1]-1][0])**2 +
                (p[i[j]-1][1]-p[i[j+1]-1][1])**2)**(1/2)
    ans.append(tmp)

print(sum(ans)/len(ans))
