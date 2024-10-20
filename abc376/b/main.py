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
    n, q = list(map(int, input().split()))
    query = [input().split() for i in range(q)]

    cur_left, cur_right = 0, 1

    res = 0
    for hi, ti in query:
        ti = int(ti) - 1

        if hi == "R":
            if cur_right < ti:
                if cur_right < cur_left < ti:
                    res += cur_right + n - ti
                else:
                    res += abs(ti - cur_right)
            else:
                if ti < cur_left < cur_right:
                    res += ti + n - cur_right
                else:
                    res += abs(ti - cur_right)

            cur_right = ti

        else:
            if cur_left < ti:
                if cur_left < cur_right < ti:
                    res += cur_left + n - ti
                else:
                    res += abs(ti - cur_left)
            else:
                if ti < cur_right < cur_left:
                    res += ti + n - cur_left
                else:
                    res += abs(ti - cur_left)
            
            cur_left = ti
    
    print(res)


    return


if __name__ == "__main__":
    main()
