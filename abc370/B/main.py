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


def main() -> None:
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]

    cur = a[0][0]

    for i in range(1, n):
        cur = a[max(cur - 1, i)][min(cur - 1, i)]

    print(cur)

    return


if __name__ == "__main__":
    main()
