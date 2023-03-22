def dfs(graph, start_vertex):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


graph = [
    [1], #0
    [0,4], #1
    [5], #2
    [4,6], #3
    [1,3,5], #4
    [4,2], #5
    [3], #6
    [8], #7
    [7], #8
]

start = 0
points = {"shop":2, "bank":7}

visited= dfs(graph, start)

for point in points:
    if visited[points.get(point)]:
        print(f"Сan go to the {point}")
    else:
        print(f"Сan't go to the {point}")

