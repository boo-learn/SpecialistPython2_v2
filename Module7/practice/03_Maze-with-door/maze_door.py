# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.

def dfs(v, graph):
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    visited = [False] * (len(graph))
    _dfs(v)
    return visited


graph_with_doors = [
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
    [11],
]
graph_without_doors = [
    [1],
    [0, 5],
    [6],
    [7],
    [8, 5],
    [1, 4],
    [2, 10],
    [3, 11],
    [4, 9, 12],
    [8, 10],
    [6, 9],
    [7, 15],
    [8, 13],
    [12],
    [15],
    [11, 14],
]
keys = [7, 10]
finish = 0
start_points = {5: 'S-1', 13: 'S-2', 3: 'S-3', 8: 'S-4'}

for start_point in start_points.keys():
    visited = dfs(start_point, graph_with_doors)
    is_key = False
    if visited[finish]:
        print(f'Из точки {start_points[start_point]} можно добраться до финиша без ключа')
        continue
    for key in keys:
        if visited[key]:
            is_key = True
            break
    if is_key:
        visited = dfs(start_point, graph_without_doors)
        if visited[finish]:
            print(f'Из точки {start_points[start_point]} можно добраться до финиша, используя ключ')
            continue
    print(f'Из точки {start_points[start_point]} нельзя добраться до финиша')
