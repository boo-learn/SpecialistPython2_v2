graph = [
    [1, 3, 4],    # 0
    [0, 4, 3],  #1
    [5],    # 2
    [0, 6, 4, 1], # 3
    [1, 3, 0],     # 4
    [2, 8],  # 5
    [3],  # 6
    [8],  # 7
    [7, 5], # 8
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



bank = dfs(graph, 7)[2]
if bank:
    print("Can go to the bank")
else:
    print("Can't go to the bank")
