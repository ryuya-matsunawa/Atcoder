from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

L = [input() for _ in range(R)]
G = [[-1]*C for _ in range(R)]

G[sy-1][sx-1] = 0
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

que = deque()
que.append((sy-1, sx-1))

while que:
    y, x = que.popleft()
    for i, j in d:
        nx = x+i
        ny = y+j
        if 0 <= nx < C and 0 <= ny < R and G[ny][nx] == -1 and L[ny][nx] == '.':
            G[ny][nx] = G[y][x] + 1
            que.append((ny, nx))

print(G[gy-1][gx-1])
