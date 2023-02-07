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
    [0],  # 3
    [7],  # 4
    [8],  # 5
    [7],  # 6
    [4, 6],  # 7
    [5],  # 8
]

start_points = 0
final = 7

visited = dfs(graph, start_points)

print(visited)
if visited[final]:
    print(f"Сan go to the bank")
else:
    print(f"Can't go to the bank")
