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


map_of_treasures = [
    [1, 4],      # 0
    [0, 2],      # 1
    [1],         # 2
    [7],         # 3
    [0],         # 4
    [6, 9],      # 5
    [5, 10],     # 6
    [3, 11],     # 7
    [9, 12],     # 8
    [5, 8, 10],  # 9
    [6, 9, 14],  # 10
    [7],         # 11
    [8],         # 12
    [],          # 13
    [10, 15],    # 14
    [14]         # 15
]

treasures = [0, 1, 2, 0, 3, 0, 5, 3, 0, 5, 3, 0, 0, 8, 4, 7]

start_points = [0, 12, 3, 13, 11, 8]

for point in start_points:
    total_treasures = 0
    visited_points = dfs(map_of_treasures, start_point=point)
    for n, temp_point in enumerate(visited_points):
        if temp_point:
            total_treasures += treasures[n]
    print(f"Из точки {point} можно собрать сокровищ суммарной ценностью {total_treasures}")
