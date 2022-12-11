S = input()

if len(S) != 8:
    print('No')
    exit()

s = S[0]
n = S[1:-1]
f = S[-1]

try:
    n = int(n)
except ValueError:
    print('No')
    exit()

if str.isalpha(s) and str.isalpha(f) and 100000 <= n <= 999999:
    print('Yes')
else:
    print('No')
