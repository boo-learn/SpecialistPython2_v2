def dfs(start_point, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                _dfs(w)

    _dfs(start_point)
    return visited


def max_treasure(start_points, treasure_dict):
    sorted_tuples = sorted(treasure_dict.items(), key=lambda x: x[1], reverse=True)
    treasure_dict_sorted = dict(sorted_tuples)
    for pointname, point in start_points.items():
        picked_treasures = []
        for cell in list(treasure_dict_sorted.keys()):
            if dfs(point, graph)[cell] and len(picked_treasures) < 2:
                picked_treasures.append(treasure_dict_sorted[cell])
        print(f'Из точки {pointname} можно собрать сокровищ суммарной ценностью {sum(picked_treasures)}')


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
    [6, 9, 14],  # 10
    [7],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15
]
start_points = {'S-1': 0, 'S-2': 12, 'S-3': 3}
treasures = {0: 0, 1: 1, 2: 2, 3: 0, 4: 3, 5: 0, 6: 5, 7: 3, 8: 0, 9: 5, 10: 3, 11: 0, 12: 0, 13: 8, 14: 4, 15: 7}
max_treasure(start_points, treasures)
# Решите задачу и выведите ответ в нужном формате
