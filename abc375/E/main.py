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
    n, m, q = list(map(int, input().split()))
    edge_input = [list(map(int, input().split())) for i in range(m)]
    query = [list(map(int, input().split())) for i in range(q)]

    mindist = [[INF] * n for i in range(n)]

    removed_edge_index = set()
    for query_i in query:
        if query_i[0] == 1:
            ai, bi, ci = edge_input[query_i[1] - 1]
            ai -= 1
            bi -= 1

            # 辺の削除
            removed_edge_index.add(query_i[1] - 1)

    for i, (ai, bi, ci) in enumerate(edge_input):
        if i in removed_edge_index:
            continue
        ai -= 1
        bi -= 1

        mindist[ai][bi] = min(ci, mindist[ai][bi])
        mindist[bi][ai] = min(ci, mindist[bi][ai])

    # warshall
    for i in range(n):
        mindist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                mindist[i][j] = min(mindist[i][j], mindist[i][k] + mindist[k][j])

    # クエリ処理
    res_list = []
    for query_i in query[::-1]:
        if query_i[0] == 2:
            xi, yi = query_i[1] - 1, query_i[2] - 1
            res_list.append((mindist[xi][yi]) if mindist[xi][yi] != INF else -1)

        else:
            ai, bi, ci = edge_input[query_i[1] - 1]
            ai -= 1
            bi -= 1

            # 辺の追加
            for i in range(n):
                for j in range(n):
                    mindist[i][j] = min(
                        mindist[i][j], mindist[i][ai] + mindist[bi][j] + ci
                    )
                    mindist[i][j] = min(
                        mindist[i][j], mindist[i][bi] + mindist[ai][j] + ci
                    )

    for res in res_list[::-1]:
        print(res)
    return


if __name__ == "__main__":
    main()
