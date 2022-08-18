def dfs(graph, start):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    
    _dfs(start)
    return visited

graph_closed = [
    [1],            # 0
    [0, 5],         # 1
    [6],         # 2
    [7],         # 3
    [8],            # 4
    [1],         # 5
    [2, 10],            # 6
    [3, 11],        # 7
    [4, 9, 12],        # 8
    [8, 10],        # 9
    [6, 9],        # 10
    [7, 15],    # 11
    [8],        # 12
    [],       # 13
    [],           # 14
    [11]            # 15
]

graph_opened = [
    [1],            # 0
    [0, 5],         # 1
    [6],         # 2
    [7],         # 3
    [8, 5],            # 4
    [1, 4],         # 5
    [2, 10],            # 6
    [3, 11],        # 7
    [4, 9, 12],        # 8
    [8, 10],        # 9
    [6, 9],        # 10
    [7, 15],    # 11
    [8, 13],        # 12
    [12],       # 13
    [15],           # 14
    [11, 14]            # 15
]

keys = [7, 10]
start_points = {'S-1' : 5,
                'S-2' : 13,
                'S-3' : 3,
                'S-4' : 8
}
finish = 0

for name, start in start_points.items():
    graph = graph_closed
    if dfs(graph, start)[finish]:
        print(f"Из точки {name} можно добраться до финиша без ключа")
        continue

    for key in keys:
        if dfs(graph, start)[key]:
            graph = graph_opened
            break

    if dfs(graph, start)[finish]:
        print(f"Из точки {name} можно добраться до финиша, используя ключ")
    else:
        print(f"Из точки {name} нельзя добраться до финиша")
