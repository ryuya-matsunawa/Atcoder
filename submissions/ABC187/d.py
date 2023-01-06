n = int(input())

x = 0
l = []

for _ in range(n):
    a, b = map(int, input().split())
    x -= a
    l.append(2*a+b)

l.sort()
ans = 0
while x <= 0:
    k = l.pop()
    x += k
    ans += 1

print(ans)
