"""
------------------------------------------------------------------------------
AtCoder用テンプレート
"""

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush

# from itertools import accumulate, permutations, product
from sys import setrecursionlimit, stdin
from typing import Dict, List, Set

# import numpy as np


def input() -> str:
    return stdin.readline().strip()


# setrecursionlimit(700000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

INF = (1 << 61) - 1
MOD9, MOD10 = 998244353, 1000000007
"------------------------------------------------------------------------------"


def main() -> None:
    n = int(input())
    s = [input() for i in range(n)]

    for col in range(max([len(si) for si in s])):
        cur_s_list = []
        for row in range(n)[::-1]:
            cur_s_list.append(s[row][col] if col < len(s[row]) else "*")
        print("".join(cur_s_list).rstrip("*"))
    return


if __name__ == "__main__":
    main()
