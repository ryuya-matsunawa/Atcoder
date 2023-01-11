s = sorted(set(list(input())))

l = [chr(ord("a")+i) for i in range(26)]

for i in l:
    if i not in s:
        print(i)
        exit()

print('None')
