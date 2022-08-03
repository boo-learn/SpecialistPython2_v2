# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


graph_with_doors = [
    [1],             # 0
    [0, 5],          # 1
    [6],             # 2
    [7],             # 3
    [8],             # 4
    [1],             # 5
    [2, 10],         # 6
    [3, 11],         # 7
    [4, 9, 12],      # 8
    [8, 10],         # 9
    [6, 9],          # 10
    [7, 15],         # 11
    [8],             # 12
    [],              # 13
    [],              # 14
    [11],            # 15
]

graph_without_doors = [
    [1],             # 0
    [0, 5],          # 1
    [6],             # 2
    [7],             # 3
    [5, 8],          # 4
    [1, 4],          # 5
    [2, 10],         # 6
    [3, 11],         # 7
    [4, 9, 12],      # 8
    [8, 10],         # 9
    [6, 9],          # 10
    [7, 15],         # 11
    [8, 13],         # 12
    [12],            # 13
    [15],            # 14
    [11, 14],        # 15
]

starts = {'S-1': 5, 'S-2': 13, 'S-3': 3, 'S-4': 8}
finish = 0
key1 = 7
key2 = 10
result_with_doors = dfs(graph_with_doors, finish)
result_without_doors = dfs(graph_without_doors, finish)
result_key1 = dfs(graph_with_doors, key1)
result_key2 = dfs(graph_with_doors, key2)

for point_name, point_value in starts.items():
    if result_with_doors[point_value]:
        print(f"Из точки {point_name} можно добраться до финиша без ключа")
    elif result_key1[point_value] or result_key2[point_value]:
        if result_without_doors[point_value]:
            print(f"Из точки {point_name} можно добраться до финиша, используя ключ")
        else:
            print(f"Из точки {point_name} нельзя добраться до финиша")
    else:
        print(f"Из точки {point_name} нельзя добраться до финиша")
