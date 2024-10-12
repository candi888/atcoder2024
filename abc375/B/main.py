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


def calc_dist(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5


def main() -> None:
    n = int(input())
    coordinates = [list(map(int, input().split())) for i in range(n)]

    cx, cy = 0, 0

    res = 0
    for nx, ny in coordinates:
        res += calc_dist(cx, cy, nx, ny)
        cx, cy = nx, ny

    res += calc_dist(cx, cy, 0, 0)

    print(res)
    return


if __name__ == "__main__":
    main()
