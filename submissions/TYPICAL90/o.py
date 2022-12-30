import numpy as np
n, k = map(int, input().split())

for _ in range(k):
    n = int(str(n), 8)
    n = np.base_repr(n, base=9)
    n = str(n).replace('8', '5')

print(int(n))
