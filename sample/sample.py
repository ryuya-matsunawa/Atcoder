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