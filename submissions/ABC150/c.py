from itertools import permutations
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

a = list(permutations(list(range(1, n+1))))

print(abs(a.index(tuple(p))-a.index(tuple(q))))
