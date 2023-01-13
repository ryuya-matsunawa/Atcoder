h, w = map(int, input().split())

for i in range(h+2):
    s = '#'*(w+2)
    if i == 0 or i == h+1:
        print(s)
    else:
        print('#'+input()+'#')
