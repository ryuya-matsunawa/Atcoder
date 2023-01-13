s = list(input())
t = list(input())

for _ in range(len(s)):
    if s == t:
        print('Yes')
        exit()
    s.insert(0, s.pop())

print('No')
