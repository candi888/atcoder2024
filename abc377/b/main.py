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
    grid = [list(input()) for i in range(8)]

    res_grid = [[1] * 8 for i in range(8)]

    for komai in range(8):
        for komaj in range(8):
            if grid[komai][komaj] == "#":
                for checki in range(8):
                    res_grid[checki][komaj] = 0
                for checkj in range(8):
                    res_grid[komai][checkj] = 0
    
    res=0
    for i in range(8):
        res+=sum(res_grid[i])

    print(res)

    return


if __name__ == "__main__":
    main()
