V, A, B, C = map(int, input().split())

while V >= 0:
    if V-A < 0:
        print('F')
        exit()
    elif V - A - B < 0:
        print('M')
        exit()
    elif V - A - B - C < 0:
        print('T')
        exit()
    else:
        V = V - A - B - C
