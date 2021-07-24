# Сюда отправляем решение задачи "Лабиринт с сокровищами"
# Решите задачу и выведите ответ в нужном формате
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


graph = [
    [1, 4],             # 0
    [0, 2],             # 1
    [1],                # 2
    [7],                # 3
    [0],                # 4
    [6, 8, 9],          # 5
    [5, 10],            # 6
    [3, 11],            # 7
    [9, 12],            # 8
    [5, 8, 10],         # 9
    [6, 9, 14],         # 10
    [7],                # 11
    [8],                # 12
    [],                 # 13
    [10, 15],           # 14
    [14]                # 15
]

treasure = [0, 1, 2, 0, 3, 0, 5, 3, 0, 5, 3, 0, 0, 8, 4, 7]
treasure_limit = 2
start_points = {'S-1': 0, 'S-2': 12, 'S-3': 3}
treasure_collected = []
for item in start_points.items():
    treasure_collected.clear()
    i = 0
    while i < len(bts(graph, item[1])):
        if bts(graph, item[1])[i] is not None:
            treasure_collected.append(treasure[i])
        i += 1
    treasure_collected.sort()
    max_treasure = sum(treasure_collected[-2:])
    print(f'Максимальная ценность сокровищ при движении из точки {item[0]} составляет {max_treasure}')
