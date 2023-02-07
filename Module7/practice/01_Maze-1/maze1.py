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
    [1], # 0
    [0, 4], # 1
    [5], # 2
    [6, 4], # 3
    [1, 3, 5], # 4
    [2, 4], # 5
    [3], # 6
    [8], # 7
    [7], # 8    
]

start = 0
result = dfs(graph, 0)

if result[7]:
    print("Can go to the bank")
else:
    print("Can't go to the bank")
