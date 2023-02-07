def dfs(graph, start_point):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited

graph = [
    [1, 3], # 0
    [0, 4], # 1
    [5], # 2
    [0, 4, 6], # 3
    [1, 3], # 4
    [2, 8], # 5
    [3], # 6
    [8], # 7
    [5, 7], # 8    
]

start = 7
result = dfs(graph, 7)

if result[2]:
    print("Can go to the bank")
else:
    print("Can't go to the bank")
