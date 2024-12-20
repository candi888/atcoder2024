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
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))

    acc_a = list(accumulate([0] + a + a))
    rem = [ai % m for ai in acc_a]

    counter = Counter(rem[:n])

    res = 0
    for left in range(n):
        right = left + n

        res += counter[rem[left]] - 1

        counter[rem[left]] -= 1
        counter[rem[right]] += 1

    print(res)

    return


if __name__ == "__main__":
    main()
