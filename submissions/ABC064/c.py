n = int(input())
a = list(map(int, input().split()))

a = [a[i] // 400 if a[i] < 3200 else 8 for i in range(n)]
sa = set([i for i in a if i != 8])
print(max(1, len(sa)), len(sa) + a.count(8))
