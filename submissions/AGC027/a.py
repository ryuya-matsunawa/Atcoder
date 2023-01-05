n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
cnt = 0
for i in range(n):
    if x >= a[i]:
        x -= a[i]
        cnt += 1
    else:
        print(cnt)
        exit()

if x > 0:
    print(cnt-1)
else:
    print(cnt)
