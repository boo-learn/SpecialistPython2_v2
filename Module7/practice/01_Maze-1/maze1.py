# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    ...
]

# Решите задачу и выведите ответ в нужном формате
graph = [
    # список смежности
    [1],  # 0
    [0, 4],  # 1
    [5],  # 2
    [4, 6],  # 3
    [3, 5, 1],  # 4
    [2, 4],  # 5
    [3],  # 6
    [8],  # 7
    [7]  # 8
]
start = 0
lengths = [None] * len(graph)
lengths[start] = 0
queue = [start]
while queue:
    cur_vertex = queue.pop(0)
    for vertex in graph[cur_vertex]:
        if lengths[vertex] is None:
            lengths[vertex] = lengths[cur_vertex] + 1
            queue.append(vertex)

print(lengths)
