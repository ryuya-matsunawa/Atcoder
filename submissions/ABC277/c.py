from collections import defaultdict
N = int(input())

L = defaultdict(list)

for _ in range(N):
    A, B = map(int, input().split())
    L[A].append(B)
    L[B].append(A)

visited = defaultdict(bool)
visited[1] = True
q = [1]
ans = 1

while q:
    i = q.pop()
    ans = max(i, ans)
    for l in L[i]:
        if not visited[l]:
            q.append(l)
            visited[l] = True

print(ans)
