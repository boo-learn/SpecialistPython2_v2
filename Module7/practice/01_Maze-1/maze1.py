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


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


my_dict = {0: 'S-1', 12: 'S-2', 3: 'S-3'}

for start in my_dict.keys():
    visited = [False] * (len(graph))
    dfs(start)
    if visited[14]:
        print(f'Из точки {my_dict[start]} можно дойти до финиша')
    else:
        print(f'Из точки {my_dict[start]} нельзя дойти до финиша')
    #print(visited)
