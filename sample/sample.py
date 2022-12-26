s = input()
n = int(input())
n,m = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict
dict = defaultdict(int)

from itertools import combinations
combi = list(combinations(range(1, n+1), 2))

from itertools import accumulate
S0 = list(accumulate(a))

import math
math.ceil(1.2)
math.floor(1.2)
math.gcd(10,20,30)