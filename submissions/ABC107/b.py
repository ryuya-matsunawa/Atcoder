h, w = map(int, input().split())

a = [list(input()) for _ in range(h)]

ri = []
ci = []

for i in range(h):
    if a[i].count('.') == w:
        ri.append(i)

for i in range(w):
    if [a[j][i] for j in range(h)].count('.') == h:
        ci.append(i)

for i in range(h):
    ans = ''
    if i in ri:
        continue
    for j in range(w):
        if j in ci:
            continue
        ans += a[i][j]
    print(ans)
