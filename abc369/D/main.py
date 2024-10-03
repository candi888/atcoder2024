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
    a = list(map(int, input().split()))

    dp = [[0 for j in range(2)] for i in range(n)]

    # 初期条件 1が偶数回目に倒すとき
    dp[0][0] = a[0]
    dp[0][1] = 0

    for i in range(n - 1):
        x = a[i + 1]
        # dp[i + 1][1] = max(dp[i][0] + 2 * x, dp[i][1])
        # dp[i + 1][0] = max(dp[i][1] + x, dp[i][0])

        for is_even in range(2):
            dp[i + 1][is_even] = max(
                dp[i][is_even], dp[i][~is_even] + (1 << is_even) * x
            )

    print(max(dp[n - 1]))
    return


if __name__ == "__main__":
    main()
