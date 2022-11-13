L, R = map(int, input().split())
S = input()

l = S[:L-1]
c = S[L-1:R]
r = S[R:]

c = c[::-1]

ans = l + c + r
print(ans)
