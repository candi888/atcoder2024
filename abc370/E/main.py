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
"""
sortedmultiset，累積和で各左端について和がKになる連続部分列がなんこあるかはいけそう
累積和の要素と元配列の要素を対応づける？これでidxもわかるか？
補集合を考えて数え上げか2^nのMODINT？
"""


def main() -> None:
    return


if __name__ == "__main__":
    main()