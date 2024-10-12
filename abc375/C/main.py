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
    n = int(input())
    grid_input = [list(input()) for i in range(n)]

    #  1-index
    def rotate(rotate_num, sx, sy):
        rem_rotate = rotate_num % 4
        resx, resy = -INF, -INF
        if rem_rotate == 1:
            resx = sy
            resy = n + 1 - sx

        elif rem_rotate == 2:
            resx = n + 1 - sx
            resy = n + 1 - sy

        elif rem_rotate == 3:
            resx = n + 1 - sy
            resy = sx
        else:
            resx = sx
            resy = sy

        return resx, resy

    grid_res = [[-INF] * n for i in range(n)]

    for rotate_num in range(1, n // 2 + 1):
        gy = rotate_num - 1
        for gx in range(rotate_num - 1, n - rotate_num):
            nx, ny = rotate(rotate_num, gx + 1, gy + 1)
            grid_res[nx - 1][ny - 1] = grid_input[gx][gy]
        gx = n - rotate_num
        for gy in range(rotate_num - 1, n - rotate_num):
            nx, ny = rotate(rotate_num, gx + 1, gy + 1)
            grid_res[nx - 1][ny - 1] = grid_input[gx][gy]
        gy = n - rotate_num
        for gx in range(rotate_num, n - rotate_num + 1):
            nx, ny = rotate(rotate_num, gx + 1, gy + 1)
            grid_res[nx - 1][ny - 1] = grid_input[gx][gy]
        gx = rotate_num - 1
        for gy in range(rotate_num, n - rotate_num + 1):
            nx, ny = rotate(rotate_num, gx + 1, gy + 1)
            grid_res[nx - 1][ny - 1] = grid_input[gx][gy]

    # res
    for i in range(n):
        print("".join(grid_res[i]))

    return


if __name__ == "__main__":
    main()
