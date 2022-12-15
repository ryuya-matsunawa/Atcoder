N = int(input())
P = list(map(int, input().split()))

cnt = [0] * N

for i in range(N):
    for j in range(3):
        cnt[(P[i]-1-i+j+N) % N] += 1

print(max(cnt))
