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
    0,  # 0
    1,  # 1
    2,  # 2
    0,  # 3
    3,  # 4
    0,  # 5
    5,  # 6
    3,  # 7
    0,  # 8
    5,  # 9
    3,  # 10
    0,  # 11
    0,  # 12
    8,  # 13
    4,  # 14
    7  # 15
]


def Calc(p_start, graph):
    start = p_start
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


points = {'S-1': 0, 'S-2': 12, 'S-3': 3}

for key, value in points.items():

    result = Calc(value, graph)

    treasure_list = []

    for idx, way in enumerate(result):
        if way is not None and treasure[idx] > 0:
            treasure_list.append(treasure[idx])
    treasure_list.sort(reverse=True)

    print(f"Из точки {key} можно собрать сокровищ суммарной ценностью {sum(treasure_list[0:2])}")
