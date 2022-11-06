import numpy as np

N = int(input())
A = list(map(int, input().split()))

ans = [0]

now = 0

for a in A:
    now += a
    now %= 360
    ans.append(now)

ans.append(360)
ans.sort()

arr = np.array(ans)
diff = np.diff(arr)
num = np.amax(diff)
print(num)
