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
    [2],  # 1
    [1,3],  # 2
    [2],  # 3
    [0],  # 4
    [6,9],  # 5
    [5,7],  # 6
    [6,11],  # 7
    [],  # 8
    [5,13],  # 9
    [],  # 10
    [7,15],  # 11
    [13],  # 12
    [12,9,14],  # 13
    [13],  # 14
    [11]  # 15
]


start_point = 14
vis = dfs(start_point, graph)
for num, vi in enumerate(vis,1):
    if vi:
        print(f"Из точки S-{num} можно дойти до финиша")
    else:
        print(f"Из точки S-{num} нельзя дойти до финиша")
print(vis)
