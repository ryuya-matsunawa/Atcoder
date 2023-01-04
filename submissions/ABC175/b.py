n = int(input())
l = sorted(list(map(int, input().split())))

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if l[i] == l[j] or l[j] == l[k]:
                continue
            if l[j] - l[i] < l[k] < l[i] + l[j]:
                cnt += 1

print(cnt)
