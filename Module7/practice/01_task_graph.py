graph = [
    # список смежности
    [1],  # 0
    [4, 2, 0],  # 1
    [1, 3, 4],  # 2
    [2],  # 3
    [1, 2, 5, 6],  # 4
    [4],  # 5
    [4, 7, 8],  # 6
    [6],  # 7
    [6],  # 8
    [10],  # 10
    [9],  # 9
]


def start_bfs(start):
    lengths = [None] * (len(graph))
    lengths[start] = start
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    return lengths


start_point = 7
finish_point = 8
lengths = start_bfs(start_point).copy()
if lengths[finish_point]:
    print(f"Из точки {start_point} можно дойти до точки {finish_point}")
else:
    print(f"Из точки {start_point} нельзя дойти до точки {finish_point}")
