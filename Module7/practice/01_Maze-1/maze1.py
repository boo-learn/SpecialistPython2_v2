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


graph = [
    [1],                # 0
    [0, 5],             # 1
    [6],                # 2
    [7],                # 3
    [5, 8],             # 4
    [1, 4],             # 5
    [2, 10],            # 6
    [3],                # 7
    [4, 9, 12],         # 8
    [8, 10],            # 9
    [6, 9, 11, 14],     # 10
    [10],               # 11
    [8],                # 12
    [],                 # 13
    [10, 15],           # 14
    [14]                # 15
]

start_points = {'S-1': 0, 'S-2': 12, 'S-3': 3}
finish = 14
for item in start_points.items():
    if bts(graph, item[1])[finish] is not None:
        print(f'Из точки {item[0]} можно дойти до финиша')
    else:
        print(f'Из точки {item[0]} нельзя дойти до финиша')


# Решите задачу и выведите ответ в нужном формате
