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
    n, m = list(map(int, input().split()))
    edges_input = [list(map(int, input().split())) for i in range(m)]

    edges = [[] for i in range(n)]
    edges_set = [set() for i in range(n)]
    for ai, bi in edges_input:
        edges[ai - 1].append(bi - 1)
        edges_set[ai - 1].add(bi - 1)

    # bfs
    dist = [INF] * n
    dist[0] = 0
    q = deque([0])
    while q:
        cur = q.popleft()
        for nxt in edges[cur]:

            if nxt ==0:
                print(dist[cur]+1)
                exit()
            elif dist[cur] + 1 < dist[nxt]:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    print(-1)

    return


if __name__ == "__main__":
    main()
