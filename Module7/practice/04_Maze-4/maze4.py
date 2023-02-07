def bfs(graph, start_vertex):
    start = start_vertex
    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)

    return lengths


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
    [3],  # 0
    [2],  # 1
    [1],  # 2
    [0,6],  # 3
    [5],  # 4
    [4,8],  # 5
    [3,7],  # 6
    [6],  # 7
    [5],  # 8
]

start_points = 1
point_bank = 3
point_shop = 5
point_bar = 8

visited = dfs(graph, start_points)

if visited[point_bank]:
    print(f"Сan go to the bank")
else:
    print(f"Can't go to the bank")

if visited[point_shop]:
    print(f"Сan go to the shop")
else:
    print(f"Can't go to the shop")

if visited[point_bar]:
    print(f"Сan go to the bar")
else:
    print(f"Can't go to the bar")
