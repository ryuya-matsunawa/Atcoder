H, M = map(int, input().split())

T = [(h, m) for h in range(0, 24) for m in range(0, 60)]

while True:
    h = str(H)
    m = str(M)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    t = (int(h[0]+m[0]), int(h[1]+m[1]))

    if t in T:
        print(H, M)
        exit()
    if M == 59:
        M = 0
        H += 1
        if H == 24:
            H = 0
        continue
    M += 1
