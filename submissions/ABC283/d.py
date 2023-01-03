from collections import defaultdict
s = list(input())

used = defaultdict(bool)
c = 0
x = [set([]) for _ in range(len(s))]

for i in range(len(s)):
    m = s[i]
    if m == '(':
        x.append(set([]))
        c += 1
        continue
    elif m == ')':
        for k in x[c-1]:
            used[k] = False
        x[c-1].clear()
        c -= 1
    else:
        if used[m]:
            print('No')
            exit()
        else:
            x[c-1].add(m)
            used[m] = True

print('Yes')
