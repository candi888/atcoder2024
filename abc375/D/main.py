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

    leftcnt = Counter(list(s)[0])
    rightcnt = Counter(list(s)[2:])
    n = len(s)

    res = 0

    alphalist = [chr(i) for i in range(ord("A"), ord("Z") + 1)]

    for centeridx in range(1, n - 1):
        for alphabet in alphalist:
            res += leftcnt[alphabet] * rightcnt[alphabet]

        leftcnt[s[centeridx]] += 1
        rightcnt[s[centeridx + 1]] -= 1

    print(res)

    return


if __name__ == "__main__":
    main()
