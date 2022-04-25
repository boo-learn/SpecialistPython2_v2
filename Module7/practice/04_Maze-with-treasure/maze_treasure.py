def dfs(start_vertex, graph):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                _dfs(w)

    _dfs(start_vertex)
    return visited


graph = [
    [1, 4],  # 0
    [0, 2],  # 1
    [1],  # 2
    [7],  # 3+
    [0],  # 4-
    [6, 9],  # 5-
    [10],  # 6
    [3, 11],  # 7
    [12, 9],  # 8
    [8, 5, 10],  # 9
    [6, 9, 14],  # 10+
    [7],  # 11
    [8],  # 12-
    [],  # 13-
    [10, 15],  # 14-
    [14],  # 15-
]
treasure_points = [0, 1, 2, 0, 3, 0, 5, 3, 0, 5, 3, 0, 0, 8, 4, 7]
# позиция в списке - цифра точки \ значение в списке - ценость

start_points = {"S-1": 0, "S-2": 12, "S-3": 3}

for point_name, num_vertex in start_points.items():
    visited = dfs(num_vertex, graph)
    treasures_visited=[]
    for i in range(len(visited)):
        if visited[i]:
            treasures_visited.append(treasure_points[i])
    treasures_visited.sort(reverse=True)
    print(f"Из точки {point_name} можно собрать сокровищ максимальной ценностью {sum(treasures_visited[:2])}")
