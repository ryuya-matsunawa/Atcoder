s = list(input())

n = int(s[0])
cnt = 0

for i in range(len(s)-1):
    if n == int(s[i+1]):
        cnt += 1
        n = (n+1) % 2
    else:
        n = int(s[i+1])

print(cnt)
