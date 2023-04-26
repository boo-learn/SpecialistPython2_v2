from copy import deepcopy
graph = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11]  # 15
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



finish_point = 0
start_points = {5: "S-1", 8: "S-4", 13: "S-2", 3: "S-3"}
key_points = [10, 7]
paths = {}
cant_go_points = dict(start_points) # Словарь точек из которых нельзя добраться до финиша
graph_opened = deepcopy(graph)
doors = [[4, 5], [12, 13], [14, 15]]

for start_point, point_name in start_points.items():
    for key in key_points:

        for door in doors:
            graph_opened[door[1]].append(door[0])
            graph_opened[door[0]].append(door[1])

        can_get_key = dfs(graph, start_point)[key]
        no_key_path = dfs(graph, start_point)[finish_point]
        path_with_key = dfs(graph_opened, start_point)[finish_point]

        if can_get_key:
            if path_with_key:
                paths[point_name] = "with_key"
                if start_point in cant_go_points.keys():
                    del cant_go_points[start_point]

        elif no_key_path:
            paths[point_name] = "with_out_key"
            if start_point in cant_go_points.keys():
                del cant_go_points[start_point]

for point_name in cant_go_points.values():
    paths[point_name] = "cant go"

for name, path in paths.items():
    if path == "with_key":
        print(f"Из точки {name} можно добраться до финиша используя ключ")
    elif path == "with_out_key":
        print(f"Из точки {name} можно добраться до финиша без ключа")
    else:
        print(f"Из точки {name} нельзя добраться до финиша")
