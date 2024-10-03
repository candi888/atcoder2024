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


def is_tosa(cur_right_val, nxt_right_val, step):
    return step == nxt_right_val - cur_right_val


def main() -> None:
    n = int(input())
    lis = list(map(int, input().split()))

    def check(cur_que, cur_step):
        if len(cur_que) <= 2:
            return True
        else:
            return is_tosa(
                cur_right_val=cur_que[-2], nxt_right_val=cur_que[-1], step=cur_step
            )

    cur_step = INF
    res = 1
    que = deque([lis[0]])

    for r in lis[1:]:
        que.append(r)

        # 左端を縮めた時に行う処理

        while que and (
            not check(cur_que=que, cur_step=cur_step)
        ):  # 要は条件を満たさない時
            l = que.popleft()
            # 左端を縮めた時に行う処理

        cur_step = que[-1] - que[-2]

        # なんかの処理。
        # 今のdequeは任意の右端に対して条件を満たす最長の連続部分列となっているのでそれを活かす
        res += len(que)

        # 短いとout,長いとokの場合は？
        # 判定条件から補

    print(res)
    return


if __name__ == "__main__":
    main()
