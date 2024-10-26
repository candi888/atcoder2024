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

    if n == 1:
        print(0)
        exit()

    n -= 1

    res_len = 0
    cur_check = 0
    for i in range(10**7):
        res_len += 1

        cur_increment = 9 * pow(10, i)
        if n <= cur_check + cur_increment:
            break
        cur_check += cur_increment

        res_len += 1

        if n <= cur_check + cur_increment:
            break
        cur_check += cur_increment

    res_list = [-INF] * res_len

    check_n_str = f"{n - cur_check:0{math.ceil(res_len / 2)}}"
    print(check_n_str)
    for i in range(math.ceil(res_len / 2)):
        cur_res = int(check_n_str[i])
        if i == 0:
            res_list[i] = str(cur_res + 1)
            res_list[-i - 1] = str(cur_res + 1)
        else:
            res_list[i] = str(cur_res - 1)
            res_list[-i - 1] = str(cur_res - 1)

    print("".join(res_list))

    return


if __name__ == "__main__":
    main()
