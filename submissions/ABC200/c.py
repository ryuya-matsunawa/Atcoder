import collections
n = int(input())
a = list(map(int, input().split()))
a = [i % 200 for i in a]
c = collections.Counter(a)
ans = 0

for i in c.values():
    ans += i * (i - 1) // 2

print(ans)
