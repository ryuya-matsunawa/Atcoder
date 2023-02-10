s = input()

l = len(s) - len('keyence')

for i in range(len('keyence')):
    if s[:i] + s[l+i:] == 'keyence':
        print("YES")
        exit()

print("NO")
