# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под текущий лабиринт
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи


# Решите задачу и выведите ответ в нужном формате
graph = [
    [1],        #0
    [0, 2],     #1
    [1, 3],     #2
    [2, 7],     #3   
    [5],        #4
    [6, 4],     #5
    [5],        #6   
    [3, 11],    #7    
    [9, 12],    #8    
    [8, 10],    #9
    [11, 9],   #10
    [10, 7, 15], #11
    [8, 13],    #12
    [12, 14],   #13
    [13],       #14
    [11]        #15

]

# Решите задачу и выведите ответ в нужном формате

possible_starts = {'S-1':1, 'S-2':5, 'S-3':15}
output = {} #словарь с вершинами + флаги можно/нельзя дойти до финиша
#start = 0 #параметризовать
finish = 14 #можно ввести свое значение
lengths = [None] * (len(graph))
for name, start in possible_starts.items():
    lengths[start] = 0
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    output[name] = bool(lengths[finish])
    #print(name, lengths)

for vertex, is_possible in output.items():
    print(f"Из вершины {vertex} {'можно' if is_possible else 'нельзя'} дойти до финиша")



