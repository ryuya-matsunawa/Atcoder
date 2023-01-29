n, m = map(int, input().split())
s = list(input() for _ in range(n))
t = list(input() for _ in range(m))

cnt = 0
for i in range(n):
    if s[i][-3:] in t:
        cnt += 1
print(cnt)
