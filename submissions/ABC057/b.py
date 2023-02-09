n, m = map(int, input().split())

l = []

for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])

check = []

for i in range(m):
    c, d = map(int, input().split())
    check.append([c, d])

for i in range(n):
    a, b = l[i]
    len = float('inf')
    ans_idx = 0
    for j in range(m):
        c, d = check[j]
        if abs(a-c) + abs(b-d) < len:
            len = abs(a-c) + abs(b-d)
            ans_idx = j
        elif abs(a-c) + abs(b-d) == len:
            ans_idx = min(ans_idx, j)

    print(ans_idx+1)
