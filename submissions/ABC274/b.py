h, w = map(int, input().split())

ans = [0] * w

for _ in range(h):
    C = list(input())
    for i in range(w):
        if C[i] == '#':
            ans[i] += 1

print(*ans)
