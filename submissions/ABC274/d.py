N, x, y = map(int, input().split())
A = list(map(int, input().split()))

A_even = [A[i] for i in range(N) if i % 2 == 0]
A_odd = [A[i] for i in range(N) if i % 2 == 1]


def dp(l, s, f):
    st = set([s])
    for k in l:
        tmp = set([])
        for v in st:
            tmp.add(v + k)
            tmp.add(v - k)
        st = set(tmp)
    return f in st


if dp(A_even[1:], A_even[0], x) and dp(A_odd, 0, y):
    print('Yes')
else:
    print('No')
