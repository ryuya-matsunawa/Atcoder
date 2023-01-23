n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

tmp = a[p-1:q]
a[p-1:q] = a[r-1:s]
a[r-1:s] = tmp
print(*a)
