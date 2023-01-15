x = int(input())

for i in range(x//100+1):
    for j in range(x//101+1):
        for k in range(x//102+1):
            for l in range(x//103+1):
                for m in range(x//104+1):
                    for n in range(x//105+1):
                        if i*100 + j*101 + k*102 + l*103 + m*104 + n*105 == x:
                            print(1)
                            exit()

print(0)
