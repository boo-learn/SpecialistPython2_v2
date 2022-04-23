# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
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
    [0, 5],
    [6],
    [7],
    [5, 8],
    [1, 4],
    [2, 10],
    [3],
    [4, 9, 12],
    [8, 10],
    [6, 9, 11, 14],
    [10],
    [8],
    [],
    [10, 15],
    [14]
]

s1 = 0
s2 = 12
s3 = 3
finish = 14

start_finish(s1, finish)
start_finish(s2, finish)
start_finish(s3, finish)
# Решите задачу и выведите ответ в нужном формате
