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
    s = input()

    n = len(s)
    print(
        "Yes"
        if s[0] == "<"
        and all([s[i] == "=" for i in range(1, n - 1)])
        and s[n - 1] == ">"
        else "No"
    )
    return


if __name__ == "__main__":
    main()