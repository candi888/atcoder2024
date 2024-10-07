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
    edges_input = [list(map(int, input().split())) for i in range(n - 1)]
    v_input = list(map(int, input().split()))

    edges = [[] for i in range(n)]
    for u, v in edges_input:
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    def dfs(root, n, branches):
        stack = [~root, root]
        seen = [0] * n
        seen[root] = 1
        parent = [~root] * n  # 一番最後の根での帰りがけの時に都合がよいよう初期化

        while stack:
            cur = stack.pop()

            if cur >= 0:  # 行きがけ (今のcurからnxtへ行く)
                # curに来たときにやる処理

                for nxt in branches[cur]:  # edgeの定義
                    if not seen[nxt]:
                        seen[nxt] = 1
                        parent[nxt] = cur
                        stack.append(~nxt)
                        stack.append(nxt)

            elif cur < 0:  # 帰りがけ (今のcurからprvへ帰る)
                cur = ~cur
                prv = parent[cur]
                if prv == ~root:
                    break

                # curから出るときにやる処理

        return parent

    root = v_input[0] - 1
    parent = dfs(root=root, n=n, branches=edges)

    res_set = set()
    for vi in v_input:
        vi -= 1
        cur = vi

        if cur in res_set:
            continue

        while cur != root:
            res_set.add(cur)
            cur = parent[cur]

    res_set.add(root)
    print(len(res_set))

    return


if __name__ == "__main__":
    main()
