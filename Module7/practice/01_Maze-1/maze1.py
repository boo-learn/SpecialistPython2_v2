# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)

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

# Решите задачу и выведите ответ в нужном формате
visited = [False] * (len(graph))  # list of visited places, initially all == False
start = 3
finish = 14
dfs(start)
if visited[finish]:
    print(f'Из точки {start} можно дойти до финиша')
else:
    print(f'Из точки {start} нельзя дойти до финиша')
