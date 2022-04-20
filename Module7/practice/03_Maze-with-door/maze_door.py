# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.
def dfs(start_vertex, graph):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                _dfs(w)

    _dfs(start_vertex)
    return visited


# Решите задачу и выведите ответ в нужном формате
graph = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3+
    [8],  # 4-
    [1],  # 5-
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10+
    [7, 15],  # 11
    [8],  # 12-
    [],  # 13-
    [],  # 14-
    [11],  # 15-
]

graph_with_doors = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3+
    [8, 5],  # 4-
    [1, 4],  # 5-
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10+
    [7, 15],  # 11
    [8, 13],  # 12-
    [12],  # 13-
    [15],  # 14-
    [11, 14],  # 15-
]

key_position = [10, 7]
door_position = [4 - 5, 12 - 13, 14 - 15]

finish_point = 0
start_points = {"S-1": 5, "S-2": 13, "S-3": 3, "S-4": 8}

for point_name, num_vertex in start_points.items():
    start_point = num_vertex
    visited_key=False
    visited = dfs(start_point, graph)
    if visited[finish_point]:
        print(f"Из точки {point_name} можно добраться до финиша без ключа")
    else:
        for position in key_position:
            if visited[position]:
                visited_key=True
        if visited_key:
            visited_new = dfs(start_point, graph_with_doors)
            if visited_new[finish_point]:
                print(f"Из точки {point_name} можно добраться до финиша, используя ключ")
            else:
                print(f"Из точки {point_name} нельзя добраться до финиша")
        else:
            print(f"Из точки {point_name} нельзя добраться до финиша")
