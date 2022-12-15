from functools import lru_cache
N = int(input())


@lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return 1
    return f(n//2) + f(n//3)


print(f(N))
