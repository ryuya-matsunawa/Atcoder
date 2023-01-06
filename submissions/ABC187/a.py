a, b = map(str, input().split())

la = [int(i) for i in list(a)]
lb = [int(i) for i in list(b)]

print(max(sum(la), sum(lb)))
