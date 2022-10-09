N = int(input())

l = list(map(int, input().split()))
l = sorted(l, reverse=True)
l_odd = [i for i in l if i % 2 == 1]
l_even = [i for i in l if i % 2 == 0]
sum_odd = 0
sum_even = 0

for m in range(len(l_odd)):
    for n in range(1, len(l_odd) - m):
        sum_odd = l_odd[m] + l_odd[m + n]
        if sum_odd % 2 == 0:
            break
    else:
        continue
    break

for m in range(len(l_even)):
    for n in range(1, len(l_even) - m):
        sum_even = l_even[m] + l_even[m + n]
        if sum_even % 2 == 0:
            break
    else:
        continue
    break

max_num = sum_odd if sum_odd > sum_even else sum_even
res = max_num if max_num % 2 == 0 and max_num != 0 else -1
print(res)
