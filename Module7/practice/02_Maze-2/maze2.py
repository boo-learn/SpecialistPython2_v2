def dfs(start_point, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [4],  # 0
    [5],  # 1
    [6],  # 2
    [],  # 3
    [0,8],  # 4
    [1,9],  # 5
    [2,7,10],  # 6
    [6],  # 7
    [4],  # 8
    [5,13],  # 9
    [6,14],  # 10
    [],  # 11
    [],  # 12
    [9],  # 13
    [10,15],  # 14
    [14]  # 15
]


finish_point = 14
start_points = (1,5,15)
vis = dfs(finish_point, graph)
n= 1
for start_point in start_points:
    if vis[start_point] == True:
        print(f'Из точки S-{n} можно дойти до финиша')
    else:
        print(f'Из точки S-{n} нельзя дойти до финиша')
    n += 1
