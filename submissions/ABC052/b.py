n = int(input())
s = input()
x = [0]
for i in range(n):
    if s[i] == 'I':
        x.append(x[i]+1)
    else:
        x.append(x[i]-1)
print(max(x))
