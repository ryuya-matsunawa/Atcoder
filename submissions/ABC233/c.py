import itertools
N, X = map(int, input().split())

a_list = []

for _ in range(N):
    _, *a = list(map(int, input().split()))
    a_list.append(a)


def prod(l):
    prod = 1
    for i in l:
        prod *= i
    return prod


combi = [prod(l) for l in list(itertools.product(*a_list))]
ans = list(filter(lambda x: x == X, combi))

print(len(ans))
