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
    k = int(input())

    def Prime_Factorize(n):  # [2,2,2,3,3...] O(√N)
        p = []
        while n % 2 == 0:
            p.append(2)
            n //= 2
        f = 3
        while f**2 <= n:
            if n % f == 0:
                p.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            p.append(n)
        return p

    prime_to_pownum = Counter(Prime_Factorize(k))

    prime_to_contain = Counter()
    for prime, pownum in prime_to_pownum.items():
        prime_to_contain[prime] = sum([i // prime for i in range(1, pownum + 1)])

    print(prime_to_contain)
    print(max([p * prime_to_contain[p] for p, pownum in prime_to_pownum.items()]))

    return


if __name__ == "__main__":
    main()
