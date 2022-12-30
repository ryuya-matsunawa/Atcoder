q = int(input())
l = []
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        l.insert(0, x)
    elif t == 2:
        l.append(x)
    else:
        print(l[x-1])
