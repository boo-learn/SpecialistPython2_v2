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


def start_finish(start, finish):
    if dfs(start, graph)[finish]:
        print(f'Из точки {start} можно дойти до точки {finish}')
    else:
        print(f'Из точки {start} нельзя дойти до точки {finish}')


graph = [
    [1],
    [0, 2],
    [1, 3],
    [2, 7],
    [5],
    [6, 4],
    [5],
    [3, 11],
    [9, 12],
    [8, 10],
    [9, 11],
    [7, 10, 15],
    [8, 13],
    [12, 14],
    [13],
    [11]
]

s1 = 1
s2 = 5
s3 = 15
finish = 14

start_finish(s1, finish)
start_finish(s2, finish)
start_finish(s3, finish)
