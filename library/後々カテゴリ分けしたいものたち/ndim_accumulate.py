import operator
from functools import reduce


def n_dim_cumsum(arr):
    """
    N次元配列の累積和を計算します。累積和配列の各軸の先頭に0を追加します。

    Parameters:
    arr (list): 入力のN次元配列（ネストされたリスト）。

    Returns:
    list: 各軸に0を追加したN次元累積和配列。
    """
    import itertools

    # 配列の形状を取得
    def get_shape(arr):
        shape = []
        while isinstance(arr, list):
            shape.append(len(arr))
            if len(arr) == 0:
                break
            arr = arr[0]
        return shape

    shape = get_shape(arr)

    # 0で初期化した配列を作成
    def zeros_plus_one(shape):
        if len(shape) == 0:
            return 0
        else:
            return [zeros_plus_one(shape[1:]) for _ in range(shape[0] + 1)]

    csum = zeros_plus_one(shape)

    # 値の取得と設定の関数
    def get_value(arr, idx):
        for i in idx:
            arr = arr[i]
        return arr

    def set_value(arr, idx, value):
        for i in idx[:-1]:
            arr = arr[i]
        arr[idx[-1]] = value

    # 入力配列の値を累積和配列にコピー（インデックスを+1）
    indices = itertools.product(*(range(dim) for dim in shape))
    for idx in indices:
        idx_plus_one = [i + 1 for i in idx]
        value = get_value(arr, idx)
        set_value(csum, idx_plus_one, value)

    # 各次元に沿って累積和を計算
    csum_shape = [dim + 1 for dim in shape]
    for d in range(len(shape)):
        csum_indices = itertools.product(*(range(dim) for dim in csum_shape))
        for idx in csum_indices:
            if idx[d] >= 1:
                temp_idx = list(idx)
                temp_idx[d] -= 1
                csum_value = get_value(csum, idx)
                temp_csum_value = get_value(csum, temp_idx)
                set_value(csum, idx, csum_value + temp_csum_value)

    return csum


def calc_part_of_accmulate_ndim(acc_ndim_list_prefix_zero, left_right_list, bits):
    """
    N次元累積和を使って指定ブロックの総和を計算するときの各項を計算する

    Args:
        acc_ndim_list_prefix_zero (List): N次元の累積和を計算したList．各軸の最初に0が入っていることを前提にする．
        left_right_list (List[tuple(int, int)]): 指定ブロックの端点のインデックス(li, ri)(1-index)を格納する．ゆえにndim * 2個の要素を持つ．
        bits (List[bool]): ndim次元の1次元配列で，i次元目でli, riどちらの端点を使用して値を算出するかの情報を示す．

    Returns:
        int : 指定ブロックの総和を計算するときの各項
    """
    return pow(-1, (sum(bits) % 2) ^ 1) * reduce(
        operator.getitem,
        [ri if bits[idx] else li - 1 for idx, (li, ri) in enumerate(left_right_list)],
        acc_ndim_list_prefix_zero,
    )


# TODO 使用例

# acc_a = n_dim_cumsum(arr=a)

# ndim = 3
# for queryi in query:
#     assert 2 * ndim == len(queryi)

#     left_right_list = [(queryi[2 * i], queryi[2 * i + 1]) for i in range(ndim)]

#     cur_sum = 0
#     for bits in product([0, 1], repeat=ndim):
#         cur_sum += calc_part_of_accmulate_ndim(
#             acc_ndim_list_prefix_zero=acc_a,
#             left_right_list=left_right_list,
#             bits=bits,
#         )

#     print(cur_sum)
