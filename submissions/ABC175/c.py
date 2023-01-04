x, k, d = map(int, input().split())

x = abs(x)
l = min(k, x//d)
k -= l
x -= l*d

if k % 2 == 1:
    print(d-x)
else:
    print(x)
