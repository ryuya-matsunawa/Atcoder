import collections
t = int(input())


def prime_factorize(n):
    while n % 2 == 0:
        if n % (2**2) == 0:
            return [2, n//(2**2)]
        else:
            return [int((n//2)**(1/2)), 2]
    f = 3
    while f * f <= n:
        if n % f == 0:
            if n % (f**2) == 0:
                return [f, n//(f**2)]
            else:
                return [int((n//f)**(1/2)), f]
        else:
            f += 2


for _ in range(t):
    n = int(input())
    l = prime_factorize(n)
    print(*l)
