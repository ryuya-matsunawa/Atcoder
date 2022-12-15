import itertools
S = [input() for _ in range(9)]

ans = 0
for y1, x1, y2, x2 in itertools.product(range(9), repeat=4):
    if x2 > x1 and y2 >= y1 and S[y1][x1] == '#' and S[y2][x2] == '#':
        x = x2 - x1
        y = y2 - y1
        x3 = x2 - y
        y3 = y2 + x
        x4 = x3 - x
        y4 = y3 - y
        l = [x3, y3, x4, y4]
        if min(l) >= 0 and max(l) <= 8 and S[y3][x3] == '#' and S[y4][x4] == '#':
            ans += 1

print(ans)
