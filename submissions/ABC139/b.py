A, B = map(int, input().split())

if B == 1:
    print(0)
    exit()

cnt = 1
total = A
while total < B:
    cnt += 1
    total += A - 1

print(cnt)
