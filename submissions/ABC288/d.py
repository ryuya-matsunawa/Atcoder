from itertools import accumulate
n, k = map(int, input().split())
a = list(map(int, input().split()))

acc = [[0] + list(accumulate([a[i]*(i % k == j) for i in range(n)]))
       for j in range(k)]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    s = acc[0][r] - acc[0][l]
    for i in range(1, k):
        if s != acc[i][r] - acc[i][l]:
            print("No")
            break
    else:
        print("Yes")
