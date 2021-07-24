# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


# Решите задачу и выведите ответ в нужном формате
def dfs(v, graph):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(v)
    return visited


graph1 = [
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
graph2 = [
    [1],
    [0, 5],
    [6],
    [7],
    [5, 8],
    [1, 4],
    [2, 10],
    [3, 11],
    [4, 9, 12],
    [8, 10],
    [6, 9],
    [7, 15],
    [8],
    [12, 13],
    [15],
    [11, 14]
]
key1 = 7
key2 = 10
start_points = {5: 'S-1', 13: 'S-2', 3: 'S-3', 8: 'S-4'}
finish = 0
for point in start_points:
    visited = dfs(point, graph1)
    if visited[finish]:
        print(f'Из точки {start_points[point]} можно дойти до финиша без ключа')
    else:
        if visited[key1] or visited[key2]:
            visited = dfs(point, graph2)
            if visited[finish]:
                print(f'Из точки {start_points[point]} можно дойти до финиша с  ключом')
            else:
                print(f'Из точки {start_points[point]} нельзя дойти до финиша')
        else:
            print(f'Из точки {start_points[point]} нельзя дойти до финиша')
