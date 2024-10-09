from heapq import heappop, heappush
from typing import List

INF = (1 << 61) - 1


def dijkstra(edge: List[tuple], start_node: int) -> List:
    """ダイクストラ法によって，始点からすべての頂点までの最短距離を０(ElogV)で算定する．

    Args:
        edge (List[tuple]): 各頂点から出る辺の情報をもつ．[[行先のノード番号，辺のコスト] ,...]
        start_node (int): 始点のノード番号

    Returns:
        mindist_from_start_node (List): 始点から各ノードへの最短距離を格納したリスト
    """
    # 全頂点数
    node_num = len(edge)

    # 最短経路長を管理。infで初期化
    mindist_from_start_node = [INF for i in range(node_num)]
    mindist_from_start_node[start_node] = 0

    # 最短距離確定済みの頂点
    confirmed = [False for i in range(node_num)]

    # heapq用の配列
    heap: List = []
    # [頂点の暫定値，頂点番号]を格納していく
    heappush(heap, [0, start_node])

    while heap:
        _, cur = heappop(heap)

        # 確定済みだったら飛ばす
        if confirmed[cur]:
            continue

        # その時点での最短経路長の頂点を確定
        confirmed[cur] = True

        for nxt, cost in edge[cur]:
            if mindist_from_start_node[cur] + cost < mindist_from_start_node[nxt]:
                mindist_from_start_node[nxt] = mindist_from_start_node[cur] + cost
                heappush(heap, [mindist_from_start_node[nxt], nxt])

    return mindist_from_start_node
