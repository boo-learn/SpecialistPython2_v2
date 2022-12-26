# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи

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


graph = [
    [1],  # 0
    [0, 2],  # 1
    [1, 3],  # 2
    [2, 7],  # 3
    [5],  # 4
    [4, 6],  # 5
    [5],  # 6
    [3, 11],  # 7
    [9, 12],  # 8
    [8, 10],  # 9
    [9, 11],  # 10
    [7, 10, 15],  # 11
    [8, 13],  # 12
    [12, 14],  # 13
    [13],  # 14
    [11],  # 15
]

# Решите задачу и выведите ответ в нужном формате
get_to_finish(1, 14, graph, 'S1')
get_to_finish(5, 14, graph, 'S2')
get_to_finish(15, 14, graph, 'S3')
