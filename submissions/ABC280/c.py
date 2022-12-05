S = list(input())
T = list(input())

for i in range(len(S)):
    if S[i] != T[i]:
        print(i+1)
        exit()

print(len(S)+1)
