# "Лабиринт с ключем"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - стартовые точки
# Посетив клетку K, можно подобрать ключ, который отпирают любую дверь.
# Определите:
# Из каких точек можно добраться до точки F?
# Какую дверь нужно открыть, чтобы добраться до точки P-2?


# Сюда отправляем полное решение

graph_no_key = [
    # список смежности
    [1],  # 0
    [0, 2],  # 1
    [1, 7],  # 2
    [6],  # 3
    [],  # 4
    [6],  # 5
    [3, 5],  # 6
    [2],  # 7
    [9],  # 8
    [8],  # 9
]

graph_with_key = [
    # список смежности
    [10],  # 0
    [10, 2, 5],  # 1
    [1, 7],  # 2
    [6],  # 3
    [],  # 4
    [6, 1],  # 5
    [3, 5],  # 6
    [2],  # 7
    [9],  # 8
    [8, 10],  # 9
    [0, 9, 1],  # 10
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

finish_point = 3
key = 7
start_points = {
    "P-1": 0,
    "P-2": 8,
    "P-3": 4,
    "P-4": 2, 
    "P-5": 6
}

for point_name, vertex in start_points.items():
    visited_no_key = dfs(graph_no_key, vertex)
    if visited_no_key[key]:
        visited_with_key = dfs(graph_with_key, vertex)
        if visited_with_key[finish_point]:
            print(f'Из точки {point_name} можно дойти до финиша')
    elif visited_no_key[finish_point]:
        print(f'Из точки {point_name} можно дойти до финиша')
    else:
        print(f'Из точки {point_name} нельзя дойти до финиша')
