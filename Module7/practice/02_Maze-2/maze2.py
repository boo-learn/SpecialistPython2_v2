# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],
    [2],
    [3],
    [7],

    [5],
    [6],
    [],
    [3, 11],

    [9, 12],
    [8, 10],
    [9, 11],
    [7, 10, 15],

    [8, 13],
    [12, 14],
    [],
    [11]
]

# Решите задачу и выведите ответ в нужном формате


def dfs(v, n, graph):
    visited = [False] * n
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(v)
    return visited


start_points = {1: 'S-1', 5: 'S-2', 15: 'S-3'}
finish = 14

for start in start_points:
    visited = dfs(start, len(graph), graph)
    if visited[finish]:
        print(f'Из точки {start_points[start]} можно дойти до финиша')
    else:
        print(f'Из точки {start_points[start]} нельзя дойти до финиша')
