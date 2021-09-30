# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.
def bfs(graph, start):
    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    return lengths


graph_close = [
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
    [9, 6],  # 10
    [7, 15],  # 11
    [8, 13],  # 12
    [12],  # 13
    [15],  # 14
    [11, 14],  # 15
]



starts_points = {
    "s-1": 5,
    "s-2": 13,
    "s-3": 3,
    "s-4": 8,
}

finish = 0

keys = [7, 10]

for point_name, vertex in starts_points.items():
    visited1 = bfs(graph_close, vertex)
    visited2 = bfs(graph_open, vertex)
    if visited1[finish] != None:
        print(f'Из точки {point_name} можно добраться до финиша без ключа')
    else:
        for key in keys:
            if visited1[key] != None:
                if visited2[finish] != None:
                    print(f'Из точки {point_name} можно добраться до финиша с ключом')
                    break
                else:
                    ()
        else:
            print(f'Из точки {point_name} нельзя добраться до финиша')


# Решите задачу и выведите ответ в нужном формате
