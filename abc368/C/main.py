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
    n = int(input())
    h = list(map(int, input().split()))

    t = 0
    for curh in h:
        tmph = curh
        while tmph:
            if (t + 1) % 3 == 1 or (t + 1) % 3 == 2:
                t += 1
                tmph -= 1
            else:
                div, rem = tmph // 5, tmph % 5

                t += 3 * div
                tmph = rem

                if tmph == 0:
                    tmph = 0
                elif tmph <= 3:
                    t += 1
                else:
                    t += tmph - 2

                tmph = 0

    print(t)

    return


if __name__ == "__main__":
    main()
