a, b, c = map(int, input().split())

for i in range(a, b*a, a):
    if i % b == c:
        print('YES')
        exit()
print('NO')
