k, n = map(int, input().split())
a = list(map(int, input().split()))
l = [a[i+1]-a[i] for i in range(n-1)]
l.append(k-a[-1]+a[0])
l.remove(max(l))
print(sum(l))
