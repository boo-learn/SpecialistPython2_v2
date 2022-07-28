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
    [14],  # 15
]
print(f'введите точку финиша')
finish = int(input())

points = {
    's-1': 0,
    's-2': 0,
    's-3': 0,

}
bfs_list = bfs(graph,finish)

for point in points:
    
    print(f'введите точку {point} (0-15):')
    f = int(input())
    if 15 < f <= 0:
        print('сказано от 0 до 15')
    else:
        points.__setitem__(point, f)
        s = points[point]
        if bfs_list[s] is not None:
            print(f'Из точки {point} можно добраться до финиша ({finish})')
        else:
            print(f'Из точки {point} нельзя добраться до финиша ({finish})')



