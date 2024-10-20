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
    n, c = list(map(int, input().split()))

    t = list(map(int, input().split()))

    last_time = 0
    res = 0
    for i in range(n):
        cur_time = t[i] - last_time

        if cur_time < c and i != 0:
            continue
        else:
            res += 1
            last_time = t[i]

    print(res)

    return


if __name__ == "__main__":
    main()
