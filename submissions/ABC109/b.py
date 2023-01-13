n = int(input())

w = input()
l = set([w])

for _ in range(n-1):
    s = input()
    if s in l or s[0] != w[-1]:
        print('No')
        exit()
    l.add(s)
    w = s

print('Yes')
