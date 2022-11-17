K = int(input())
b = str(bin(K)[2:])
ans = b.replace('1', '2')

print(ans)
