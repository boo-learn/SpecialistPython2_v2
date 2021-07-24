closed_graph = [
    [1],
    [0, 5],
    [6],
    [7],
    [8],
    [1],
    [2, 10],
    [3, 11],
    [4, 9, 12],
    [8, 10],
    [6, 9],
    [7, 15],
    [8],
    [],
    [],
    [11],
]
open_graph = [
    [1],
    [0, 5],
    [6],
    [7],
    [8, 5],
    [1, 4],
    [2, 10],
    [3, 11],
    [4, 9, 12],
    [8, 10],
    [6, 9],
    [7, 15],
    [8, 13],
    [12],
    [15],
    [11, 14],
]
keys = [7, 10]
    

def dfs(v, n, graph):
    visited = [False] * n
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(v)
    return visited


start_points = {5: 'S-1', 13: 'S-2', 3: 'S-3', 8: 'S-4', 9: 'S-5'}
finish = 0


for start in start_points:
    visited = dfs(start, len(closed_graph), closed_graph)
    if visited[finish]:
        print(f'Из точки {start_points[start]} можно дойти до финиша')
    key_found = list(filter(lambda x: visited[x], keys))
    if key_found:
        visited = dfs(start, len(open_graph), open_graph)
        if visited[finish]:
            print(f'Из точки {start_points[start]} можно дойти до финиша, используя ключ')
    else:
        print(f'Из точки {start_points[start]} нельзя дойти до финиша')
