graph = [
    [1],    # 0
    [0, 4],  #1
    [5],    # 2
    [4, 6], # 3
    [1, 3, 5],     # 4
    [2, 4],  # 5
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



bank = dfs(graph, 0)[7]
if bank:
    print("Can go to the bank")
else:
    print("Can't go to the bank")
