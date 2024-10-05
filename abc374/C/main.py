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
    n = int(input())
    k = list(map(int, input().split()))

    res = INF
    for bits in product([0, 1], repeat=n):
        groupa, groupb = 0, 0
        for idx, cur_bit in enumerate(bits):
            if cur_bit == 0:
                groupa += k[idx]
            else:
                groupb += k[idx]

        res = min(res, max(groupa, groupb))

    print(res)

    return


if __name__ == "__main__":
    main()
