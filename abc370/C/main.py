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
    s = input()
    t = input()

    len_s = len(s)

    diff_num = 0
    for i in range(len_s):
        si = s[i]
        ti = t[i]
        if si != ti:
            diff_num += 1

    print(diff_num)
    cur_s = s[:]
    for cur_change in range(diff_num):
        check_lis = [
            "".join(cur_s[:i] + t[i] + cur_s[i + 1 :])
            for i in range(len_s)
            if cur_s[i] != t[i]
        ]

        cur_s = min(check_lis)
        print(cur_s)

    return


if __name__ == "__main__":
    main()
