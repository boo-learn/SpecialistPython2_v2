start = 0


def bfs(graph: list, start= 0):

    lengths = [None] * (len(graph))
    lengths[start] = start
    queue = []
    queue.append(start)
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    return lengths



graph_closed = [
    # список смежности
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 12, 9],  # 8
    [8, 10],  # 9
    [6],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11],  # 15
]

print(f'введите точку финиша')
finish = int(input())

print(f'введите позицию 1 двери 1:')
door_1 = int(input())
print(f'введите позицию 2 двери 1:')
door_2 = int(input())
door = [door_1,door_2]





key_list = [10,7]

points = {
    's-1': 0,
    's-2': 0,
    's-3': 0,

}

bfs_list2 = []
for point in points:

    print(f'введите точку {point} (0-15):')
    f = int(input())
    if 15 < f <= 0:
        print('сказано от 0 до 15')
    else:

        points.__setitem__(point, f)
        #print(graph_closed)
        s = points[point]
        bfs_list = bfs(graph_closed, points[point])
        if bfs_list[finish] is None:
            for key in key_list:
                if bfs_list[key] is not None:

                    graph_closed[door_1].append(door_2)
                    graph_closed[door_2].append(door_1)
                    bfs_list2 = bfs(graph_closed,finish)
                    #print(bfs(graph_closed,finish))
                    if bfs_list2[s] is not None:
                        print(f'Из точки {point} можно добраться до финиша с ключом ({finish})')

                else:
                    print(f'Из точки {point} нельзя добраться до финиша ({finish})')
        else:
            print(f'Из точки {point} можно добраться до финиша ({finish})')



