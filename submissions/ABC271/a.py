n = int(input())

h = hex(n)[2:]
if len(h) == 1:
    h = "0" + h

print(h.upper())
