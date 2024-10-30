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

    def eratosthenes(n):
        p = list(range(n + 1))

        for i in p[3:]:
            if p[i] % 2 == 0:
                p[i] = 0
        for i in range(3, n):
            if i**2 > n:
                break
            if p[i] != 0:
                for j in range(i, n + 1, 2):
                    if i * j > n:
                        break
                    p[i * j] = 0

        res = sorted(list(set(p)))[2:]
        return res

    prime_list = eratosthenes(10**6)

    res = 0
    len_prime_list = len(prime_list)

    print(len_prime_list)
    for i in range(len_prime_list):
        a = prime_list[i]
        cur_check = a**2

        if cur_check > n:
            break
        for j in range(i + 1, len_prime_list):
            b = prime_list[j]
            cur_check = a**2 * b
            if cur_check > n:
                break

            for k in range(j + 1, len_prime_list):
                c = prime_list[k]
                cur_check = a**2 * b * c**2

                if cur_check > n:
                    break
                res += 1

    return


if __name__ == "__main__":
    main()
