from collections import deque

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x = int(input())

que = deque([0])

visited = [False] * (x + 1)
can = [True] * (x + 1)
for i in b:
    can[i] = False

while que:
    now = que.popleft()
    if now == x:
        print('Yes')
        exit()
    if now > x:
        print('No')
        exit()
    if visited[now]:
        continue
    visited[now] = True
    for i in a:
        if now + i <= x and can[now + i]:
            que.append(now + i)

print('No')
