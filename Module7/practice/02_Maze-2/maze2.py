# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    # список смежности
    [1],         # 0
    [0, 2],   # 1
    [1, 3],         # 2
    [2, 7],      # 3
    [5],         # 4
    [4, 6],      # 5
    [5],            # 6
    [3, 11],             # 7
    [9, 12],             # 8
    [8, 10],             # 9
    [9, 11],             # 10
    [7, 10, 15],             # 11
    [8, 13],             # 12
    [12, 14],             # 13
    [13],             # 14
    [11],             # 15
]

# Решите задачу и выведите ответ в нужном формате


start = {
    "s-1": 1,
    "s-2": 5,
    "s-3": 14
}
finish = 15


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
    visited = bts(graph, vertex)
    if visited[finish]:
        print(f'Из точки {point_name} можно дойти до финиша')
    else:
        print(f'Из точки {point_name} нельзя дойти до финиша')


