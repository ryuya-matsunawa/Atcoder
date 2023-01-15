import math
x = int(input())

if x < 4:
    print(1)
    exit()

for i in range(x, -1, -1):
    for j in range(2, int(math.sqrt(i))+1):
        for k in range(2, int(math.sqrt(i))+1):
            if j**k == i:
                print(i)
                exit()
