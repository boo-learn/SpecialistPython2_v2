graph = [
    [1, ],    # 0
    [0, 4],  #1
    [5],    # 2
    [6, 4], # 3
    [1, 3, 5],     # 4
    [4, 2],  # 5
    [3],  # 6
    [8],  # 7
    [7], # 8
]

def dfs(graph: list, start_point: int) -> list[bool]:
    """
    Алгоритм поиска в глубину
    """
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


shop = (dfs(graph, 0)[2], "shop")
bank = (dfs(graph, 0)[7], "bank")

def answer(var):
    if var[0]:
        print(f"Can go to the {var[1]}")
    else:
        print(f"Can't go to the {var[1]}")

answer(shop)
answer(bank)
