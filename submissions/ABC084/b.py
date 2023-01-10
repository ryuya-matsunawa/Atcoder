a, b = map(int, input().split())
s = input()

if not s[:a].isdigit() or s[a] != '-' or not s[a+1:].isdigit():
    print('No')
else:
    print('Yes')
