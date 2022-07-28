maze_graph = [
    # список смежности
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [12],  # 13
    [15],  # 14
    [11, 14]  # 15
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


def GetFreeGraph(p_src_graph, p_graph):
    res_graph = []
    for idx, vertexes in enumerate(p_src_graph):
        new_vertexes = []
        for vertex in vertexes:
            if (idx, vertex) not in p_graph and (vertex, idx) not in p_graph:
                new_vertexes.append(vertex)
        res_graph.append(new_vertexes)

    return res_graph


points = {'S-1': 5, 'S-2': 13, 'S-3': 3, 'S-4': 8, 'F': 0}
doors = [(4, 5), (12, 13), (14, 15)]
keys = [7, 10]

free_graph = GetFreeGraph(maze_graph, doors)
door_result = Calc(points['F'], maze_graph)



for key, value in points.items():
    if key != 'F':

        free_result = Calc(points[key], free_graph)
        
        have_key = False  # check for KEY

        for fkey in keys:
            if free_result[fkey] is not None:
                have_key = True
                break

        if free_result[points['F']] is not None:
            print(f"Из точки {key} можно дойти до финиша без ключа")
        else:
            if have_key and door_result[points['F']] is not None:
                print(f"Из точки {key} можно дойти до финиша c ключем")
            else:
                print(f"Из точки {key} нельзя дойти до финиша")
