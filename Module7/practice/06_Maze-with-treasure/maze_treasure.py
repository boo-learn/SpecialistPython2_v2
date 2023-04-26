# Сюда отправляем решение задачи "Лабиринт с сокровищами"


# Решите задачу и выведите ответ в нужном формате
def bfs(graph: list, start_point: int, weight: dict) -> list[int | None]:
    """
    Алгоритм поиска в ширину
    """
    lengths = [None] * len(graph)
    lengths[start_point] = weight[start_point]
    queue = [start_point]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + weight[vertex]
                queue.append(vertex)

    return lengths


graph = [
    # список смежности
    [1, 4],  # 0
    [0, 2],  # 1
    [1],  # 2
    [7],  # 3
    [0],  # 4
    [6, 9],  # 5
    [5, 10],  # 6
    [3, 11],  # 7
    [9, 12],  # 8
    [5, 8, 10],  # 9
    [6, 9, 14],  # 10
    [7],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15
]

treasures_value = {
    0: 0,
    1: 1,
    2: 2,
    3: 0,
    4: 3,
    5: 0,
    6: 5,
    7: 3,
    8: 0,
    9: 5,
    10: 3,
    11: 0,
    12: 0,
    13: 8,
    14: 4,
    15: 7
}
start_points = {
    'S-1': 0,
    'S-2': 12,
    'S-3': 3
}


for room, point in start_points.items():
    values = bfs(graph, start_point=point, weight=treasures_value)
    while None in values:
        values.remove(None)
    print(f"Из точки {room} можно собрать сокровищ суммарной ценностью {max(values)}")
