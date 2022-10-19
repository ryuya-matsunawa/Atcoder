from collections import defaultdict
N = int(input())

XY = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])
    Y.append(y)

Y = list(set(Y))
S = input()

XR = defaultdict(list)
XL = defaultdict(list)

for y in Y:
    XR[y]
    XL[y]

for s, (x, y) in zip(S, XY):
    if s == 'R':
        XR[y].append(x)
    else:
        XL[y].append(x)

for y in Y:
    if len(XR[y]) == 0 or len(XL[y]) == 0:
        continue
    if min(XR[y]) < max(XL[y]):
        print('Yes')
        exit()

print('No')
