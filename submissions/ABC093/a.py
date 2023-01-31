a, b, c = map(int, input().split())

even = [a % 2, b % 2, c % 2].count(0)
l = [a, b, c]

if even == 0 or even == 3:
    max = max(a, b, c)
    cnt = (max-a)//2 + (max-b)//2 + (max-c)//2
    print(cnt)
elif even == 1:
    for i in range(3):
        if l[i] % 2 == 1:
            l[i] += 1
    max = max(l)
    cnt = (max-l[0])//2 + (max-l[1])//2 + (max-l[2])//2
    print(cnt+1)
elif even == 2:
    for i in range(3):
        if l[i] % 2 == 0:
            l[i] += 1
    max = max(l)
    cnt = (max-l[0])//2 + (max-l[1])//2 + (max-l[2])//2
    print(cnt+1)
