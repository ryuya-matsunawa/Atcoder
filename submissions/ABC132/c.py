n = int(input())
d = sorted(list(map(int, input().split())))
print(max(0, d[len(d)//2]-d[len(d)//2-1]))
