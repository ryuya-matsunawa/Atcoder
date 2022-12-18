H, W = map(int, input().split())

if H == 1 or W == 1:
    print(1)
    exit()

ans = (H * W) // 2
if (H * W) % 2 == 1:
    ans += 1
print(ans)
