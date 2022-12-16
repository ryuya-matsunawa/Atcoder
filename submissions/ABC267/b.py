S = input()

if S[0] == '1':
    print('No')
    exit()

col = [False] * 7
col[0] = S[6] == '1'
col[1] = S[3] == '1'
col[2] = S[1] == '1' or S[7] == '1'
col[3] = S[4] == '1'
col[4] = S[2] == '1' or S[8] == '1'
col[5] = S[5] == '1'
col[6] = S[9] == '1'

for i in range(7):
    for j in range(i):
        if col[i] and col[j]:
            for k in range(j+1, i):
                if not col[k]:
                    print('Yes')
                    exit()

print('No')
