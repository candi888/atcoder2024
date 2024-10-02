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
    n = int(input())
    mg = int(input())

    edges_mg = [list(map(int, input().split())) for i in range(mg)]

    mh = int(input())
    edges_mh = [list(map(int, input().split())) for i in range(mh)]

    a = [list(map(int, input().split())) for i in range(n - 1)]

    set_edges_mg = set([tuple([u - 1, v - 1]) for (u, v) in edges_mg]) | set(
        [tuple([v - 1, u - 1]) for (u, v) in edges_mg]
    )
    set_edges_mh = set([tuple([u - 1, v - 1]) for (u, v) in edges_mh]) | set(
        [tuple([v - 1, u - 1]) for (u, v) in edges_mh]
    )

    res = INF
    for p_tuple in permutations(list(range(n)), n):
        cur_res = 0
        for curj in range(n):
            for curi in range(n):
                p_i = p_tuple[curi]
                p_j = p_tuple[curj]

                if ((curi, curj) in set_edges_mg) != ((p_i, p_j) in set_edges_mh):
                    cur_max = max(p_i, p_j)
                    cur_min = min(p_i, p_j)

                    cur_res += a[cur_min][cur_max - cur_min - 1]

        if cur_res < res:
            res = cur_res

    if cur_res % 2 != 0:
        raise RuntimeError

    print(res // 2)

    return


if __name__ == "__main__":
    main()
