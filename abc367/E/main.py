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
    x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    # ダブリング
    dv = [[0 for j in range(n)] for i in range(100)]

    # TODO 一回操作をしたらjは何に飛んでいくかの定義。Rangeはピッタリに
    for j in range(n):
        dv[0][j] = x[j] - 1

    # log(k)でおｋ
    for i in range(99):
        # 最初のスタートがj
        for j in range(n):
            # iのテーブルで2^i回動かしてから2^i回動かす
            dv[i + 1][j] = dv[i][dv[i][j]]

    bit_1_list = []
    for i in range(100):
        if k >> i & 1:
            bit_1_list.append(i)

    res = []
    for idx in range(n):
        # 開始地点
        cur_idx = idx
        for i in bit_1_list:
            cur_idx = dv[i][cur_idx]  # 1が立っているiについて2^i回を足し合わせれば答え

        res.append(a[cur_idx])

    print(*res)

    return


if __name__ == "__main__":
    main()
