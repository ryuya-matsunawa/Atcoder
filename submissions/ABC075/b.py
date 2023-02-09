h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

d = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

for y in range(h):
    for x in range(w):
        if s[y][x] == '#':
            continue
        cnt = 0
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < w and 0 <= ny < h and s[ny][nx] == '#':
                cnt += 1
        s[y][x] = str(cnt)

for i in s:
    print(''.join(i))
