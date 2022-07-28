
def dfs(start_point, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited

def dif_graphs(graph, doors):
  '''разница графов - на выходе граф с удаленными связами на месте дверей'''
    i = 0
    for inner_lists in graph:
        inner_list_diff = []
        for el in inner_lists:
            if el not in doors[i]:
                inner_list_diff.append(el)
        graph_with_doors.insert(i, inner_list_diff)
        i += 1
        inner_list_diff = []
    return graph_with_doors

graph = [
    [4],  # 0
    [2],  # 1
    [1, 3],  # 2
    [2],  # 3
    [0, 5],  # 4
    [4, 6, 9],  # 5
    [5, 7],  # 6
    [6],  # 7
    [],  # 8
    [5, 13],  # 9
    [11, 14],  # 10
    [10],  # 11
    [13],  # 12
    [9, 12, 14],  # 13
    [10, 13, 15],  # 14
    [14]  # 15
]

doors = [  # двери могут быть односторонними, прописываем обе стороны
    [],  # 0
    [],  # 1
    [],  # 2
    [],  # 3
    [5],  # 4
    [4],  # 5
    [],  # 6
    [],  # 7
    [],  # 8
    [],  # 9
    [],  # 10
    [],  # 11
    [13],  # 12
    [12],  # 13
    [15],  # 14
    [14]  # 15
]

graph_with_doors = []

keys = [7, 10]

start_points = {
    3: "S-3",
    4: "S-5",  # хоть одна точка старта, из которой финиш доступен без ключа
    5: "S-1",
    8: "S-4",
    13: "S-2",
}

finish_point = 0

graph_with_doors = dif_graphs(graph, doors)

for vertex, point_name in start_points.items():
    visited = dfs(vertex, graph_with_doors)
    if visited[finish_point]:
                print(f"Из точки {point_name} можно дойти до финиша без ключа")
    else:
        visited = dfs(vertex, graph)
        if visited[finish_point]: # здесь нужно добавить проверку на доступность ключа
            print(f"Из точки {point_name} можно дойти до финиша, используя ключ")
        else:
            print(f"Из точки {point_name} нельзя дойти до финиша")
