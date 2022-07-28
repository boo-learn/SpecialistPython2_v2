# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.

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

graph_close_door = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11]  # 15
]

graph_open_door = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6],  # 10
    [7, 15],  # 11
    [8, 13],  # 12
    [12],  # 13
    [15],  # 14
    [11, 15]  # 15
]

points_start = [{'name': 'S-1', 'vertex': 5}, {'name': 'S-2', 'vertex': 13}, {'name': 'S-3', 'vertex': 3},
                {'name': 'S-4', 'vertex': 8}]
point_finish = 0
keys = [7, 10]

for start in points_start:
    result_close_door = dfs(graph_close_door, start['vertex'])
    result_open_door = dfs(graph_open_door, start['vertex'])
    if result_close_door[point_finish]:
        print(f"Из точки {start['name']} можно дойти до финиша")
    else:
        have_key = False
        for vertex_key in keys:
            if result_close_door[vertex_key]:
                have_key = True
        if have_key and result_open_door[point_finish]:
            print(f"Из точки {start['name']} можно дойти до финиша")
        else:
            print(f"Из точки {start['name']} нельзя дойти до финиша")
