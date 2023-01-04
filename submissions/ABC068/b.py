from bisect import bisect
n = int(input())

l = [2**i for i in range(7)]

print(l[bisect(l, n)-1])
