# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.

def bfs(graph, start_vertex):
    start = start_vertex
    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)

    return lengths


def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)

    return visited


graph = [
    [1, 4],  # 0
    [0, 2],  # 1
    [1],  # 2
    [7],  # 3
    [0],  # 4
    [6, 9],  # 5
    [5, 10],  # 6
    [3, 11],  # 7
    [9, 12],  # 8
    [5, 8, 10],  # 9
    [9, 6, 14],  # 10
    [7],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14]  # 15
]

points_start = [{'name': 'S-1', 'vertex': 0}, {'name': 'S-2', 'vertex': 12}, {'name': 'S-3', 'vertex': 3}]
treasures = {1: 1, 2: 2, 4: 3, 6: 5, 7: 3, 9: 5, 10: 3, 13: 8, 14: 4, 15: 7}

for start in points_start:
    vertex_available = dfs(graph, start['vertex'])
    found_treasure = [treasures[vt] for vt in treasures if vertex_available[vt]]
    found_treasure.sort(reverse=True)
    print(f"Из точки {start['name']} можно собрать сокровищ суммарной ценностью {sum(found_treasure[:2])}")
