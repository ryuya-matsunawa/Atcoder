N = int(input())
X = list(map(int, input().split()))

ans = []
for i in range(1, 100):
    sum = 0
    for x in X:
        sum += (i-x)**2
    ans.append(sum)

print(min(ans))
