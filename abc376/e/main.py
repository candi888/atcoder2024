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
    t = int(input())
    query = [list(map(int, input().split())) for i in range(3 * t)]

    for _ in range(t):
        n, k = query[3 * _][0]
        a = query[3 * _ + 1]
        b = query[3 * _ + 2]

        sorted_b_idx = [(bi, i) for i, bi in enumerate(b)]
        sorted_b_idx.sort(key=lambda x: x[0])
        acc_sorted_b = list(accumulate([0] + [bi for bi, _ in sorted_b_idx]))
        idx_to_sortedidx = [sortedidx for i, (_, sortedidx) in enumerate(sorted_b_idx)]

        res = INF

    return


if __name__ == "__main__":
    main()
