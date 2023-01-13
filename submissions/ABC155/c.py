from collections import defaultdict
n = int(input())
c = defaultdict(int)
dict = defaultdict(list)
max = 0
for i in range(n):
    s = input()
    c[s] += 1
    if c[s] > max:
        max = c[s]
    dict[c[s]].append(s)

for i in sorted(dict[max]):
    print(i)
