# Сюда отправляем решение задачи "Лабиринт с сокровищами"


def dfs(v, graph):
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    visited = [False] * (len(graph))
    _dfs(v)
    return visited


graph = [
    # список смежности
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
    [6, 9, 14],  # 10
    [7],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14]  # 15
]

treasure = [
    [],  # 0
    [1],  # 1
    [2],  # 2
    [],  # 3
    [3],  # 4
    [],  # 5
    [5],  # 6
    [3],  # 7
    [],  # 8
    [5],  # 9
    [3],  # 10
    [],  # 11
    [],  # 12
    [8],  # 13
    [4],  # 14
    [7]  # 15
]
start_points = {0: 'S-1', 12: 'S-2', 3: 'S-3'}

for start_point in start_points.keys():
    visited = dfs(start_point, graph)
    values = []
    for i, is_visited in enumerate(visited):
        if is_visited and treasure[i]:
            values.append(treasure[i][0])
    values.sort(reverse=True)
    print(f'Из точки {start_points[start_point]} можно собрать сокровищ суммарной ценностью {sum(values[:2])}')
