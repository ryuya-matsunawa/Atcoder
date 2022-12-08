N = int(input())

f = ['H', 'D', 'C', 'S']
s = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

L = []

for _ in range(N):
    S = input()
    if S[0] not in f or S[1] not in s or S in L:
        print('No')
        exit()
    L.append(S)

print('Yes')
