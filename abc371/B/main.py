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
    n, m = list(map(int, input().split()))
    query = [list(input().split()) for i in range(m)]

    already_set = set()
    for ai, bi in query:
        ai = int(ai)
        if ai not in already_set and bi == "M":
            print("Yes")
            already_set.add(ai)
        else:
            print("No")

    return


if __name__ == "__main__":
    main()
