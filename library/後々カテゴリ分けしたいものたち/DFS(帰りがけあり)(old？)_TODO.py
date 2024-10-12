import sys

input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(700000)
inf, mod9, mod10 = 1 << 60, 998244353, 1000000007
from collections import Counter, defaultdict, deque
from itertools import accumulate

#! Stack DFS（行きがけ、帰りがけ両方）
edge = []
seen = []

# ここから見よ

stack = [(0, 0, 1, 0, 0), (1, 1, 0, 0, 0)]
# 1-index で管理、初期化は架空の頂点0を考えて根からもう一つ上に伸びているイメージ
# 初期化の際のprvは使うことはないので取り得ない値を勝手に設定しておｋ（memo配列と都合がいいように）
while stack:
    # (Go or Back,今いる頂点番号,一つ前の頂点番号,(今居る頂点に持っていきたい情報))（行きがけだけならprvは不要）
    f, cur, prv, curw, prvw = stack.pop()

    if f:
        # ここに今いる頂点に入った時にやりたい処理（インクリメント）
        pass

        for nxt, nxtw in edge[cur]:  # ここは基本このまま写せばおｋ
            if not seen[nxt]:  # メモのチェックに当たる部分
                seen[nxt] = 1
                stack.append((0, cur, nxt, curw, nxtw))
                stack.append((1, nxt, cur, nxtw, curw))

    else:
        # この時は、prvが出ていく頂点番号、curが戻り先の頂点番号を表す。prv→cur cur→nxtという対応関係
        # （↑を意識した上で）ここに今いる頂点を離れる時にやりたい処理（デクリメント）
        pass

# メモ化再帰の場合は↓'

n = int(input())
a = list(map(int, input().split()))
d = Counter(a)


def idx(i, j, k):
    return i * (n + 2) ** 2 + j * (n + 2) + k


memo = [-1] * (n + 2) ** 3
memo[0] = 0
tmp = [0] * (n + 2) ** 3  # stackDFSでは遷移でもらう値をtmp配列に記憶していく


def dfs():
    stack = [
        (0, 0, n + 1, n + 1, n + 1, d[1], d[2], d[3]),
        (1, 0, d[1], d[2], d[3], n + 1, n + 1, n + 1),
    ]
    while stack:
        f, edge, ci, cj, ck, pi, pj, pk = stack.pop()
        wa = ci + cj + ck

        if f:
            if ci > 0:
                ni, nj, nk = (
                    ci - 1,
                    cj,
                    ck,
                )  # メモがあるならそれを使う、そうでなければ潜る
                if memo[idx(ni, nj, nk)] != -1:
                    tmp[idx(ci, cj, ck)] += memo[idx(ni, nj, nk)] * ci / wa
                # 本来帰りがけでtmpに保存するところを、メモがあるならここで処理してしまう。潜る必要がなくなる。
                else:
                    stack.append((0, 0, ci, cj, ck, ni, nj, nk))
                    stack.append((1, 0, ni, nj, nk, ci, cj, ck))
            if cj > 0:
                ni, nj, nk = ci + 1, cj - 1, ck
                if memo[idx(ni, nj, nk)] != -1:
                    tmp[idx(ci, cj, ck)] += memo[idx(ni, nj, nk)] * cj / wa
                else:
                    stack.append((0, 1, ci, cj, ck, ni, nj, nk))
                    stack.append((1, 1, ni, nj, nk, ci, cj, ck))
            if ck > 0:
                ni, nj, nk = ci, cj + 1, ck - 1
                if memo[idx(ni, nj, nk)] != -1:
                    tmp[idx(ci, cj, ck)] += memo[idx(ni, nj, nk)] * ck / wa
                else:
                    stack.append((0, 2, ci, cj, ck, ni, nj, nk))
                    stack.append((1, 2, ni, nj, nk, ci, cj, ck))

        else:
            # その頂点を離れるときdpの値が確定する。
            cur = (ci, cj, ck)
            memo[idx(pi, pj, pk)] = tmp[idx(pi, pj, pk)] + n / (pi + pj + pk)
            tmp[idx(ci, cj, ck)] += (
                memo[idx(pi, pj, pk)] * cur[edge] / wa
            )  # 遷移式で使う材料をtmp配列に記憶
