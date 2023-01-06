n = int(input())

l = set()
m = set()

for _ in range(n):
    s = input()
    if '!' in s:
        m.add(s)
    else:
        l.add(s)

for s in l:
    if '!'+s in m:
        print(s)
        exit()

print('satisfiable')
