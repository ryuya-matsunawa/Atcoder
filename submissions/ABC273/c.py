import collections

N = int(input())
A = list(map(int, input().split()))

nums = list(set(A))
nums = sorted(nums)

idxs = {}

for i, num in enumerate(nums):
    idxs[num] = len(nums) - i - 1

A = [idxs[A[i]] for i in range(N)]
ans = collections.Counter(A)

for i in range(N):
    print(ans[i])
