# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.
def dfs(start_point, graph):
    visited_list = [False] * (len(graph))

    def _dfs(v):
        visited_list[v] = True
        for w in graph[v]:
            if not visited_list[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(start_point)
    return visited_list

# Решите задачу и выведите ответ в нужном формате

graph_with_doors = [
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
    [11]  # 15
]

graph_without_doors = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8, 5],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [12],  # 13
    [15],  # 14
    [11]  # 15
]

start_points = {"S-1": 5, "S-3": 3, "S-4": 8}
keys = [7, 10]
finish_point = 0

for point_name, vertex in start_points.items():
    visited = dfs(vertex, graph_with_doors)
    if visited[finish_point]:
        print(f"Из точки {vertex} можно дойти до финиша")
    else:
        has_key = False
        for key in keys:
            if visited[key]:
                has_key = True
        if has_key:
            visited_without_door = dfs(vertex, graph_without_doors)
            if visited_without_door[finish_point]:
                print(f"Из точки {point_name} можно дойти до финиша")
            else:
                print(f"Из точки {point_name} нельзя дойти до финиша")
        else:
            print(f"Из точки {point_name} нельзя дойти до финиша")


# Решите задачу и выведите ответ в нужном формате
