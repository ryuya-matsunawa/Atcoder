a, b = map(int, input().split())

if a <= 0 <= b:
    print('Zero')
    exit()

if a <= 0 and b <= 0 and (b-a+1) % 2 == 1:
    print('Negative')
    exit()

print('Positive')
