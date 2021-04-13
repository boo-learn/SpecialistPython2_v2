# "Лабиринт с ключем"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - стартовые точки
# Посетив клетку K, можно подобрать ключ, который отпирают любую дверь.
# Определите:
# Из каких точек можно добраться до точки F?
# Какую дверь нужно открыть, чтобы добраться до точки P-2?

# Схема лабиринта
#
# (x)   - номер узла
# [D-x] - двери
# P-x   - стартовая точка
# K     - ключ от дверей
# F     - финиш
#
# --------------------------------|
# (7)P-5 (8)F |            (6)P-6 |
#       ------|     |-------------|
#   (9)[D-1]        |     (10)P-3 |
# ------------|     |     |-------|
#      (5)P-2 |     |     | (0)K  |
# -(4)[D-2]---| (1) |     |       |
#                   |     |       |
#        |----|     |-----|       |
# (3)P-1 |     (2)P-4             |
# -------|------------------------|

labyrinth_closed = [
    [2],        # 0
    [2, 3, 6],  # 1
    [0, 1],     # 2
    [1],        # 3
    [5],        # 4
    [4],        # 5
    [1],        # 6
    [8],        # 7
    [7],        # 8
    [],         # 9
    [],         # 10
]
labyrinth_opened = [
    [2],                # 0
    [2, 3, 4, 6, 9],    # 1
    [0, 1],             # 2
    [1],                # 3
    [1, 5],             # 4
    [4],                # 5
    [1],                # 6
    [8, 9],             # 7
    [7],                # 8
    [1, 7],             # 9
    [],                 # 10
]


def find_a_way(start=0, finish=0, graph=[], check_all=False):
    visited = [False] * (len(graph))
    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                dfs(w)
    dfs(start)
    if check_all:
        return visited
    return visited[finish]


def find_winners(runners: list, open_graph: list, closed_graph: list, key: int, finish: int) -> str:
    """Получает список игроков, графы с дверьми и без, номер узла ключа и финиша, возвращает строку с результатом"""
    res = ''
    for runner in runners:
        # проверяем пути
        key_found = find_a_way(runner['point'], key, closed_graph)
        if key_found:
            finished_with_key = find_a_way(key, finish, open_graph)
        finished_without_key = find_a_way(runner['point'], finish, closed_graph)

        # проверяем результаты
        if finished_without_key:
            res += f"{runner['name']} добрался до финиша сразу\n"
        elif key_found and finished_with_key:
            res += f"{runner['name']} нашел ключ и добрался до финиша\n"
        elif key_found and not finished_with_key:
            res += f"{runner['name']} нашел ключ, но не добрался до финиша\n"
        else:
            res += f"{runner['name']} не нашел ключ и не добрался до финиша\n"
    return res


def find_a_right_door(doors: list, point, graph):
    res = ''
    for door in doors:
        if find_a_way(door['point'], point, graph):
            res += f"{door['name']} ведёт к искомой точке"
    return res


if __name__ == '__main__':
    runners = [
        {'name': 'P-1', 'point': 3},
        {'name': 'P-2', 'point': 5},
        {'name': 'P-3', 'point': 10},
        {'name': 'P-4', 'point': 2},
        {'name': 'P-5', 'point': 7},
        {'name': 'P-6', 'point': 6},
    ]
    k = 0
    f = 8
    print(find_winners(runners=runners, key=k, finish=f, open_graph=labyrinth_opened, closed_graph=labyrinth_closed))

    doors = [
        {'name': 'D-1', 'point': 9},
        {'name': 'D-2', 'point': 4},
    ]
    f = 5
    print(find_a_right_door(doors=doors, point=f, graph=labyrinth_closed))
