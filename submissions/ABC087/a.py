n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

l = [a[0][:i+1] + a[1][i:] for i in range(n)]

print(max([sum(i) for i in l]))
