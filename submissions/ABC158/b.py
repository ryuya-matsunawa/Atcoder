n, a, b = map(int, input().split())

cnt = n//(a+b) * a
n = n % (a+b)
if n > a:
    print(cnt+a)
else:
    print(cnt+n)
