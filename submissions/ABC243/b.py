N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B = {num: i for i, num in enumerate(B)}
A = {num: i for i, num in enumerate(A) if num in B.keys()}

cntA = 0
for num in A.keys():
    if A[num] == B[num]:
        cntA += 1
cntB = len(A) - cntA

print(cntA)
print(cntB)
