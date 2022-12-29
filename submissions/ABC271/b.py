n, q = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(n)]

for _ in range(q):
    s, t = map(int, input().split())
    print(l[s-1][t])
