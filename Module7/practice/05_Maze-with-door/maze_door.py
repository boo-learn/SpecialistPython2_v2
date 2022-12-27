# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.
# Решите задачу и выведите ответ в нужном формате
from copy import deepcopy


def dfs(graph, start_point):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


graph = [[1], [0, 5], [6], [7],
         [8], [1], [2, 10], [3, 11],
         [4, 9, 12], [8, 10], [6, 9], [7, 15],
         [8], [], [], [11]
         ]
start_points = {'S-1': 5,
                'S-2': 13,
                'S-3': 3,
                'S-4': 8,
                }
finish_points = {'F': 0, }
key_points = [7, 10]
doors = [(4, 5), (12, 13), (14, 15)]

for start_name, start in start_points.items():
    doors_opened = False
    # делаем копию оригинального списка, чтобы не внести в него изменения при открытии дверей (просто .copy не сработало)
    cur_graph = deepcopy(graph)
    can_visited = dfs(graph, start)
    # проверяем доступность ключей
    for key in key_points:
        if can_visited[key]:
            doors_opened = True
            break
    # открываем все двери
    if doors_opened:
        for door in doors:
            room1, room2 = door
            cur_graph[room1].append(room2)
            cur_graph[room2].append(room1)
        can_visited_with_doors = dfs(cur_graph, start)
    # проверяем доступность путей с ключами и без
    for finish_name, finish in finish_points.items():
        if can_visited[finish]:
            result = 'можно добраться без ключа'
        elif doors_opened and can_visited_with_doors[finish]:
            result = 'можно добраться с помощью ключа'
        else:
            result = 'нельзя добраться'
        print(f'Из точки {start_name}({start}) {result} до финиша {finish_name}({finish})')
