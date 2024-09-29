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
    s_list = list(input())

    cur_i = s_list.index("A")
    res = 0
    for i in range(1, 26):
        next_i = s_list.index(chr(ord("A") + i))
        res += abs(next_i - cur_i)

        cur_i = next_i

    print(res)

    return


if __name__ == "__main__":
    main()
