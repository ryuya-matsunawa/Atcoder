import itertools
N, M = list(map(int, input().split()))

res = []

for m in range(1, M+1):
    l = list(map(int, input().split()))
    k_i = l.pop(0)
    for pair in itertools.combinations(l, 2):
        res.append(pair)
res = set(res)
count = N * (N - 1) / 2
result = "Yes" if len(res) == count else "No"
print(result)
