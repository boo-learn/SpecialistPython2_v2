# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14]  # 15
]

# Решите задачу и выведите ответ в нужном формате
s = int(input(f"Введите стартовую точку от 0 до {len(graph)-1} :"))
f = int(input(f"Введите финишную точку от 0 до {len(graph)-1} :"))
start = s
finish = f
lengths = [None] * (len(graph))
lengths[start] = 0
queue = [start]
while queue:
    cur_vertex = queue.pop(0)
    for vertex in graph[cur_vertex]:
        if lengths[vertex] is None:
            lengths[vertex] = lengths[cur_vertex] + 1
            queue.append(vertex)
print(lengths)

if lengths[finish]:
    print(f"Из точки {start} можно дойти до финишной точки {finish}")
else:
    print(f"Из точки {start} нельзя дойти до финишной точки {finish}")
