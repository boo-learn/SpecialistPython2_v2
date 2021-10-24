# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под текущий лабиринт
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи


# Решите задачу и выведите ответ в нужном формате
graph = [
    [1],  # 0
    [1, 2],  # 1
    [1, 3],  # 2
    [2, 7],  # 3
    [5],  # 4
    [4, 6],  # 5
    [5],  # 6
    [3, 11],  # 7
    [9, 12],  # 8
    [8, 10],  # 9
    [9, 11],  # 10
    [10, 7, 15],  # 11
    [8, 13 ],  # 12
    [12,14],  # 13
    [13],  # 14
    [11],  # 15

]

# Решите задачу и выведите ответ в нужном формате

starts = {
    "s 1": 1,
    "s 2": 5,
    "s 3": 15}
finish = 14

lengths = [None] * (len(graph))
lengths[finish] = 0
queue = [finish]
while queue:
    cur_vertex = queue.pop(0)
    for vertex in graph[cur_vertex]:
        if lengths[vertex] is None:
            lengths[vertex] = lengths[cur_vertex] + 1
            queue.append(vertex)

value = int()
for key in starts:
    value = starts.get(f"{key}")
    if lengths[value] != None:
        print(f"Из точки {key} можно дойти до финиша")
    elif lengths[value] == None:
        print(f"Из точки {key} нельзя дойти до финиша")
