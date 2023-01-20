n = int(input())
a = list(map(int, input().split()))

a = [a[i] for i in range(n) if a[i] % 2 == 0]


def divide2(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    return cnt


for i in range(len(a)):
    a[i] = divide2(a[i])

print(sum(a))
