# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],
    [5],
    [6],
    [7],
    [5, 8],
    [4, 1],
    [2, 10],
    [3],
    [4, 9],
    [8, 10],
    [6, 9, 11, 14],
    [10],
    [8],
    [],
    [10, 15],
    [14]
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


start_points = {0: 'S-1', 12: 'S-2', 3: 'S-3'}
finish = 14

for start in start_points:
    visited = dfs(start, len(graph), graph)
    if visited[finish]:
        print(f'Из точки {start_points[start]} можно дойти до финиша')
    else:
        print(f'Из точки {start_points[start]} нельзя дойти до финиша')
