x1, y1, x2, y2 = map(int, input().split())

i, j = x2-x1, y2-y1

x3, y3 = x2-j, y2+i
x4, y4 = x3-i, y3-j

print(x3, y3, x4, y4)
