a, b = map(str, input().split())
n = int(a+b)
if float.is_integer(n**(1/2)):
    print('Yes')
else:
    print('No')
