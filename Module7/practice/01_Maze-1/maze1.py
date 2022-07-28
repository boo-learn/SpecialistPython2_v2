# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],  # 0
    [0, 5],
    [6],
    [7],
    [5, 8],
    [1, 4],
    [2, 10],
    [3],
    [4, 9, 12],
    [8, 10],
    [6, 9, 11, 14],  # 10
    [10],
    [8],
    [],
    [10, 15],
    [14]
]


def bfs(start, finish):
    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                if vertex == finish:
                    return True
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    return False


points_start = [{'name': 'S-1', 'vertex': 0}, {'name': 'S-2', 'vertex': 12}, {'name': 'S-3', 'vertex': 3}]
point_finish = {'name': 'F', 'vertex': 14}

for start in points_start:
    if bfs(start['vertex'], point_finish['vertex']):
        print(f"Из точки {start['name']} можно дойти до финиша")
    else:
        print(f"Из точки {start['name']} нельзя дойти до финиша")
