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
    a, b, c = list(map(int, input().split()))

    if b > c:
        c += 24
        print("No" if (b <= a <= c or b <= a + 24 <= c) else "Yes")

    else:
        print("No" if b <= a <= c else "Yes")


if __name__ == "__main__":
    main()
