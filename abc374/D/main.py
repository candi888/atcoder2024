"""
------------------------------------------------------------------------------
AtCoder用テンプレート
"""

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, product
from sys import setrecursionlimit, stdin
from typing import Dict, List, Set


def input() -> str:
    return stdin.readline().strip()


setrecursionlimit(700000)
# import pypyjit;pypyjit.set_param('max_unroll_recursion=-1')

INF = (1 << 61) - 1
MOD9, MOD10 = 998244353, 1000000007
"------------------------------------------------------------------------------"


def calc_dist(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5


def main() -> None:
    n, s, t = map(int, input().split())
    line_coordinates = [list(map(int, input().split())) for _ in range(n)]

    res = INF
    for order in permutations(range(n)):
        for bool_inside in product([0, 1], repeat=n):
            cur_time = 0
            cx, cy = 0, 0
            # 全探索
            for cur in range(n):
                in_from_ab = bool_inside[cur]
                cur_line = order[cur]

                ai, bi, ci, di = line_coordinates[cur_line]

                if in_from_ab:
                    # 橋に移動
                    cur_time += calc_dist(cx, cy, ai, bi) / s
                    # 線描が
                    cur_time += calc_dist(ai, bi, ci, di) / t
                    cx, cy = ci, di
                else:
                    # 橋に移動
                    cur_time += calc_dist(cx, cy, ci, di) / s
                    # 線描が
                    cur_time += calc_dist(ci, di, ai, bi) / t
                    cx, cy = ai, bi

            res = min(res, cur_time)

    print(res)

    return


if __name__ == "__main__":
    main()
