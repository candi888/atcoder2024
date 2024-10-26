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
    n, m = list(map(int, input().split()))

    koma = [list(map(int, input().split())) for i in range(m)]

    cant_coordinate_set = set()

    dij = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for ai, bi in koma:
        cant_coordinate_set.add((ai - 1, bi - 1))
        for di, dj in dij:
            nxti, nxtj = ai - 1 + di, bi - 1 + dj

            if nxti < 0 or nxti >= n or nxtj < 0 or nxtj >= n:
                continue
            cant_coordinate_set.add((nxti, nxtj))

    # print(cant_coordinate_set)

    print(n**2 - len(cant_coordinate_set))

    return


if __name__ == "__main__":
    main()
