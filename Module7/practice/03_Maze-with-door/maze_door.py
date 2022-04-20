# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def dfs(start_vertex, graph):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                _dfs(w)

    _dfs(start_vertex)
    return visited


# Опишите список смежности по изображению лабиринта из файла task.md
graph_close = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3,11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6],  # 10
    [7,15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11],  # 15
]
graph_open = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8,5],  # 4
    [1,4],  # 5
    [2, 10],  # 6
    [3,11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6],  # 10
    [7,15],  # 11
    [8],  # 12
    [],  # 13
    [15],  # 14
    [11,14],  # 15
]


finish = 0
start_points = {"S-1": 5, "S-2": 13, "S-3": 3, "S-4": 8}
visited_close = dfs(finish, graph_close)
visited_open =  dfs(finish, graph_open)
for point_name, num_vertex in start_points.items():
    if visited_close[num_vertex]:
        print(f"из точки {point_name} можно дойти до финиша без ключа")
    elif visited_open[num_vertex]:
        print(f"из точки {point_name} можно дойти до финиша используя ключ")
    else:
        print(f"из точки {point_name} нельзя дойти до финиша")
