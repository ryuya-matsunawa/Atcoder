N = int(input())

S = list(map(int, input().split()))
M = []
for a in range(1, 150):
    for b in range(1, 150):
        if 4*a*b + 3*a + 3*b <= 1000:
            M.append(4*a*b + 3*a + 3*b)

M = set(M)
M = sorted(M)

cnt = 0


for s in S:
    if s not in M:
        cnt += 1

print(cnt)
