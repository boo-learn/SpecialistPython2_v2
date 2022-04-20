Вавилов Иван
graph_clouse = [
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
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11],  # 15
]
graph_open = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8, 13],  # 12
    [12],  # 13
    [15],  # 14
    [11, 14],  # 15
]


def dfs(start_point, graph):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


keys_of_the_doors = [7, 10]
last_key = keys_of_the_doors[-1]
finish = 0
start_points = {'S-1': 5, 'S-2': 13, 'S-3': 3, "S-4": 8}
for point_name, num_vertex in start_points.items():
    for key in keys_of_the_doors:
        visited = dfs(num_vertex, graph_clouse)
        if visited[key]:
            open_visited = dfs(num_vertex, graph_open)
            if open_visited[finish]:
                print(f"Из точки {num_vertex} можно дойти до финиша")
            else:
                print(f"Из точки {num_vertex} нельзя дойти до финиша")
            break
        else:
            if visited[finish]:
                print(f"Из точки {num_vertex} можно дойти до финиша")
                break
            else:
                if key == last_key:
                    print(f"Из точки {num_vertex} нельзя дойти до финиша")
