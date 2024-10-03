from collections import deque
from typing import List


def syakutori(
    input_list: List,
) -> None:
    """尺取り法をする．
    見ている区間が短いときにTrue, 長くなるとどこかでFalseになるパターンのものが対象．
    ↑の逆の場合はis_shrink_leftの判定の補集合を考えればよさそう？

    Args:
        input_list (List): 尺取り法で走査対象のリスト．
    """

    def is_shrink_left() -> bool:
        """左端を縮めるかの判定を行う．

        Returns:
            bool: 左端を縮めるか
        """
        return False

    que: deque = deque()
    for right_idx, (right_value) in enumerate(input_list):
        que.append(right_value)

        # TODO 処理を記述．右端を伸ばしたあと

        while que and (not is_shrink_left()):
            left_value = que.popleft()
            # left_idx = right_idx - len(que)

            # TODO 処理を記述．左端を縮めたあと

        # TODO 処理を記述．今のdequeは任意の右端に対して条件を満たす最長の連続部分列となっている

    return
