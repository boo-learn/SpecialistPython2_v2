def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


def possible(graph, start_vertex, end_vertex):
    if graph[end_vertex]:
        return f'Из точки {start_vertex} можно дойти до финиша'
    else:
        return f'Из точки {start_vertex} нельзя дойти до финиша'


graph = [
    [1],  # 0
    [0, 2],  # 1
    [1, 3],  # 2
    [2, 7],  # 3
    [5],  # 4
    [4, 6],  # 5
    [5],  # 6
    [3, 11],  # 7
    [9, 12],  # 8
    [8, 10],  # 9
    [9, 11],  # 10
    [7, 10, 15],  # 11
    [8, 13],  # 12
    [12, 14],  # 13
    [13],  # 14
    [11],  # 15
]

s1 = 1
s2 = 5
s3 = 15
end1 = 14

visited1 = dfs(graph, s1)
print(possible(visited1, s1, end1))

visited2 = dfs(graph, s2)
print(possible(visited2, s2, end1))

visited3 = dfs(graph, s3)
print(possible(visited3, s3, end1))
