h, w = map(int, input().split())

s = [input() for _ in range(h)]

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for y in range(h):
    for x in range(w):
        if s[y][x] == '#':
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0 <= nx < w and 0 <= ny < h:
                    if s[ny][nx] == '#':
                        break
            else:
                print('No')
                exit()

print('Yes')
