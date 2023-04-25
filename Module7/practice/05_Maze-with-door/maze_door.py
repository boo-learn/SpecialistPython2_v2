# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


# Решите задачу и выведите ответ в нужном формате
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


rooms_closed_doors = [
    # список смежности
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
rooms_open_doors = [
    # список смежности
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
    [],  # 13
    [15],  # 14
    [11, 14],  # 15
]

rooms = {
    "S-1": 5,
    "S-2": 13,
    "S-3": 3,
    "S-4": 8
}
finish_point = 0
keys = [7, 10]

for room, point in rooms.items():
    opened_with_keys = False
    visited = dfs(rooms_closed_doors, start_point=point)
    for key in keys:
        if visited[key]:
            visited = dfs(rooms_open_doors, start_point=point)
            opened_with_keys = True
    if visited[finish_point] and opened_with_keys:
        print(f"Из точки {room} можно добраться до финиша, используя ключ")
    elif visited[finish_point] and not opened_with_keys:
        print(f"Из точки {room} можно добраться до финиша без ключа")
    else:
        print(f"Из точки {room} нельзя добраться до финиша")
