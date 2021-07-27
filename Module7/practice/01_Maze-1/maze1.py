# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def dfs(v, graph):
    visited = [False] * (len(graph))
    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                dfs(w)

    _dfs(v)
    return visited

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    # список смежности
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3]  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [9, 10, 15]  # 14
    [14] # 15
]


start_points = {0: 'S-1', 12: 'S-2', 3: 'S-3'}

finish = 14

for start_point in start_points.keys():
    visited = dfs(start_point, graph)
    if visited[finish]:
        print(f'Из точки {start_points[start_point]} можно дойти до финиша')
    else:
        print(f'Из точки {start_points[start_point]} нельзя дойти до финиша')
