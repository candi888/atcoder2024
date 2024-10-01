from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import accumulate, product
from sys import setrecursionlimit, stdin


def input() -> str:
    return stdin.readline().strip()


setrecursionlimit(700000)
# import pypyjit;pypyjit.set_param('max_unroll_recursion=-1')

INF = (1 << 61) - 1
MOD9, MOD10 = 998244353, 1000000007
"------------------------------------------------------------------------------"


def main() -> None:
    s_ab, s_ac, s_bc = list(input().split())

    if (s_ab == "<" and s_ac == ">") or (s_ab == ">" and s_ac == "<"):
        print("A")
    elif (s_ab == "<" and s_bc == "<") or (s_ab == ">" and s_bc == ">"):
        print("B")
    else:
        print("C")

    return


if __name__ == "__main__":
    main()
