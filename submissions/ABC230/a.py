N = int(input())

if N >= 42:
    N += 1

ans = 'AGC' + str(N).zfill(3)

print(ans)
