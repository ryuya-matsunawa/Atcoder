s = input()

l = list('ACGT')

cnt = []
tmp = 0
for i in range(len(s)):
    if s[i] in l:
        tmp += 1
    else:
        cnt.append(tmp)
        tmp = 0
cnt.append(tmp)

print(max(cnt))
