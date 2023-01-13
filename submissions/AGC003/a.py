s = list(input())
s = sorted(list(set(s)))

if len(s) == 4 or list('NS') == s or list('EW') == s:
    print('Yes')
else:
    print('No')
