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

import numpy as np


def main() -> None:
    m = int(input())

    tmp = np.base_repr(m, 3)

    ans = []
    for idx, i in enumerate(list(tmp)[::-1]):
        cur = int(i)
        if cur == 0:
            continue

        for j in range(cur):
            ans.append(idx)

    print(len(ans))
    print(*ans)

    return


if __name__ == "__main__":
    main()
