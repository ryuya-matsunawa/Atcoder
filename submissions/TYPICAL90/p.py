n = int(input())
a, b, c = map(int, input().split())
p = 10000
ans = p

for i in range(p):
    for j in range(p):
        k = n-(a*i+b*j)
        if k >= 0 and k % c == 0:
            if ans > i+j+k//c:
                ans = i+j+k//c

print(ans)
