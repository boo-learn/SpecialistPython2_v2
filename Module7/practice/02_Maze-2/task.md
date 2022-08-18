def dfs(graph, start):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    
    _dfs(start)
    return visited

graph = [
    # список смежности
    [1],            # 0
    [0, 2],         # 1
    [1, 3],         # 2
    [2, 7],         # 3
    [5],            # 4
    [4, 6],         # 5
    [5],            # 6
    [3, 11],        # 7
    [9, 12],        # 8
    [8, 10],        # 9
    [9, 11],        # 10
    [7, 10, 15],    # 11
    [8, 13],        # 12
    [12, 14],       # 13
    [13],           # 14
    [11]            # 15
]

start_points = [1, 5, 15]
finish = 14

counter = 1
for start in start_points:
    if dfs(graph, start)[finish]:
        print(f"Из точки S-{counter} можно дойти до финиша")
    else:
        print(f"Из точки S-{counter} нельзя дойти до финиша")
    counter += 1
