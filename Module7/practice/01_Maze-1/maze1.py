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
    [1],        # 0
    [0, 4],     # 1
    [5],        # 2
    [4, 6],     # 3
    [1, 3, 5],  # 4
    [2, 4],     # 5
    [3],        # 6
    [8],        # 7
    [7],        # 8
]


start_vertex = 0
bank = 5

lengths = bfs(graph, start_vertex=start_vertex)
print(lengths)

if lengths[bank] == None:
    print("Мы не предем в Банк")
else:
    print("Мы придем в банк")
