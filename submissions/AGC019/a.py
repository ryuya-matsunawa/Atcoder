q, h, s, d = map(int, input().split())
n = int(input())
ans = 0

a = min(q*4, h*2, s)

if a*2 <= d:
    ans = a*n
else:
    ans = d*(n//2) + a*(n % 2)

print(ans)
