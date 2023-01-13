o = input()
e = input()

ans = ''

for i in range(len(o)+len(e)):
    ans += o[i//2] if i % 2 == 0 else e[i//2]

print(ans)
