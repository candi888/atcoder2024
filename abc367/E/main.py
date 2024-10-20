"""
------------------------------------------------------------------------------
AtCoder用テンプレート
"""

import math
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


def doubling(init_list: List[int], iter_num: int) -> List[int]:
    """
    K回同じ操作をした後の状態を知りたい（kがクソデカ整数）の場合に、o(k)をo(log(k))に落とせる。
    Dv[i][j]→jに2^i回操作したら何に飛んでいくか

    Args:
        init_list (List[int]):  一回操作をしたのち，入力したidxがどう移動するかの定義．0-indexに注意
        iter_num (int): ダブリング対象操作の繰り返し回数

    Returns:
        res_idx (List[int]): iter_num回繰り返し操作したあと，idxがどう移動するかの結果
    """

    # ダブリング用配列の列数．
    col_num = len(init_list)

    res_idx = list(range(col_num))

    # row_numの算出でlog(iter_num)を計算するので必要
    if iter_num == 0:
        return res_idx

    # ダブリング用配列の行数．
    row_num = int(math.log2(iter_num)) + 2

    # axis=0の+10はbuffer．理論上はlog_2(iter_num)でおｋ
    dv = [[0 for __ in range(col_num)] for _ in range(row_num)]

    for j in range(col_num):
        dv[0][j] = init_list[j]

    for i in range(row_num - 1):
        # 最初のスタートがjのとき，
        for j in range(col_num):
            # iのテーブルで2^i回動かしてから2^i回動かす．
            dv[i + 1][j] = dv[i][dv[i][j]]

    # bitが立っている場所を記録
    bit_idx_list = []
    for i in range(row_num):
        if iter_num >> i & 1:
            bit_idx_list.append(i)

    for idx in range(col_num):
        # 開始地点
        cur_idx = idx
        for i in bit_idx_list:
            # 1が立っているiについて2^i回を足し合わせれば答え
            cur_idx = dv[i][cur_idx]

        res_idx[idx] = cur_idx

    return res_idx


def main() -> None:
    n, k = list(map(int, input().split()))
    x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    res_idx = doubling(init_list=[xi - 1 for xi in x], iter_num=k)

    res = [a[idx] for idx in res_idx]
    print(*res)

    return


if __name__ == "__main__":
    main()
