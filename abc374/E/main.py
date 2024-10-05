"""
------------------------------------------------------------------------------
AtCoder用テンプレート
"""

import math
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

buffer = 120000


def main() -> None:
    n, x = list(map(int, input().split()))
    input_query = [list(map(int, input().split())) for i in range(n)]

    product1 = [(ai, pi) for (ai, pi, bi, qi) in input_query]
    product2 = [(bi, qi) for (ai, pi, bi, qi) in input_query]

    def check(cur_w):
        all_cost = 0
        for cur_product in range(n):
            ai, pi = product1[cur_product]
            bi, qi = product2[cur_product]
            if pi / ai < qi / bi:
                use_num_max = math.ceil(cur_w / ai)
                cur_cost = use_num_max * pi
                for i, use_num_a in enumerate(range(use_num_max)[::-1]):
                    use_num_b = math.ceil((cur_w - use_num_a * ai) / bi)

                    tmp_produce = use_num_a * ai + use_num_b * bi
                    assert tmp_produce >= cur_w

                    tmp_cost = use_num_a * pi + use_num_b * qi
                    if tmp_cost < cur_cost:
                        cur_cost = tmp_cost
                    elif use_num_max - i <= buffer:
                        continue
                    else:
                        break

            elif abs(pi / ai - qi / bi) > 1e-6:
                use_num_max = math.ceil(cur_w / bi)
                cur_cost = use_num_max * qi

                for i, use_num_b in enumerate(range(use_num_max)[::-1]):
                    use_num_a = math.ceil((cur_w - use_num_b * bi) / ai)

                    tmp_produce = use_num_a * ai + use_num_b * bi
                    assert tmp_produce >= cur_w

                    tmp_cost = use_num_a * pi + use_num_b * qi
                    if tmp_cost < cur_cost:
                        cur_cost = tmp_cost

                    elif use_num_max - i <= buffer:
                        continue
                    else:
                        break
            else:
                if ai <= bi:
                    use_num_max = math.ceil(cur_w / ai)
                    cur_cost = use_num_max * pi
                    for i, use_num_a in enumerate(range(use_num_max)[::-1]):
                        use_num_b = math.ceil((cur_w - use_num_a * ai) / bi)

                        tmp_produce = use_num_a * ai + use_num_b * bi
                        assert tmp_produce >= cur_w

                        tmp_cost = use_num_a * pi + use_num_b * qi
                        if tmp_cost < cur_cost:
                            cur_cost = tmp_cost
                        elif use_num_max - i <= buffer:
                            continue
                        else:
                            break
                else:
                    use_num_max = math.ceil(cur_w / bi)
                    cur_cost = use_num_max * qi

                    for i, use_num_b in enumerate(range(use_num_max)[::-1]):
                        use_num_a = math.ceil((cur_w - use_num_b * bi) / ai)

                        tmp_produce = use_num_a * ai + use_num_b * bi
                        assert tmp_produce >= cur_w

                        tmp_cost = use_num_a * pi + use_num_b * qi
                        if tmp_cost < cur_cost:
                            cur_cost = tmp_cost

                        elif use_num_max - i <= buffer:
                            continue
                        else:
                            break

            all_cost += cur_cost

        return all_cost <= x

    def binary_search() -> int:
        left, right = 0, INF
        while right - left > 1:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid

        return left

    print(binary_search())

    return


if __name__ == "__main__":
    main()
