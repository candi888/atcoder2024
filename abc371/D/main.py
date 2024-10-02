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
    x = list(map(int, input().split()))
    p = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for i in range(q)]

    acc_p = [0] + list(accumulate(p))

    for li, ri in query:
        lidx = bisect_left(x, li)
        ridx = bisect_right(x, ri)

        print(acc_p[ridx] - acc_p[lidx])
    return


if __name__ == "__main__":
    main()
