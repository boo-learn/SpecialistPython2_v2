def dfs(graph, v):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(v)
    return visited


graph_with_doors = [
    [1],  # 0
    [0, 2],  # 1
    [7, 1],  # 2
    [6],  # 3
    [],  # 4
    [6],  # 5
    [5, 3],  # 6
    [2],  # 7
    [9],  # 8
    [8]  # 9
]

graph_without_doors = [
    [10],  # 0
    [10, 2, 5],  # 1
    [7, 1],  # 2
    [6],  # 3
    [],  # 4
    [6],  # 5
    [5, 3],  # 6
    [2],  # 7
    [9],  # 8
    [8],  # 9
    [9, 0, 1]  # 10
]

point_finish = 3
key_point = 7
start_points = {
    "P-1": 0,
    "P-2": 8,
    "P-3": 4,
    "P-4": 2,
    'P-5': 6,
}
door_points = {
    'D-1': 9,
    'D-2': 5,
}

for point_name, vertex in start_points.items():
    visited = dfs(graph_with_doors, vertex)
    if visited[point_finish]:
        print(f"Из точки {point_name} можно дойти до финиша")
    elif visited[key_point]:
        visited = dfs(graph_without_doors, vertex)
        if visited[point_finish]:
            print(f"Из точки {point_name} можно дойти до финиша")
        else:
            print(f"Из точки {point_name} нельзя дойти до финиша")
    else:
        print(f"Из точки {point_name} нельзя дойти до финиша")
