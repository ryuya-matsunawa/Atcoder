N = int(input())
A = list(map(int, input().split()))
l = [0 for _ in range(N)]

for a in A:
    l[a-1] += 1

ans = l.index(min(l)) + 1
print(ans)
