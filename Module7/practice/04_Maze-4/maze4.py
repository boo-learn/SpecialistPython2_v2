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
    [1],        # 0
    [4],        # 1
    [5],        # 2
    [4],        # 3
    [1, 3, 7],  # 4
    [2],        # 5
    [],         # 6
    [4, 8],     # 7
    [7]         # 8
]

MSG1_1 = "Сan go to the bank"
MSG1_2 = "Сan't go to the bank"

MSG2_1 = "Сan go to the shop"
MSG2_2 = "Сan't go to the shop"

MSG3_1 = "Сan go to the bar"
MSG3_2 = "Сan't go to the bar"

visited = dfs(graph1, start_point=1)

if visited[1] and visited[3]:
    print(MSG1_1)
else:
    print(MSG1_2)

if visited[1] and visited[5]:
    print(MSG2_1)
else:
    print(MSG2_2)

if visited[1] and visited[8]:
    print(MSG3_1)
else:
    print(MSG3_2)
  
