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
