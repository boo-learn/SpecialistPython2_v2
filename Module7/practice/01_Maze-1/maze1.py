# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [4, 1],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15

]

# Решите задачу и выведите ответ в нужном формате

starts = {
    "s 1": 0,
    "s 2": 12,
    "s 3": 3}
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
         print (f"Из точки {key} можно дойти до финиша")
     elif lengths[value] == None:
         print(f"Из точки {key} нельзя дойти до финиша")


# S-1,S-2,S-3 - точки старта
# Определите: Из каких точек можно дойти до финиша(F), а из каких нет.


print(lengths)
