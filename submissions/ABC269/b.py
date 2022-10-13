b = []
for k in range(1, 11):
    l = input()
    l = [(k, i + 1) for i, x in enumerate(l) if x == '#']
    b.append(l)
b = [l for l in b if len(l) > 0]
A, C = b[0][0]
B, D = b[-1][-1]
print(A, B)
print(C, D)
