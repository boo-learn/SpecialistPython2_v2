# "Лабиринт с ключем"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - стартовые точки
# Посетив клетку K, можно подобрать ключ, который отпирают любую дверь.
# Определите:
# Из каких точек можно добраться до точки F?
# Какую дверь нужно открыть, чтобы добраться до точки P-2?


# Сюда отправляем полное решение
graph_open = [
    [1],  # 0
    [0, 2, 4],  # 1
    [1, 3],  # 2
    [2],  # 3
    [1, 5, 7],  # 4
    [4, 6],  # 5
    [5],  # 6
    [4, 8, 11],  # 7
    [7, 9],  # 8
    [8, 10],  # 9
    [9],  # 10
    [7],  # 11
    [13],  # 12
    [12],  # 13
]

graph_close = [
    [1],  # 0
    [0, 4],  # 1
    [3],  # 2
    [2],  # 3
    [1, 5, 7],  # 4
    [4, 6],  # 5
    [5],  # 6
    [4, 11],  # 7
    [9],  # 8
    [8, 10],  # 9
    [9],  # 10
    [7],  # 11
    [13],  # 12
    [12],  # 13
]


def dfs(graph, v):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(v)
    return visited


point_finish = 10
key_point = 6
start_points = {
    "P-2": 3,
    "P-1": 0,
    "P-4": 5,
    "P-3": 12,
    "P-5": 9,
}

for point_name, vertex in start_points.items():
    visited = dfs(graph_close, vertex)
    if visited[point_finish]:
        print(f"Из точки {point_name} можно дойти до финиша")
    elif visited[key_point]:
        visited = dfs(graph_open, vertex)
        if visited[point_finish]:
            print(f"Из точки {point_name} можно дойти до финиша с ключом")
    else:
        print(f"Из точки {point_name} нельзя дойти до финиша")
