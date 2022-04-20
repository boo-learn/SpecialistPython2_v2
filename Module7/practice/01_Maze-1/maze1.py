def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w)


graph = [
    # список смежности
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [4, 1],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15
]

visited = [False] * (len(graph))
start = 14
start_points = [0, 3, 12]

dfs(start)

for element in start_points:
    if visited[element] == True:
        print(f"из точки {element} можно дойти до финиша")
    else:
        print(f"из точки {element} нельзя дойти до финиша")
