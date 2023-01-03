import bisect
n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())

for _ in range(q):
    b = int(input())
    i = bisect.bisect(a, b)
    if i == 0:
        print(a[i]-b)
    elif i == len(a):
        print(b-a[i-1])
    else:
        print(min(b-a[i-1], a[i]-b))
