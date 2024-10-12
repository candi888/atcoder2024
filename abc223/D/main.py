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


def topological_sort(n: int, edge: List[List[int]]) -> List[int]:
    """
    頂点0~n-1をもつ，edgeで繋がれた有向連結グラフに対し，トポロジカルソートを行う．
    returnされるトポロジカルソート後のグラフは頂点番号の並びが辞書順最小のものである．

    Args:
        n (int): 頂点数
        edge (List[List[int]]): グラフの辺．edge[i]には頂点iの行先のnodeの番号が格納されている

    Returns:
        sorted_list (List[int]): トポロジカルソート後の頂点番号の配列
    """

    # 各ノードの入次数
    in_cnt = [0 for i in range(n)]
    for from_node in range(n):
        for to_node in edge[from_node]:
            in_cnt[to_node] += 1

    # 何も入ってこない（どこにあろうが自由）ノードで初期化
    node_incnt_zero = [i for i in range(n) if in_cnt[i] == 0]
    # 辞書順最小にするためにheapqを使う
    heapify(node_incnt_zero)

    sorted_list = []
    while node_incnt_zero:
        cur = heappop(node_incnt_zero)
        sorted_list.append(cur)

        for nxt in edge[cur]:
            in_cnt[nxt] -= 1

            # もう何も入ってこないならば候補に入れる
            if in_cnt[nxt] == 0:
                heappush(node_incnt_zero, nxt)

    return sorted_list


def main() -> None:
    n, m = list(map(int, input().split()))
    edge_input = [list(map(int, input().split())) for i in range(m)]

    edge = [[] for i in range(n)]
    for fromnode, tonode in edge_input:
        edge[fromnode - 1].append(tonode - 1)

    sorted_node = topological_sort(n=n, edge=edge)

    if len(sorted_node) != n:
        print(-1)
    else:
        print(*[xi + 1 for xi in sorted_node])

    return


if __name__ == "__main__":
    main()
