#!/usr/bin

graph = [
    [1],
    [0, 3, 5],
    [5],
    [1, 7],
    [8],
    [6, 2, 1],
    [5],
    [3],
    [4]
]

visited = [False] * (len(graph))
prev = [None] * (len(graph))

# вершина выхода
start = 6


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)

dfs(start)
for i in [4, 2, 0, 3]:
    if visited[i]:
        print(f"From vertex {i} exit can be reached")
