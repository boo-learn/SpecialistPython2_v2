# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],
    [0, 5],
    [6],
    [3],
    [5, 8],
    [4, 1],
    [2, 10],
    [3],
    [4, 9, 12],
    [8, 10],
    [9, 6, 11, 14],
    [10],
    [8],
    [],
    [10, 15],
    [14],
]


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


starts = [[0, 'S-1'], [12, 'S-2'], [3, 'S-3']]
finish = 14
for start in starts:
    visited = [False] * (len(graph))
    dfs(start[0])
    if visited[finish]:
        print(f'Из точки {start[1]} можно дойти до финиша')
    else:
        print(f'Из точки {start[1]} нельзя дойти до финиша')
