a, b, k = map(int, input().split())

if b-a < k:
    for i in range(a, b+1):
        print(i)
    exit()

l = list(range(a, a+k)) + list(range(b-k+1, b+1))
l = sorted(list(set(l)))

for i in l:
    print(i)
