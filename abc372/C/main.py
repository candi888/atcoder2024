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


def count_part_str(left_index, step, original_list_s):
    res = 0
    for left in range(left_index, left_index + step):
        if "".join(original_list_s[left : left + 3]) == "ABC":
            res += 1

    # print(original_list_s)
    # print(res)
    return res


def main() -> None:
    n, q = list(map(int, input().split()))
    s = input()
    query = [list(input().split()) for i in range(q)]

    cur_res = s.count("ABC")

    list_s = list(s)
    for i, (xi, ci) in enumerate(query):
        xi = int(xi) - 1  # xiは0-index

        left = max(0, xi - 2)
        right = min(len(list_s) - 1, xi + 2)
        step = right - left

        ori_cnt = count_part_str(left_index=left, step=step, original_list_s=list_s)
        list_s[xi] = ci
        cur_cnt = count_part_str(left_index=left, step=step, original_list_s=list_s)

        cur_res += cur_cnt - ori_cnt

        print(cur_res)

    return


if __name__ == "__main__":
    main()
