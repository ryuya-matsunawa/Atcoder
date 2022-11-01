N = int(input())
res = "Yes" if N >= -2**31 and N < 2**31 else "No"
print(res)
