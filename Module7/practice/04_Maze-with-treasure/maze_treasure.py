from itertools import combinations


def dfs(v, n, graph):
    visited = [False] * n
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]: 
                _dfs(w)
    _dfs(v)
    return visited

graph = [
    [1, 4],
    [0, 2], 
    [1],
    [7],

    [0],
    [6, 9], 
    [5, 10],
    [3, 11],

    [12, 9],
    [5, 8, 10], 
    [9, 6, 14],
    [7],

    [8],
    [], 
    [10, 15],
    [14]
]

treasures = {
    1: 1, 
    2: 2,
    4: 3,
    6: 5,
    7: 3,
    9: 5,
    10: 3,
    13: 8,
    14: 4,
    15: 7
}

start_points = {0: 'S-1', 3: 'S-3', 12: 'S-2'}

for start_point in start_points:
    visited = dfs(start_point, len(graph), graph)
    collected = []
    for point, value in  treasures.items():
        if visited[point]:
            collected.append(value)
    collected.sort()
    print(f'Из точки {start_points[start_point]} можно собрать сокровищ' 
          f'суммарной ценностью {sum(collected[-2:])}')
