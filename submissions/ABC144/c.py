n = int(input())

ans = float('inf')

for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        ans = min(ans, i-1+n//i-1)

print(ans)
