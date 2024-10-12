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

import numpy as np


def input() -> str:
    return stdin.readline().strip()


# setrecursionlimit(700000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

INF = (1 << 61) - 1
MOD9, MOD10 = 998244353, 1000000007
"------------------------------------------------------------------------------"


def main() -> None:
    q = int(input())

    query = [list(map(int, input().split())) for i in range(q)]

    cnter = Counter()
    for queryi in query:
        if queryi[0] == 1:
            x = queryi[1]

            cnter[x] += 1
        elif queryi[0] == 2:
            x = queryi[1]
            cnter[x] -= 1
            if cnter[x] == 0:
                # 2 今ゼロになったキーだけ削除
                del cnter[x]

        else:
            # ↓遅いのでボツ！！！
            # # 1 ゼロ以下の要素を削除
            # cnter += Counter()
            print(len(cnter))

    return


if __name__ == "__main__":
    main()
