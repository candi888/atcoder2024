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
    s_input = input()
    s_list = list(s_input)

    dp = [[-INF] * 3 for i in range(n + 1)]

    # init
    dp[0] = [0] * 3

    hand_to_index = {hand: i for i, hand in enumerate(["R", "S", "P"])}

    for i in range(n):
        si = s_list[i]

        if si !="P": 
            dp[i + 1][hand_to_index["R"]] = max(
                dp[i][hand_to_index["S"]] + (si == "S"),
                dp[i][hand_to_index["P"]] + (si == "S"),
            )
        if si != "R":
            dp[i + 1][hand_to_index["S"]] = max(
                dp[i][hand_to_index["R"]] + (si == "P"),
                dp[i][hand_to_index["P"]] + (si == "P"),
            )
        if si !="S":
            dp[i + 1][hand_to_index["P"]] = max(
                dp[i][hand_to_index["R"]] + (si == "R"),
                dp[i][hand_to_index["S"]] + (si == "R"),
            )

    print(max(dp[-1]))
    return


if __name__ == "__main__":
    main()
