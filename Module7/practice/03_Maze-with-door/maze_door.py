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


def open_door(gr, start, visited_points, door_loc):
    # Открываем дверь и проверяем, можем ли мы дойти до финиша
    door_entrance = door_loc[0]
    door_exit = door_loc[1]

    if visited_points[door_entrance] is not None or visited_points[door_exit] is not None:
        gr[door_entrance].append(door_exit)
        gr[door_exit].append(door_entrance)

        return bfs(gr, start)

    return visited_points


def check_reachability(gr, start, finish, key_locs, door_locs):
    visited_points = bfs(gr, start)

    if visited_points[finish] is not None:
        return "можно добраться до финиша без ключа"

    # Проверяем сколько ключей мы сумели собрать
    keys_collected = 0
    for key in key_locs:
        if visited_points[key] is not None:
            keys_collected += 1

    # Если ключей не собрали и не сумели дойти до финиша, значит дойти нереально
    if keys_collected == 0 and visited_points[finish] is None:
        return "нельзя добраться до финиша"

    # Если собрали ключ, значит можем открыть все двери, открываем
    new_visited = visited_points
    for door in door_locs:
        door_entrance = door[0]
        door_exit = door[1]
        # Если смогли достигнуть хоть одной двери, открываем
        if new_visited[door_entrance] is not None or new_visited[door_exit] is not None:
            new_visited = open_door(gr, start, new_visited, door)

    if new_visited[finish] is not None:
        return "можно добраться до финиша, используя ключ"

    return "нельзя добраться до финиша"


door_locations = [
    (4, 5),
    (12, 13),
    (14, 15)
]

key_locations = [7, 10]

finish_point = 0
s1_start = 5
print(f"Из точки S-1 {check_reachability(graph, s1_start, finish_point, key_locations, door_locations)}")

s2_start = 13
print(f"Из точки S-2 {check_reachability(graph, s2_start, finish_point, key_locations, door_locations)}")

s3_start = 3
print(f"Из точки S-3 {check_reachability(graph, s3_start, finish_point, key_locations, door_locations)}")

s4_start = 8
print(f"Из точки S-4 {check_reachability(graph, s4_start, finish_point, key_locations, door_locations)}")

