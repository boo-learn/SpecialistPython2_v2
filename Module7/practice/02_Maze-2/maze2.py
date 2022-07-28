# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph1 = [
    # список смежности
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


graph2 = [
    # список смежности
    [1],  # 0
    [0, 2],  # 1
    [1,3],  # 2
    [2,7],  # 3
    [5],  # 4
    [4,6],  # 5
    [5],  # 6
    [3,11],  # 7
    [9, 12],  # 8
    [8, 10],  # 9
    [ 9, 11],  # 10
    [7,10,15],  # 11
    [8,13],  # 12
    [12,14],  # 13
    [13],  # 14
    [11]  # 15
]


def Calc(p_start,graph):
    start = p_start
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


points = {'S-1': 1, 'S-2': 5, 'S-3': 15, 'F': 14}

for key, value in points.items():
    if key != 'F':
        result = Calc(value,graph2)

        if result[points['F']] is not None:
            print(f"Из точки {key} можно дойти до финиша")
        else:
            print(f"Из точки {key} нельзя дойти до финиша")

