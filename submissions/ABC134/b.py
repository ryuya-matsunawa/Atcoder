import math
n, d = map(int, input().split())

d = d*2+1

print(math.ceil(n/d))
