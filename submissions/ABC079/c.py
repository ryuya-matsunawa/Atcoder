n = list(input())
a, b, c, d = int(n[0]), int(n[1]), int(n[2]), int(n[3])

for i in range(2):
    for j in range(2):
        for k in range(2):
            if i == 0:
                x = a+b
            else:
                x = a-b
            if j == 0:
                y = x+c
            else:
                y = x-c
            if k == 0:
                z = y+d
            else:
                z = y-d
            if z == 7:
                if i == 0:
                    s = '+'
                else:
                    s = '-'
                if j == 0:
                    t = '+'
                else:
                    t = '-'
                if k == 0:
                    u = '+'
                else:
                    u = '-'
                print(f'{a}{s}{b}{t}{c}{u}{d}=7')
                exit()
