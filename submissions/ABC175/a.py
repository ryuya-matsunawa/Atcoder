s = list(input())
cnt = []
tmp = 0
for i in range(3):
    if s[i] == 'R':
        tmp += 1
    else:
        cnt.append(tmp)
        tmp = 0
cnt.append(tmp)
print(max(cnt))
