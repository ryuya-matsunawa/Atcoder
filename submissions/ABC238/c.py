N = int(input())

d = len(str(N))

ans = 0


def sum_n(d):
    n = 10 ** d - 10**(d-1)
    if 10 ** d - 1 > N:
        n = N - (10**(d - 1) - 1)
    s = (n + 1) * n // 2
    return s


for i in range(1, d+1):
    ans += sum_n(i)

print(int(ans % 998244353))
