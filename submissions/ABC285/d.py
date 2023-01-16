from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())

dict = defaultdict(str)
s_l = []
t_l = []

for _ in range(n):
    s, t = input().split()
    dict[t] = s
    s_l.append(s)
    t_l.append(t)

if sorted(s_l) == sorted(t_l):
    print('No')
    exit()

l = list((set(s_l) ^ set(t_l)) & set(t_l))
cnt = 0


def dfs(s):
    global cnt
    if dict[s] == '':
        return
    else:
        cnt += 1
        return dfs(dict[s])


for i in l:
    dfs(i)

if cnt == n:
    print('Yes')
else:
    print('No')
