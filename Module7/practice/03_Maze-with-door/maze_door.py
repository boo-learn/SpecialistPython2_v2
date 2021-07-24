# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
def dfs(v, graph):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(v)
    return visited


graph1 = [
    # список смежности
    [1],  # 0
    [5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11]  # 15
]

graph2 = [
    # список смежности
    [1],  # 0
    [5],  # 1
    [6],  # 2
    [7],  # 3
    [8, 5],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8, 13],  # 12
    [12],  # 13
    [15],  # 14
    [14]  # 15
]

key_points = {7: 'K-1', 10: 'K-2'}

start_points = {5: 'S-1', 13: 'S-2', 3: 'S-3', 8: 'S-4'}

keys = 0
while keys == 0:
    for key_point in key_points:
        finish = key_point
        for start_point in start_points.keys():
            visited = dfs(start_point, graph1)
            if visited[finish]:
                print(f'Из точки {start_points[start_point]} можно дойти до ключа')
                keys = 1
                break
            else:
                print(f'Из точки {start_points[start_point]} нельзя дойти до ключа')
                #keys = 0


finish = 0
for start_point in start_points.keys():
    visited = dfs(start_point, graph2)
    if visited[finish]:
        print(f'Из точки {start_points[start_point]} можно дойти до финиша')
    else:
        print(f'Из точки {start_points[start_point]} нельзя дойти до финиша')
