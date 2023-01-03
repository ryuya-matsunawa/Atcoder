n = int(input())
a = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    i, *k = map(int, input().split())
    if i == 1:
        a[k[0]-1] = k[1]
    else:
        print(a[k[0]-1])
