# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


# Решите задачу и выведите ответ в нужном формате
def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)

    return visited

# Опишите список смежности по изображению лабиринта из файла task.md
graph_сlose_door = [
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

graph_open_door = [
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
    [8, 13],  # 12
    [12],  # 13
    [15],  # 14
    [11, 14]  # 15
]

start_points = {5: 'S-1', 13: 'S-2', 3: 'S-3', 8: 'S-4'}

final = 0
visited = dfs(graph_сlose_door, final)
visited_with_key = dfs(graph_open_door, final)

for vertex in start_points:
    if visited[vertex]:
        print(f"Из точки {start_points[vertex]} можно добраться до финиша без ключа")
    elif visited_with_key[vertex]:
        print(f"Из точки {start_points[vertex]} можно добраться до финиша, используя ключ")
    else:
        print(f"Из точки {start_points[vertex]} нельзя добраться до финиша")
