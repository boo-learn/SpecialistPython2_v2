import copy


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


graph_closed_doors = [
    [1],         # 0
    [0, 5],      # 1
    [6],         # 2
    [7],         # 3
    [8],         # 4
    [1],         # 5
    [2, 10],     # 6
    [3, 11],     # 7
    [4, 9, 12],  # 8
    [8, 10],     # 9
    [6, 9],      # 10
    [7, 15],     # 11
    [8],         # 12
    [],          # 13
    [],          # 14
    [11]         # 15
]

doors = [(4, 5), (12, 13), (14, 15)]
graph_open_doors = copy.deepcopy(graph_closed_doors)
for point1, point2 in doors:
    graph_open_doors[point1].append(point2)
    graph_open_doors[point2].append(point1)

# print(graph_closed_doors)
# print(graph_open_doors)

start_points = [5, 13, 3, 8, 2, 14, 4, 1, 0]
finish_point = 0
keys = [7, 10]

for point in start_points:
    finish_point_reached = False
    visited_points = dfs(graph_closed_doors,  start_point=point)
    if visited_points[finish_point]:
        finish_point_reached = True
        print(f"Из точки {point} можно добраться до финиша без ключа")
    else:
        key_found = False
        for key in keys:
            key_found = visited_points[key]
            if key_found:
                visited_points_with_key = dfs(graph_open_doors, start_point=key)
                if visited_points_with_key[finish_point]:
                    finish_point_reached = True
                    print(f"Из точки {point} можно добраться до финиша с ключом")
    if not finish_point_reached:
        print(f"Из точки {point} нельзя добраться до финиша")
