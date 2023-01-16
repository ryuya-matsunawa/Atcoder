n = int(input())
s = input()

for i in range(1, n):
    cnt = 0
    for j in range(n-i):
        if s[j] != s[j+i]:
            cnt += 1
        else:
            print(cnt)
            break
    else:
        print(cnt)
