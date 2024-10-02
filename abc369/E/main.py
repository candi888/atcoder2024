from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import accumulate, product, permutations
from sys import setrecursionlimit, stdin


def input() -> str:
    return stdin.readline().strip()


setrecursionlimit(700000)
# import pypyjit;pypyjit.set_param('max_unroll_recursion=-1')

INF = (1 << 61) - 1
MOD9, MOD10 = 998244353, 1000000007
"------------------------------------------------------------------------------"


def main() -> None:
    n, m = list(map(int, input().split()))
    edges_input = [list(map(int, input().split())) for i in range(m)]
    q = int(input())

    edges = [[] for i in range(n)]
    for u, v, cost in edges_input:
        u -= 1
        v -= 1
        edges[u].append((v, cost))
        edges[v].append((u, cost))

    min_dist = [[INF for i in range(n)] for j in range(n)]
    for u in range(n):
        min_dist[u][u] = 0
        for v, cost in edges[u]:
            min_dist[u][v] = min(min_dist[u][v], cost)
            min_dist[v][u] = min(min_dist[v][u], cost)
    # warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                min_dist[i][j] = min(min_dist[i][j], min_dist[i][k] + min_dist[k][j])

    # query
    for qi in range(q):
        ki = int(input())
        bridges_must = list(map(int, input().split()))

        res = INF
        for bridges_order in permutations(bridges_must, ki):
            for start_or_end_bits in product([0, 1], repeat=ki):
                cur_dist = 0
                cur_island = 0

                for i, bit in enumerate(start_or_end_bits):
                    cur_bridge = bridges_order[i] - 1
                    u, v, cost = edges_input[cur_bridge]
                    u -= 1
                    v -= 1

                    if bit:
                        nxt_island = u
                        cur_dist += min_dist[cur_island][nxt_island]
                        cur_island = v
                        cur_dist += cost
                    else:
                        nxt_island = v
                        cur_dist += min_dist[cur_island][nxt_island]
                        cur_island = u
                        cur_dist += cost

                # 最後だけべつ
                nxt_island = n - 1
                cur_dist += min_dist[cur_island][nxt_island]

                if cur_dist < res:
                    res = cur_dist

        print(res)

    return


if __name__ == "__main__":
    main()
