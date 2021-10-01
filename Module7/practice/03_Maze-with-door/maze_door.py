# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


# Решите задачу и выведите ответ в нужном формате
def dfs(graph, v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(graph, w)
    return visited


closed_door_graph = [
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

open_door_graph = [
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

finish = 0
starts = {
    "s-1": 5,
    "s-2": 13,
    "s-3": 3,
    "s-4": 8
}
keys = [10, 7]


for point_name, vertex in starts.items():
    visited = [False] * len(closed_door_graph)
    dfs(closed_door_graph, vertex)
    if visited[finish]:
        print(f'Из точки {point_name} можно дойти до финиша без ключа')
    else:
        for key in keys:
            if visited[key]:
                visited = [False] * len(open_door_graph)
                dfs(open_door_graph, vertex)
                if visited[finish]:
                    print(f'Из точки {point_name} можно дойти до финиша, используя ключ')
                    break
                else:
                    print(f'Из точки {point_name} нельзя дойти до финиша')
                    break
            else:
                print(f'Из точки {point_name} нельзя дойти до финиша')
                break
