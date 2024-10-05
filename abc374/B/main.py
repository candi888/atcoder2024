"""
------------------------------------------------------------------------------
AtCoder用テンプレート
"""

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, product
from sys import setrecursionlimit, stdin
from typing import Dict, List, Set


def input() -> str:
    return stdin.readline().strip()


setrecursionlimit(700000)
# import pypyjit;pypyjit.set_param('max_unroll_recursion=-1')

INF = (1 << 61) - 1
MOD9, MOD10 = 998244353, 1000000007
"------------------------------------------------------------------------------"


def main() -> None:
    s = input()
    t = input()

    for i in range(max(len(s), len(t))):
        if i >= min(len(s), len(t)):
            print(i + 1)
            return

        if s[i] != t[i]:
            print(i + 1)
            return

    print(0)
    return


if __name__ == "__main__":
    main()
