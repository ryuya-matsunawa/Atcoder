import math

X, K = map(int, input().split())
for i in range(1, K+1):
    x_str = str(X)
    if i > len(x_str):
        break
    if int(x_str[-i]) >= 5:
        X = math.ceil(X / 10**i) * 10**i
    else:
        X = math.floor(X / 10**i) * 10**i
print(X)
