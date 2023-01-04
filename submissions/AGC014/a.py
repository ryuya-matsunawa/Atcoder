l = list(map(int, input().split()))


def is_even(l):
    for i in range(3):
        if l[i] % 2 == 1:
            return False
    return True


tmp = l
cnt = 0
while is_even(l):
    l = [(l[i]+l[(i+1) % 3])//2 for i in range(3)]
    if tmp == l:
        print(-1)
        exit()
    cnt += 1

print(cnt)
