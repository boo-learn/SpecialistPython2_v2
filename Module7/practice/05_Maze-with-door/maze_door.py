# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


# Решите задачу и выведите ответ в нужном формате
import copy


def dfs(graph: list, start_point: int) -> list[bool]:
    """
    Алгоритм поиска в глубину
    """
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


def labyrinth_with_doors(
        rooms: dict,
        finish_point: int,
        keys: list,
        rooms_closed_doors: list[list[int]],
        rooms_open_doors: list[list[int]]) -> list[str]:
    messages = []
    for room, point in rooms.items():
        opened_with_keys = False
        visited = dfs(rooms_closed_doors, start_point=point)
        if visited[finish_point]:
            messages.append(f"Из точки {room} можно добраться до финиша без ключа")
            continue
        for key in keys:
            if visited[key]:
                visited = dfs(rooms_open_doors, start_point=point)
                opened_with_keys = True
        if visited[finish_point] and opened_with_keys:
            messages.append(f"Из точки {room} можно добраться до финиша, используя ключ")
        else:
            messages.append(f"Из точки {room} нельзя добраться до финиша")
    return messages


def change_layout(rooms: list[list[int]], opening: list[tuple]) -> list[list[int]]:
    changed_rooms = copy.deepcopy(rooms)
    for point1, point2 in opening:
        changed_rooms[point1].append(point2)
        changed_rooms[point2].append(point1)
    return changed_rooms


def test_labyrinth_with_doors():
    finish_point = 0
    keys = [7, 10]
    doors = [(4, 5), (12, 13), (14, 15)]
    rooms = {
        "S-1": 5,
        "S-2": 13,
        "S-3": 3,
        "S-4": 8
    }
    rooms_closed_doors = [
        # список смежности
        [1],  # 0
        [0, 5],  # 1
        [6],  # 2
        [7],  # 3
        [8],  # 4
        [1],  # 5
        [2, 10],  # 6
        [3, 11],  # 7
        [4, 9, 12],  # 8
        [8, 10],  # 9
        [6, 9],  # 10
        [7, 15],  # 11
        [8],  # 12
        [],  # 13
        [],  # 14
        [11],  # 15
    ]
    rooms_open_doors = change_layout(rooms_closed_doors, doors)

    # Example case
    messages = labyrinth_with_doors(rooms, finish_point, keys, rooms_closed_doors, rooms_open_doors)
    assert messages == [
        'Из точки S-1 можно добраться до финиша без ключа',
        'Из точки S-2 нельзя добраться до финиша',
        'Из точки S-3 нельзя добраться до финиша',
        'Из точки S-4 можно добраться до финиша, используя ключ'
    ]

    # Case delete key 10
    keys_del_10 = keys[:1]
    messages = labyrinth_with_doors(rooms, finish_point, keys_del_10, rooms_closed_doors, rooms_open_doors)
    assert messages == [
        'Из точки S-1 можно добраться до финиша без ключа',
        'Из точки S-2 нельзя добраться до финиша',
        'Из точки S-3 нельзя добраться до финиша',
        'Из точки S-4 нельзя добраться до финиша'
    ]

    # Case delete wall 1-2
    deleted_wall = [(1, 2)]
    rooms_closed_doors_del_wall_1_2 = change_layout(rooms_closed_doors, deleted_wall)
    rooms_open_doors_del_wall_1_2 = change_layout(rooms_open_doors, deleted_wall)
    messages = labyrinth_with_doors(
        rooms,
        finish_point,
        keys,
        rooms_closed_doors_del_wall_1_2,
        rooms_open_doors_del_wall_1_2)
    assert messages == [
        'Из точки S-1 можно добраться до финиша без ключа',
        'Из точки S-2 нельзя добраться до финиша',
        'Из точки S-3 нельзя добраться до финиша',
        'Из точки S-4 можно добраться до финиша без ключа'
    ]

    # Case add key 13
    keys_add_13 = copy.deepcopy(keys)
    keys_add_13.append(13)
    messages = labyrinth_with_doors(
        rooms,
        finish_point,
        keys_add_13,
        rooms_closed_doors,
        rooms_open_doors)
    assert messages == [
        'Из точки S-1 можно добраться до финиша без ключа',
        'Из точки S-2 можно добраться до финиша, используя ключ',
        'Из точки S-3 нельзя добраться до финиша',
        'Из точки S-4 можно добраться до финиша, используя ключ'
    ]
