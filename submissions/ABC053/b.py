s = input()

a = []
z = []

for i in range(len(s)):
    if s[i] == 'A':
        a.append(i)
    if s[i] == 'Z':
        z.append(i)

print(max(z) - min(a) + 1)
