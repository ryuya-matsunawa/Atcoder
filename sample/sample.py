s = input()
n = int(input())
n,m = map(int, input().split())
a = list(map(int, input().split()))

# 再帰関数の上限を変更
import sys
sys.setrecursionlimit(10 ** 7)

from collections import defaultdict
dict = defaultdict(int)

from itertools import combinations
combi = list(combinations(range(1, n+1), 2))

from itertools import permutations
perm = list(permutations(range(1, n+1), 2))

from itertools import accumulate
S0 = list(accumulate(a))

import math
math.ceil(1.2)
math.floor(1.2)
math.gcd(10,20,30)

# xを9進数に変換
import numpy as np
n = np.base_repr(x, base=9)

# 8進数の文字列を10進数に変換
n = int(str(n), 8)

# 素数判定
def is_prime(n):
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

# アルファベット→数値
def alpha2num(alpha):
    num=0
    for index, item in enumerate(list(alpha)):
        num += pow(26,len(alpha)-index-1)*(ord(item)-ord('A')+1)
    return num


from collections import defaultdict
# n種類の硬貨があり、それぞれの硬貨の枚数は無限にある。
# これらの硬貨の中から何枚かを選び、その総額をちょうどx円にする方法は何通りあるか。
n,x = map(int, input().split())

# a円硬貨をb枚持っている
dict = defaultdict(int)
# 硬貨の種類
l = []

for i in range(n):
    a,b = map(int, input().split())
    dict[a] = b
    l.append(a)

# 硬貨の種類の昇順に並び替え
l.sort(reverse=True)

def check():
    for i in range(n):
        # 硬貨の種類の昇順に並び替えたものを使って、x円を作る
        # 使う枚数は、x円をその硬貨で割った商と、その硬貨の枚数の小さい方
        # 使った枚数を引いて、次の硬貨で作る
        x -= l[i] * min(x//l[i], dict[l[i]])
    return x == 0

for i in l:
    print(i)
    if check():
        print("Yes")
        exit()
    else:
        l.shift()

print("No")