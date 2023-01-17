a, b, c, x, y = map(int, input().split())

if a+b > 2*c:
    if x > y:
        print(y*2*c+min(a*(x-y), 2*c*(x-y)))
    else:
        print(x*2*c+min(b*(y-x), 2*c*(y-x)))
else:
    print(a*x+b*y)
