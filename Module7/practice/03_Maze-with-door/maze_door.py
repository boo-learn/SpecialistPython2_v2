graph_1 = [
    [1],                # 0
    [0, 5],             # 1
    [6],                # 2
    [7],                # 3
    [8],                # 4
    [1],                # 5
    [2, 10],            # 6
    [3, 11],            # 7
    [4, 9, 12],         # 8
    [8, 10],            # 9
    [6, 9],             # 10
    [7, 15],            # 11
    [8],                # 12
    [],                 # 13
    [],                 # 14
    [11]                # 15
]

graph_2 = [
    [1],                # 0
    [0, 5],             # 1
    [6],                # 2
    [7],                # 3
    [5, 8],             # 4
    [1, 4],             # 5
    [2, 10],            # 6
    [3, 11],            # 7
    [4, 9, 12],         # 8
    [8, 10],            # 9
    [6, 9],             # 10
    [7, 15],            # 11
    [8, 13],            # 12
    [12],               # 13
    [15],               # 14
    [11, 14]            # 15
]
# Решите задачу и выведите ответ в нужном формате

key = [7, 10]
found_key = False

start = {
    "s-1": 5,
    "s-2": 13,
    "s-3": 3,
    "s-4": 8

}


finish = 0


def bts(graph, start_point):
    start = start_point
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

for point_name, vertex in start.items():
    visited = bts(graph_1, vertex)
    if visited[finish]:
        print(f'Из точки {point_name} можно дойти до финиша , без ключа')
    for i in key:
        finding_key = bts(graph_1, vertex)
        if finding_key[i]:
            found_key = True
    if found_key == True:
        visited_key = bts(graph_2, vertex)
        if visited_key[finish]:
            print(f'Из точки {point_name} можно дойти до финиша , c ключом')
        else:
            print(f'Из точки {point_name} нельзя дойти до финиша')
