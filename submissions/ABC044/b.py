import itertools
w = sorted(list(input()))

for k, g in itertools.groupby(w):
    if len(list(g)) % 2 == 1:
        print('No')
        exit()

print('Yes')
