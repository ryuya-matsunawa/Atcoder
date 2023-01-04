from bisect import bisect
n, m, x = map(int, input().split())
a = list(map(int, input().split()))
print(min(len(a[:bisect(a, x)]), len(a[bisect(a, x):])))
