from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import accumulate, product
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

    edges = [[] for i in range(n)]
    for u, v, w in edges_input:
        u -= 1
        v -= 1
        edges[u].append((v, w))
        edges[v].append((u, -w))

    seen = [0] * n
    seen[0] = 1
    res = [None] * n

    for start in range(n):
        if res[start] is None:
            res[start] = 0

            # DFS
            stack = [start]
            while stack:
                cur = stack.pop()
                seen[cur] = 1

                # 頂点に入った時の処理はここ

                for nxt, cost in edges[cur]:
                    if not seen[nxt]:
                        stack.append(nxt)
                        seen[nxt] = 1
                        res[nxt] = res[cur] + cost

                        # 次行く頂点に持ち越す情報の処理はここ，再帰じゃないのでnxtにcurを使用した情報を，curにいる間に渡さざるを得ないか

    print(*res)
    return


if __name__ == "__main__":
    main()
