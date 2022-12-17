n, a, b = map(int, input().split())
s = input()

cnt = 0
cntB = 0

for i in range(n):
    if s[i] == 'a':
        if cnt < a + b:
            cnt += 1
            print('Yes')
        else:
            print('No')
        continue
    if s[i] == 'b':
        if cnt < a + b and cntB < b:
            cnt += 1
            cntB += 1
            print('Yes')
        else:
            print('No')
        continue
    if s[i] == 'c':
        print('No')
