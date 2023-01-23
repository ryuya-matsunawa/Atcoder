from collections import defaultdict
n, m = map(int, input().split())
dict = defaultdict(bool)
ac = set()
wa = defaultdict(int)

for i in range(m):
    p, s = input().split()
    if s == 'AC':
        dict[p] = True
        ac.add(p)
    else:
        if not dict[p]:
            wa[p] += 1

wa = sum([wa[i] for i in ac])
print(len(ac), wa)
