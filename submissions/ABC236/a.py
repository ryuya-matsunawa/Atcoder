S = list(input())
a, b = map(int, input().split())

tmp = S[a-1]
S[a-1] = S[b-1]
S[b-1] = tmp

S = ''.join(S)
print(S)
