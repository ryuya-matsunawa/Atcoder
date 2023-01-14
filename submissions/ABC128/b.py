from collections import defaultdict
n = int(input())

dict = defaultdict(list)
l = set()

for i in range(1, n+1):
    s, p = input().split()
    dict[s].append([i, int(p)])
    l.add(s)

l = sorted(list(l))

for i in l:
    dict[i] = sorted(dict[i], key=lambda x: x[1], reverse=True)
    for j in dict[i]:
        print(j[0])
