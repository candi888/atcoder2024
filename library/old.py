inf, mod9, mod10 = 1 << 60, 998244353, 1000000007
from collections import Counter, defaultdict, deque
from itertools import accumulate
from sys import setrecursionlimit, stdin, stdout

input = lambda: stdin.readline().strip()
setrecursionlimit(700000)
from bisect import bisect_left
from heapq import heapify, heappop, heappush

lis = []


#! ダブリング、周期性を見出す

"""
K回同じ操作をした後の状態を知りたい（kがクソデカ整数）の場合に、o(k)をo(log(k))に落とせる。
Dv[i][j]→jに2^i回操作したら何に飛んでいくか
"""
n, k = map(int, input().split())  # kが操作の繰り返し回数
a = list(map(int, input().split()))

dv = [[0 for j in range(n)] for i in range(100)]
for j in range(n):
    dv[0][j] = a[j] - 1  # 一回操作をしたらjは何に飛んでいくかの定義。Rangeはピッタリに
for i in range(99):  # log(k)でおｋ
    for j in range(n):  # 最初のスタートがj
        dv[i + 1][j] = dv[i][dv[i][j]]  # iのテーブルで2^i回動かしてから2^i回動かす
ansl = []
for i in range(100):
    if k >> i & 1:
        ansl.append(i)
now = 0  # 開始地点
for i in ansl:
    now = dv[i][now]  # 1が立っているiについて2^i回を足し合わせれば答え

"""
もしくは周期性を見出してみる
"""
rem = k
ans = 0

first = [-1 for i in range(n)]  # いつ発見したか
first[0] = 0
for i in range(1, 10**8):  # 最初から二ループ目に入るまで
    ans += a[ans % n]
    rem -= 1
    if first[ans % n] == -1:
        first[ans % n] = i
    else:
        t = i - first[ans % n]
        break

    if rem == 0:
        print(ans)
        exit()

while (
    rem % t != 0
):  # 余り部分を先に処理　スコアの総和ではなく最大値を求めたいときなどは下を見よ
    rem -= 1
    ans += a[ans % n]

if rem == 0:
    print(ans)
    exit()

tsum = 0
for i in range(t):  # ループ部分を最後に
    rem -= 1
    tsum += a[ans % n]
    ans += a[ans % n]
ans += tsum * (rem // t)

print(ans)

# 任意回数の操作でスコアを最大化したいときなどは、
# （スタート～最初のループが終わるまで）、
# （最初のループが終わってから最後ー１回目のループが終わるまでの総スコア）＋（最後のループの始まりから余り含めてその終わりまで）
# これらのパターンを考える必要がある
# 最後-1回目に入ったらシミュレーションでよさそう

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

import sys

input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(700000)
inf, mod9, mod10 = 1 << 60, 998244353, 1000000007
from collections import Counter, defaultdict, deque
from itertools import accumulate

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


#! ワーシャルフロイド
# dp[i][j]はedgeのコストで初期化、なければinf
dp = [[]]
for k in range(10):
    for i in range(10):
        for j in range(10):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

"""
/辺の追加による最短距離の更新はワーシャルフロイドでできる！！
制約条件によって、全頂点間の最短経路は一旦ダイクストラで求める→辺の追加はワーシャルフロイドでやるなどの組み合わせも可能

・追加(a→bへのコストがcの辺) 一回当たりO(N**2)
for i in range(n):
    for j in range(n):
        dp[i][j]=min(dp[i][j],dp[i][a]+dp[b][j]+c)
（任意の二頂点について、min(辺の追加前の最短経路長,追加された辺を経由した時の経路長)を取ればよい！）


（以下はその辺を削除した時の影響を考えている）

まず、任意の二頂点対のうち最短経路が変わるものがあるか？は、a→bの最短経路長が変わるか否かだけを考えればよい
（a→bが変わらなければそれを経由した最短経路長も変わらない。経由しない最短経路長ももちろん変わらない）

check=min([dp[a][i]+dp[i][b] for i in range(n)],edge[a][b]のc以外) 
（check:=他の頂点を経由してaからbへ行く際の最短経路とa→bへの他の辺のmin。つまりc以外の最短経路の候補の全列挙
ここでc以下のものがあればそっちを使えばいいのでこの辺は削除しても全頂点対の最短経路には影響しない。
ここでcheck>cとなるならば、a→bへ行く際の最短経路に削除する辺を使っているということ）

（ワーシャルフロイドのdp[i][i]は、遷移式から分かるように0より大きくなる。（他の頂点に余計に行って戻るor自己ループ）
つまりdp[a][b]+dp[b][b]とは確実に余計な移動をしているものなのでdp[a][b]そのものにはなり得ない）

・辺の削除はクエリ逆読みで削除する辺を順番に追加していくという方針でやる？

"""

#!'トポロジカルソート（辞書順最小にするver）

n, m = map(int, input().split())

incnt = [0 for i in range(n)]  # 各ノードの入次数
edge = [[] for i in range(n)]  # 有向グラフ、入る先のノードを管理
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    incnt[b] += 1
    edge[a].append(b)

res = []  # トポロジカルソート後の配列
l = [
    i for i in range(n) if incnt[i] == 0
]  # 何も入ってこない（どこにあろうが自由）ノードで初期化
heapify(l)
while l:
    now = heappop(l)
    res.append(now)  # 何も入ってこないノードを順番に入れていく
    for nxt in edge[now]:
        incnt[nxt] -= 1
        if incnt[nxt] == 0:  # もう何も入ってこないならば候補に入れる
            heappush(l, nxt)

#!　強連結成分分解

n, m = list(map(int, input().split()))

edge = [[] for i in range(n)]
revedge = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    edge[a].append(b)
    revedge[b].append(a)

seen = [0 for i in range(n)]
num = [-1 for i in range(n)]
cnt = 0


def dfs(cur, edge):
    global cnt

    seen[cur] = 1

    for nxt in edge[cur]:
        if not seen[nxt]:
            dfs(nxt, edge)

    num[cur] = cnt
    cnt += 1
    return cnt


for i in range(n):
    if num[i] == -1:
        dfs(i, edge)

dic = {num[i]: i for i in range(n)}
seen = [0 for i in range(n)]
groupsize = []

for i in reversed(range(n)):
    if not seen[dic[i]]:
        cnt = 0
        groupsize.append(dfs(dic[i], revedge))

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


n, m = list(map(int, input().split()))

edge = [[] for i in range(n)]
revedge = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    edge[a].append(b)
    revedge[b].append(a)

seen = [0 for i in range(n)]
num = [-1 for i in range(n)]
cnt = 0


def dfs(cur, edge):
    global cnt

    seen[cur] = 1

    for nxt in edge[cur]:
        if not seen[nxt]:
            dfs(nxt, edge)

    num[cur] = cnt
    cnt += 1
    return cnt


for i in range(n):
    if num[i] == -1:
        dfs(i, edge)

dic = {num[i]: i for i in range(n)}
seen = [0 for i in range(n)]
groupsize = []

for i in reversed(range(n)):
    if not seen[dic[i]]:
        cnt = 0
        groupsize.append(dfs(dic[i], revedge))
