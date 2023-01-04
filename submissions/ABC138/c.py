n = int(input())
v = sorted(list(map(int, input().split())))

while len(v) > 1:
    nv = (v[0]+v[1])/2
    v = v[2:]
    v.insert(0, nv)

print(v[0])
