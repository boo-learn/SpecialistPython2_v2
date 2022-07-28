graph = [
    [1],             # 0
    [0, 5],          # 1
    [6],             # 2
    [7],             # 3
    [8],             # 4
    [1],             # 5
    [2, 10],         # 6
    [3, 11],         # 7
    [4, 9, 12],      # 8
    [8, 10],         # 9
    [6, 9],          # 10
    [7, 15],         # 11
    [8],             # 12
    [],              # 13
    [],              # 14
    [11]             # 15
]


def bfs(gr, start):
    lengths = [None] * (len(gr))
    lengths[start] = start
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in gr[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)

    return lengths


def check_reachability(gr, start, finish, key_locs):
    visited_points = bfs(gr, start)

    if visited_points[finish] is not None:
        return "можно добраться до финиша без ключа"

    # Проверяем сумели ли мы собрать ключ
    key_collected = False
    for key in key_locs:
        if visited_points[key] is not None:
            key_collected = True
            break

    # Если ключей не собрали и не сумели дойти до финиша, значит дойти нереально
    if not key_collected and visited_points[finish] is None:
        return "нельзя добраться до финиша"

    graph_no_doors = [
        [1],  # 0
        [0, 5],  # 1
        [6],  # 2
        [7],  # 3
        [5, 8],  # 4
        [1, 4],  # 5
        [2, 10],  # 6
        [3, 11],  # 7
        [4, 9, 12],  # 8
        [8, 10],  # 9
        [6, 9],  # 10
        [7, 15],  # 11
        [8, 13],  # 12
        [12],  # 13
        [15],  # 14
        [11, 14]  # 15
    ]
    # Если собрали ключ, значит можем открыть все двери
    visited_points = bfs(graph_no_doors, start)
    if visited_points[finish] is not None:
        return "можно добраться до финиша, используя ключ"

    return "нельзя добраться до финиша"


key_locations = [7, 10]

finish_point = 0
s1_start = 5
print(f"Из точки S-1 {check_reachability(graph, s1_start, finish_point, key_locations)}")

s2_start = 13
print(f"Из точки S-2 {check_reachability(graph, s2_start, finish_point, key_locations)}")

s3_start = 3
print(f"Из точки S-3 {check_reachability(graph, s3_start, finish_point, key_locations)}")

s4_start = 8
print(f"Из точки S-4 {check_reachability(graph, s4_start, finish_point, key_locations)}")
