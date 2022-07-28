# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],        #0
    [0, 5],     #1
    [6],        #2
    [7],        #3
    [5, 8],     #4
    [1, 4],     #5
    [2, 10],    #6
    [3],        #7
    [4, 9, 12], #8
    [8, 10],     #9
    [6, 11, 14, 9], #10
    [10],     #11
    [8],      #12
    [],       #13
    [15, 10], #14
    [14]      #15

]

# Решите задачу и выведите ответ в нужном формате

possible_starts = {'S-1':0, 'S-2':12, 'S-3':3}
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




