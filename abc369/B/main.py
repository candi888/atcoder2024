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
    n = int(input())
    query = [input().split() for i in range(n)]

    left_list = [int(ai) for (ai, si) in query if si == "L"]
    right_list = [int(ai) for (ai, si) in query if si == "R"]

    res = 0

    for i in range(1, len(left_list)):
        res += abs(left_list[i] - left_list[i - 1])
    for i in range(1, len(right_list)):
        res += abs(right_list[i] - right_list[i - 1])

    print(res)
    return


if __name__ == "__main__":
    main()
