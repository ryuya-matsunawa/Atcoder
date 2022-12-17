import math
n = float(input())

x = math.floor(n/1.08)
if math.floor(x * 1.08) == n:
    print(x)
elif math.floor((x+1) * 1.08) == n:
    print(x+1)
else:
    print(':(')
