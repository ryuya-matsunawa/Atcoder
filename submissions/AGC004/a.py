a, b, c = map(int, input().split())

if a * b * c % 2 == 0:
    print(0)
    exit()

print(min(a*b, b*c, c*a))
