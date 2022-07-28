# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
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


def Calc(p_start):
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


points = {'S-1': 0, 'S-2': 12, 'S-3': 3, 'F': 14}

for key, value in points.items():
    if key != 'F':
        result = Calc(value)

        if result[points['F']] is not None:
            print(f"Из точки {key} можно дойти до финиша")
        else:
            print(f"Из точки {key} нельзя дойти до финиша")

