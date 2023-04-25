def dfs(graph: list[list], start_point: int) -> list[bool]:
    """
    Алгоритм поиска в глубину (DFS)
    """
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited

graph1 = [
    [1],            # 0
    [4],            # 1
    [5],            # 2
    [4, 6],         # 3
    [1, 3, 5],      # 4
    [2, 4],         # 5
    [3],            # 6
    [8],            # 7
    [7]             # 8
]

MSG1 = "Сan go to the bank"
MSG2 = "Сan't go to the bank"

visited = dfs(graph1, start_point=7)
print(visited)

if visited[0] and visited[7]:
    print(MSG1)
else:
    print(MSG2)
