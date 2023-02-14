r, g, b, n = map(int, input().split())

l = [r, g, b]
l.sort()

ans = 0

for i in range(n//l[0]+1):
    for j in range((n-i*l[0])//l[1]+1):
        if (n-i*l[0]-j*l[1]) % l[2] == 0:
            ans += 1

print(ans)
