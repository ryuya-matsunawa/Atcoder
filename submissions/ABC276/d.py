from collections import defaultdict
N = int(input())

A = list(map(int, input().split()))

cnt = 0


def divide2(n):
    cnt = 0
    if n % 2 != 0:
        return (n, cnt)
    else:
        while n % 2 == 0:
            n //= 2
            cnt += 1
        return (n, cnt)


def divide3(n):
    cnt = 0
    if n % 3 != 0:
        return (n, cnt)
    else:
        while n % 3 == 0:
            n //= 3
            cnt += 1
        return (n, cnt)


minA = []
dict = defaultdict(list)

for a in A:
    a1, cnt2 = divide2(a)
    a2, cnt3 = divide3(a1)
    minA.append(a2)
    dict[2].append(cnt2)
    dict[3].append(cnt3)

if len(set(minA)) > 1:
    print(-1)
    exit()

for i in [2, 3]:
    while 0 not in dict[i]:
        dict[i] = [k - 1 for k in dict[i]]

sum2 = sum(dict[2])
sum3 = sum(dict[3])

print(sum2+sum3)
