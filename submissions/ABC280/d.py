import math
K = int(input())

for i in range(1, 2*10**6):
    K //= math.gcd(K, i)
    if K == 1:
        print(i)
        exit()

print(K)
