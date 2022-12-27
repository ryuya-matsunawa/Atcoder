import math
import functools
A, B, C = map(int, input().split())


def my_gcd(*integers):
    return functools.reduce(math.gcd, integers)


n = my_gcd(A, B, C)

ans = 0
ans += (A-n)//n
ans += (B-n)//n
ans += (C-n)//n
print(ans)
