# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи


# Решите задачу и выведите ответ в нужном формате
graph = [
    # список смежности
    [1, 3],  # 0
    [0, 4],  # 1
    [5],  # 2
    [0, 4, 6],  # 3
    [1, 3],  # 4
    [2, 8],  # 5
    [3],  # 6
    [8],  # 7
    [7, 5]  # 8
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
