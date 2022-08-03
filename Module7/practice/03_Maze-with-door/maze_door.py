def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


graph_closed_doors = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 12, 9],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11],  # 15
]

graph_open_doors = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8, 5],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 12, 9],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [12],  # 13
    [15],  # 14
    [14, 11],  # 15
]
# print (graph_closed_doors)
# print (graph_open_doors)

starts = {'S-1': 5, 'S-2': 6, 'S-3': 3}
finish = 0

keys = {'K-1': 7, "K-2": 10}

result = dfs(graph_open_doors, finish)

# for point_name, point_value in starts.items():
#     if result[point_value]:
#         print(f'Из точки {point_name} по открытому графу можно дойти до финиша')
#     else:
#         print(f'Из точки {point_name} по открытому графу нельзя дойти до финиша')

result_closed = dfs(graph_closed_doors, finish)
result_open = dfs(graph_open_doors, finish)

for point_name, point_value in starts.items():
    if result_closed[point_value]:
        print(f'Из точки ({point_name}:{point_value}) по закрытому графу можно дойти до финиша без ключа')
    else:
        if result_open[point_value]:
            for key_point_name, key_point_value in keys.items():
                result1 = dfs(graph_closed_doors, key_point_value)
                if result[key_point_value]:
                    print(f'Из точки ({point_name}:{point_value}) по закрытому графу можно дойти до финиша c ключом')
        else:
            print(f'Из точки ({point_name}:{point_value}) по закрытому графу нельзя дойти до финиша')
