from collections import defaultdict
n, m = map(int, input().split())
l = [False]*(n+1)

dict = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        dict[a].append(b)
        if len(dict[a]) == 1:
            l[a] = True
        else:
            l[a] = False
    if b > a:
        dict[b].append(a)
        if len(dict[b]) == 1:
            l[b] = True
        else:
            l[b] = False

print(sum(l))
