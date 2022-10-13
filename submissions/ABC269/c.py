import itertools

N = int(input())
l = []
for bit in range(60):
    if N & 1 << bit:
        l.append(bit)


def change(com):
    res = 0
    for n in com:
        res += 2**n
    return res


ans = []

for i in l:
    ans.append(2**i)

for count in range(2, len(l) + 1):
    for com in itertools.combinations(l, count):
        ans.append(change(com))

ans = sorted(ans)
print(0)
for a in ans:
    print(a)
