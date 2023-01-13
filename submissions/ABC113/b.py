n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

l = [abs(a-(t-h[i]*0.006)) for i in range(n)]
print(l.index(min(l))+1)
