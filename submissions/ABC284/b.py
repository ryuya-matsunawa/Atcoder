t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd = [a[i] for i in range(n) if a[i] % 2 == 1]
    print(len(odd))
