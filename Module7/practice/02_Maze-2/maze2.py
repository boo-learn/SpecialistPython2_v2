def dfs(graph, start_vertex):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


def bfs(graph, start_vertex):
    lengths = [None] * len(graph)
    lengths[start_vertex] = 0
    queue = [start_vertex]

    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    return lengths

graph = [
    [1, 3],     # 0
    [0, 4],     # 1
    [5],        # 2
    [0, 4, 6],  # 3
    [1, 3],     # 4
    [2, 8],     # 5
    [3],        # 6
    [8],        # 7
    [7, 5],     # 8
]


start_vertex = 7
bank = 2

lengths = bfs(graph, start_vertex=start_vertex)
print(lengths)

if lengths[bank] == None:
    print("Мы не придем в Банк")
else:
    print("Мы придем в банк")
