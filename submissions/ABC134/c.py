n = int(input())

a = [int(input()) for _ in range(n)]
s_a = sorted(a)[-2:]

if len(set(s_a)) == 1:
    for _ in range(n):
        print(s_a[0])
    exit()

for i in range(n):
    if a[i] == s_a[1]:
        print(s_a[0])
    else:
        print(s_a[1])
