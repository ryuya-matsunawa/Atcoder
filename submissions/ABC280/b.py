N = int(input())

S = list(map(int, input().split()))

ans = [S[0]]

for i, s in enumerate(S):
    if i == 0:
        continue
    sum_s = s - sum(ans)
    ans.append(sum_s)

print(*ans)
