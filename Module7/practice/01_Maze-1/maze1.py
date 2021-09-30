# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
       # список смежности
    [1],      # 0
    [0, 5],   # 1
    [6],      # 2
    [7],      # 3
    [5,8],    # 4
    [1,4],    # 5
    [2,10],   # 6
    [3],      # 7
    [4,9,12], # 8
    [8,10],   # 9
    [6,9,11,14],# 10
    [10],     # 11
    [8],      # 12
    [],       # 13
    [10,15],  # 14
    [14]      # 15
]

# Решите задачу и выведите ответ в нужном формате
def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)

finish = 14
start = [0, 12, 3]
s = 1
for posstart in start:
    visited = [False] * (len(graph))
    dfs(posstart)
    if visited[finish]:
        print(f'Из точки S-{s} можно дойти до финиша')
    else:
        print(f'Из точки S-{s} нельзя дойти до финиша')
    s +=1
