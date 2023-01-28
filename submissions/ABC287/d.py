s = input()
t = input()
ns = len(s)
nt = len(t)


def match(a, b):
    return a == b or a == '?' or b == '?'


pre, suf = [False]*(ns+1), [False]*(ns+1)
pre[0] = True
suf[0] = True

for i in range(nt):
    if not match(s[i], t[i]):
        break
    pre[i+1] = True

s, t = s[::-1], t[::-1]
for i in range(nt):
    if not match(s[i], t[i]):
        break
    suf[i+1] = True

for i in range(nt+1):
    if pre[i] and suf[nt-i]:
        print('Yes')
    else:
        print('No')
