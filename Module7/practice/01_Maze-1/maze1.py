# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    # список смежности
    [1],         # 0
    [0, 5],   # 1
    [6],         # 2
    [7],      # 3
    [5, 8],         # 4
    [1,4],      # 5
    [2, 10],            # 6
    [3],             # 7
    [4, 9, 12],             # 8
    [8, 10],             # 9
    [9, 6, 11, 14],             # 10
    [10],             # 11
    [8],             # 12
    [],             # 13
    [10, 15],             # 14
    [14],             # 15
]

# Решите задачу и выведите ответ в нужном формате


# start = [
#     {"name":"S-1",
#      "dot" : 0},
#     {"name": "S-2",
#      "dot": 12},
#     {"name": "S-3",
#      "dot": 3}
#      ]

start = {
    "s-1": 0,
    "s-2": 12,
    "s-3": 3
}
finish = 7


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


