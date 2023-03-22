# Скопируйте решение из предыдущей задачи и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи


# Решите задачу и выведите ответ в нужном формате
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
    # список смежности
    [1],  # 0
    [0, 4],  # 1
    [5],  # 2
    [4, 6],  # 3
    [1, 3, 5],  # 4
    [2, 4],  # 5
    [3],  # 6
    [8],  # 7
    [7]  # 8
]
visited = dfs(graph, start_vertex=0)
print(visited)

lengths = bfs(graph, start_vertex=0)
print(lengths)
