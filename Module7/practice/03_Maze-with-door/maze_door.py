# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.

def dfs(start_point, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


graph_closed_doors = [
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
    [11],  # 15
]

graph_open_doors = [
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
    [9, 6],  # 10
    [7, 15],  # 11
    [8, 13],  # 12
    [12],  # 13
    [15],  # 14
    [11, 14],  # 15
]

# Решите задачу и выведите ответ в нужном формате
finish_point = 0
start_points = {
    "S-1": 5,
    "S-2": 13,
    "S-3": 3,
    "S-4": 8
}
key_points = [7, 10]

for name, point in start_points.items():
    visited_no_key = dfs(point, graph_closed_doors)
    if visited_no_key[finish_point]:
        print(f'Из точки {name} можно дойти до финиша без ключа')
    else:
        finish = False
        for key in key_points:
            if visited_no_key[key]:
                visited_with_key = dfs(point, graph_open_doors)
                if visited_with_key[finish_point]:
                    finish = True
                    break
        if finish:
            print(f'Из точки {name} можно дойти до финиша, используя ключ')
        else:
            print(f'Из точки {name} нельзя дойти до финиша')



