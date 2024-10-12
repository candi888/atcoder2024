"""
------------------------------------------------------------------------------
AtCoder用テンプレート
"""

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, permutations, product
from sys import setrecursionlimit, stdin
from typing import Dict, List, Set


def input() -> str:
    return stdin.readline().strip()


# setrecursionlimit(700000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

INF = (1 << 61) - 1
MOD9, MOD10 = 998244353, 1000000007
"------------------------------------------------------------------------------"


def main() -> None:
    n, k = list(map(int, input().split()))
    r = list(map(int, input().split()))

    all_list = list(product(*(range(1, x + 1) for x in r)))

    res = []
    for cur_list in all_list:
        if sum(cur_list) % k == 0:
            res.append(cur_list)

    res.sort()

    for elem in res:
        print(*elem)
    return


if __name__ == "__main__":
    main()
