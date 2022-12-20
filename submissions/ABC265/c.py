from collections import defaultdict
H, W = map(int, input().split())
G = [input() for _ in range(H)]
visited = defaultdict(lambda: defaultdict(bool))
nx, ny = 0, 0

while 0 <= nx <= W-1 and 0 <= ny <= H-1:
    if visited[ny][nx]:
        print(-1)
        exit()
    g = G[ny][nx]
    visited[ny][nx] = True
    if g == 'R':
        nx += 1
        continue
    elif g == 'L':
        nx -= 1
        continue
    elif g == 'U':
        ny -= 1
        continue
    else:
        ny += 1
        continue

if ny < 0:
    ny += 2
    nx += 1
elif ny == H:
    nx += 1
elif nx < 0:
    nx += 2
    ny += 1
else:
    ny += 1
print(ny, nx)
