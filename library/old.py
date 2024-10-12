inf, mod9, mod10 = 1 << 60, 998244353, 1000000007
from collections import Counter, defaultdict, deque
from itertools import accumulate
from sys import setrecursionlimit, stdin, stdout

input = lambda: stdin.readline().strip()
setrecursionlimit(700000)
from bisect import bisect_left
from heapq import heapify, heappop, heappush

lis = []


#! 辞書順最小問題


def nexlist(
    s,
):  # i文字目以降でjが登場する最小のidx、存在しなければn（配列の一つ外）を返す
    n = len(s)

    res = [[n for j in range(26)] for i in range(n + 1)]

    for i in reversed(range(n)):
        for j in range(26):
            res[i][j] = res[i + 1][j]  # 一旦i+1番目を答えとしておく

        res[i][ord(s[i]) - 97] = i  # i文字目の情報を反映

    return res


n, k = map(int, input().split())
s = input()

nex = nexlist(s)

ans = []
now = -1
for i in range(k):  # 長さkの辞書順最小の部分列を前から順番に決める
    for j in range(26):  # a,b,c...と貪欲に確認
        idx = nex[now + 1][j]  # 既に決まった文字のidx以降を確認すればよい

        if idx + k - 1 - i < n:  # 長さkの部分列が構成できるか？（後ろにはみ出さないか）
            ans.append(s[idx])
            now = idx
            break

print("".join(ans))

#! 最長増加部分列
N = int
dp = [inf] * N
A = []
for a in A:
    idx = bisect_left(dp, a)
    dp[idx] = a

#! 累乗根を誤差なく求める
"不等式の形にして指数をいじって考える"
"誤差でintがズレるのは大体10**15くらいらしいので、制約を見て判断する"


# 1 基本これでよさそう
def calc_sqrt(x):
    sq = int(x ** (0.5))
    if sq**2 > x:
        sq -= 1
    if (sq + 1) ** 2 <= x:
        sq += 1
    return sq


# 2　にぶたんを使う　もし上でおかしくなったらこれの方が確実なので切り替える
def check(mid, x):
    if mid**2 <= x:
        return 1
    else:
        0


def binary_search(x):
    left, right = 0, 10**10
    while right - left > 1:
        mid = (left + right) // 2

        if check(mid, x):
            left = mid
        else:
            right = mid
    return left
