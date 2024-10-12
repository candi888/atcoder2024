import operator
from functools import reduce

# ネストされたリスト
nested_list = [[[19, 29], [93, 94]], [[95, 96], [97, 98]]]

# インデックスのリスト
indices = [0, 1, 1]

# 要素にアクセス
value = reduce(operator.getitem, indices, nested_list)

print(value)  # 出力: 4
