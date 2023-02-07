s = input()

for i in range(len(s))[::-1]:
    if i % 2 == 0:
        if s[:i//2] == s[i//2:i]:
            print(i)
            exit()
