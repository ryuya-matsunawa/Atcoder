N = int(input())
S = set([])
for i in range(N):
    s = input()
    if s not in S:
        print(i+1)
        S.add(s)
