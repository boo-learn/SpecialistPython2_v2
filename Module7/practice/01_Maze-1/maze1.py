def bfs(start):
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


def possible_to_finish(start_points, finish_point):
    for start in start_points:
        possibilities = bfs(start['vertex'])
        if possibilities[finish_point['vertex']]:
            print(f"Из точки {start['name']} можно дойти до финиша")
        else:
            print(f"Из точки {start['name']} нельзя дойти до финиша")


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

start_points = [{'name': 'S-1', 'vertex': 0}, {'name': 'S-2', 'vertex': 12}, {'name': 'S-3', 'vertex': 3}]
finish_point = {'name': 'F', 'vertex': 14}

possible_to_finish(start_points, finish_point)
