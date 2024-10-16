"""
--------------------------------------------------------------------------------------------------------------------------------
AtCoder用テンプレート
"""

import math
import operator
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heapify, heappop, heappush
from itertools import accumulate, permutations, product
from sys import setrecursionlimit, stdin


def input() -> str:
    return stdin.readline().strip()


# setrecursionlimit(700000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

INF = (1 << 61) - 1
MOD9, MOD10 = 998244353, 1000000007
"-------------------------------------------------------------------------------------------------------------------------------"


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    res = 0
    zero_to_right = [a[0]]
    for i in range(1, n):
        zero_to_right.append(zero_to_right[-1] ^ a[i])
        res += zero_to_right[-1]

    print(res)
    tmp = res
    for left in range(n - 2):
        tmp ^= a[left]
        res += tmp

    print(res)

    return


if __name__ == "__main__":
    main()
