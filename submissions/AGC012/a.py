n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
a = a[:2*n]
a = [a[i] for i in range(2*n) if i % 2 == 1]

ans = sum(a)

print(ans)
