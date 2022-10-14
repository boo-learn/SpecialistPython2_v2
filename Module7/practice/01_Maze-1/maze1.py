# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def dfs(start_point, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


def get_to_finish(s, f, graph, point):
    visited = dfs(s, graph)
    if visited[f]:
        print(f'Из точки {point} можно дойти до финиша')
    else:
        print(f'Из точки {point} нельзя дойти до финиша')


# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1], #0
    [0, 5], #1
    [6], #2
    [7], #3
    [5, 8], #4
    [1, 4], #5
    [2, 10], #6
    [3], #7
    [4, 9, 12], #8
    [8, 10], #9
    [9, 6, 11, 14], #10
    [10], #11
    [8], #12
    [], #13
    [10, 15], #14
    [14], #15
]

# Решите задачу и выведите ответ в нужном формате
get_to_finish(0, 14, graph, 'S1')
get_to_finish(12, 14, graph, 'S1')
get_to_finish(3, 14, graph, 'S1')
