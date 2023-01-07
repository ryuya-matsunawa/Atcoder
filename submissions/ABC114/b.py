s = list(input())
x = 753
ans = 10000
for i in range(len(s)-2):
    r = s[i:i+3]
    ans = min(ans, abs(753-int(''.join(r))))

print(ans)
