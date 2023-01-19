n = input()

c = int(n[0])
k = len(n)

if n[1:] == '9' * (k - 1):
    c += 9 * (k - 1)
else:
    c += 9 * (k - 1) - 1

print(c)
