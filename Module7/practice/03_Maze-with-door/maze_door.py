# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.
# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под текущий лабиринт
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи


# Решите задачу и выведите ответ в нужном формате
def dfs(start_point, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                _dfs(w)

    _dfs(start_point)
    return visited


def start_finish(start_points, finish):

    for point_name, point in start_points.items():
        success = None
        for key in keys:
            if dfs(point, graph_closed)[key] and dfs(key, graph_opened)[finish]:
                success = "With key"
        if dfs(point, graph_closed)[finish]:
            success = "Without key"

        if success == "Without key":
            print(f'Из точки {point_name} можно дойти до финиша без ключа')
        elif success == "With key":
            print(f'Из точки {point_name} можно дойти до финиша с ключом')
        else:
            print(f'Из точки {point_name} нельзя дойти до финиша')


graph_closed = [
    [1],
    [0, 5],
    [6],
    [7],
    [8],
    [1],
    [2, 10],
    [3, 11],
    [4, 9, 12],
    [8, 10],
    [6, 9],
    [7, 15],
    [8],
    [],
    [],
    [11]
]

graph_opened = [
    [1],   #0
    [0, 5], #1
    [6], #2
    [7], #3
    [8, 5], #4
    [1, 4], #5
    [2, 10], #6
    [3, 11], #7
    [4, 9, 12], #8
    [8, 10], #9
    [6, 9],#10
    [7, 15],#11
    [8, 13],#12
    [12],#13
    [15], #14
    [11, 14], #15
]
start_points = {'S-1': 5, 'S-2': 13, 'S-3': 3, 'S-4': 8}
finish = 0
keys = [7, 10]

start_finish(start_points, finish)


# Решите задачу и выведите ответ в нужном формате
