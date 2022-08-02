# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15
]

# Решите задачу и выведите ответ в нужном формате
finish = 14

start_list = [
    {
        'name': 'S-1',
        'point': 0
    },
    {
        'name': 'S-2',
        'point': 12
    },
    {
        'name': 'S-3',
        'point': 3
    },
]


def check_possibility(start, finish):
    print(f'Из точки {start["name"]} можно дойти до финиша') if dfs(graph, start["point"])[finish] else print(
        f'Из точки {start["name"]} нельзя дойти до финиша')


for i in start_list:
    check_possibility(i, finish)
