def dfs(start_vertex, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                _dfs(w)

    _dfs(start_vertex)
    return visited


maze = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14]  # 15
]
start = [0, 3, 12]
finish = 14

for point in start:
    run = dfs(point, maze)
    if run [finish] == True:
        print(f"Из точки {point} можно дойти до финиша")
    else:
        print(f"Из точки {point} нельзя дойти до финиша")
