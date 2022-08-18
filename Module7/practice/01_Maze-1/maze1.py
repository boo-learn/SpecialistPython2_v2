def dfs(graph, start):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start)
    return visited


graph = [
    # список смежности
    [1],         # 0
    [5],         # 1
    [6],         # 2
    [7],         # 3
    [5, 8],         # 4
    [1, 4],         # 5
    [2, 10],         # 6
    [3],         # 7
    [4, 9, 12],         # 8
    [8, 10],         # 9
    [6, 9, 11, 14],         # 10
    [10],         # 11
    [8],         # 12
    [],         # 13
    [10, 15],         # 14
    [14]          # 15
]


res = []
#res = dfs(graph, 0)
print(res)
st = [0, 12, 3]
i = 0
for point in st:
    res = dfs(graph, point)
    i += 1
    if res[14]:
        print(f'Из точки S-{i} можно дойти до финиша')
    else:
        print(f'Из точки S-{i} нельзя дойти до финиша')
