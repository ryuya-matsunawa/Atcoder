n, m = map(int, input().split())

a = 0
b = float('inf')

for _ in range(m):
    l, r = map(int, input().split())
    a = max(a, l)
    b = min(b, r)

print(len(range(a, b+1)))
