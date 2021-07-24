# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.

# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md

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

keys = [7, 10]
key_flag = False
start_points = {'S-1': 5, 'S-2': 13, 'S-3': 3,  'S-4': 8}
finish = 0
for item in start_points.items():
    if bts(graph_1, item[1])[finish] is not None:
        print(f'Из точки {item[0]} можно дойти до финиша без ключа')
        continue
    for el in keys:
        if bts(graph_1, item[1])[el] is not None:
            key_flag = True
    if key_flag:
        if bts(graph_2, item[1])[finish] is not None:
            print(f'Из точки {item[0]} можно дойти до финиша используя ключ')
            continue
    print(f'Из точки {item[0]} нельзя дойти до финиша')

# Решите задачу и выведите ответ в нужном формате
