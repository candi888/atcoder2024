from heapq import heapify, heappop, heappush


def strongly_connected_component(n, edge, rev_edge):
    """
    連結成分に含まれる頂点番号を格納したSetを全て格納したListを返す．

    Args:
        n (int): 元のグラフの頂点数
        edge (List[List[int]]): 元のグラフの辺の情報．edge[i]は頂点iの行先の頂点番号を格納している
        rev_edge (List[List[int]]): edgeの辺の向きを全て逆にしたもの

    Returns:
        List[Set[int]]: 連結成分に含まれる頂点番号を格納したSetを全て格納したList
    """

    # * ---step1  帰りがけ順に番号付け---

    # これ[(元の頂点番号)] := SCCで使用する番号
    sccnum_list = [-1] * n
    # SCCで使用する番号を保持
    cur_cnt = 0
    # DFS用
    seen = [0] * n

    def dfs_step1_post_order_numbering(cur):
        """
        再帰DFSによって，元のグラフで帰りがけ順に頂点に番号付けを行う

        Args:
            cur (int): 今居る頂点の番号
        """
        nonlocal cur_cnt, seen, sccnum_list
        seen[cur] = 1

        for nxt in edge[cur]:
            if not seen[nxt]:
                seen[nxt] = 1
                dfs_step1_post_order_numbering(cur=nxt)

        # 帰りがけ順に番号付け
        sccnum_list[cur] = cur_cnt
        cur_cnt += 1

        return

    for i in range(n):
        if not seen[i]:
            dfs_step1_post_order_numbering(cur=i)
    # * -----------------------------

    # * ---step2  scc_numの大きいnodeから逆向きの辺でDFS---

    # 強連結成分の頂点集合を格納する
    sccset_list = []
    # これ[SCCで使用する番号] := (元の頂点番号)．要はscc_numの逆写像
    sccnum_to_originalnum = [-1] * n
    for i in range(n):
        sccnum_to_originalnum[sccnum_list[i]] = i
    # DFS用
    seen = [0] * n

    def dfs_step2_get_sccset_contains_root(root):
        """
        Stack DFSにより，rootから到達できる頂点を列挙し，それら（自身含む）を強連結成分としてSetとして返す

        Args:
            root (int): DFSを開始する頂点

        Returns:
            Set[int]: 強連結成分を格納したSet
        """
        nonlocal rev_edge, seen
        stack = [root]
        seen[root] = 1

        cur_sccset = set()

        while stack:
            cur = stack.pop()

            # curに来たときにやる処理
            cur_sccset.add(cur)

            for nxt in rev_edge[cur]:
                if not seen[nxt]:
                    seen[nxt] = 1
                    stack.append(nxt)

        return cur_sccset

    for i in range(n)[::-1]:
        cur_scc_num = sccnum_to_originalnum[i]
        if not seen[cur_scc_num]:
            sccset_list.append(dfs_step2_get_sccset_contains_root(root=cur_scc_num))
    # *----------------------------------------------

    return sccset_list


def get_topological_sorted_sccsetlist(sccset_list, original_branches):
    """
    連結成分に含まれる頂点番号を格納したSetを全て格納したListを受け取り，強連結成分をそれぞれ一つの潰したSCC頂点としてみなしてトポロジカルソートを行い，その結果を返す

    Args:
        sccset_list (List[Set[int]]): 連結成分に含まれる頂点番号を格納したSetを全て格納したList
        original_branches (List[List[int]]): 元のグラフの辺の情報．edge[i]は頂点iの行先の頂点番号を格納している

    Returns:
        List[Set[int]]: 強連結成分をそれぞれ一つの潰したSCC頂点としてみなしてトポロジカルソートを行った結果を格納したList
    """

    def topological_sort(n, edge):
        """
        頂点0～n-1をもつ，edgeで繋がれた有向連結グラフに対し，トポロジカルソートを行う．
        returnされるトポロジカルソート後のグラフは頂点番号の並びが辞書順最小のものである．

        Args:
            n (int): 頂点数
            edge (List[List[int]]): グラフの辺．edge[i]には頂点iの行先のnodeの番号が格納されている

        Returns:
            sorted_list (List[int]): トポロジカルソート後の頂点番号の配列
        """

        # 各ノードの入次数
        in_cnt = [0] * n
        for from_node in range(n):
            for to_node in edge[from_node]:
                in_cnt[to_node] += 1

        # 何も入ってこない（どこにあろうが自由）ノードで初期化
        node_incnt_zero = [i for i in range(n) if in_cnt[i] == 0]
        # 辞書順最小にするためにheapqを使う
        heapify(node_incnt_zero)

        sorted_list = []
        while node_incnt_zero:
            cur = heappop(node_incnt_zero)
            sorted_list.append(cur)

            for nxt in edge[cur]:
                in_cnt[nxt] -= 1

                # もう何も入ってこないならば候補に入れる
                if in_cnt[nxt] == 0:
                    heappush(node_incnt_zero, nxt)

        return sorted_list

    nodenum_original = len(original_branches)
    nodenum_sccnode = len(sccset_list)

    # これ[（元のグラフの頂点番号）] := SCC頂点番号
    nodenum_to_sccsetidx = [-1] * nodenum_original
    for sccsetidx, cur_sccset in enumerate(sccset_list):
        for nodenum in cur_sccset:
            nodenum_to_sccsetidx[nodenum] = sccsetidx

    # SCC頂点ごとをつなぐ辺の情報をもつ配列を作る．（辺の重複は無し）
    sccnode_branches = [[] for _ in range(nodenum_sccnode)]
    for from_node in range(nodenum_original):
        from_sccsetidx = nodenum_to_sccsetidx[from_node]

        # from_sccsetidxのSCC頂点から繋がっているSCC頂点番号を格納
        sccnode_branches[from_sccsetidx] = list(
            set(
                [
                    nodenum_to_sccsetidx[to_node]
                    for to_node in original_branches[from_node]
                    if not (from_sccsetidx == nodenum_to_sccsetidx[to_node])
                ]
            )
        )

    # SCC頂点のグラフについてトポロジカルソートする
    sorted_sccnode = topological_sort(n=nodenum_sccnode, edge=sccnode_branches)

    return [sccset_list[sccnode] for sccnode in sorted_sccnode]
