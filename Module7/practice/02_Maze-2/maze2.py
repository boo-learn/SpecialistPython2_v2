# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    # список смежности
    [1],            # 0
    [0, 2],         # 1
    [1, 3],         # 2
    [2, 7],         # 3
    [5],            # 4
    [4, 6],         # 5
    [5],            # 6
    [3,11],         # 7
    [9, 12],        # 8
    [8, 10],        # 9
    [9, 11],        # 10
    [7, 10, 15],    # 11
    [8, 13],        # 12
    [12, 14],       # 13
    [13],           # 14
    [11]            # 15
]

start_list = {"S-1": 1,"S-2": 5,"S-3": 15}

finish = 14

for start in start_list:

    lengths = [None] * (len(graph))
    lengths[start_list.get(start)] = 0
    queue = [start_list.get(start)]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    if lengths[finish] == None:
        print(f"Из точки {start} нельзя дойти до финиша")
    else:
        print(f"Из точки {start} можно дойти до финиша")
