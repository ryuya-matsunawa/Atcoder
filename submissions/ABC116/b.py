s = int(input())

l = [s]
i = 1


def f(n):
    if n % 2 == 1:
        return 3*n + 1
    else:
        return n // 2


while True:
    n = f(l[i-1])
    if n in l:
        print(i+1)
        exit()
    l.append(n)
    i += 1
