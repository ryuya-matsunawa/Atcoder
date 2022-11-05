n = int(input())

if n >= 5:
    print("Yes")
else:
    ans = "Yes" if 2**n > n**2 else "No"
    print(ans)
