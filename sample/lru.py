from functools import lru_cache
n = int(input())

# メモ化再帰
@lru_cache(maxsize=1000)
def l(i):
    if i == 0:
        return 2
    if i == 1:
        return 1
    return l(i-1) + l(i-2)

print(l(n))