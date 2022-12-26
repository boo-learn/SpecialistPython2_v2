# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.
# Решите задачу и выведите ответ в нужном формате

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
         [4, 9], [8, 10], [6], [7, 15],
         [8], [], [], [11]
         ]
start_points = [3, 8, 13]
finish_points = [0]
key_points = [7, 10]
doors = [(4, 5), (12, 13), (14, 15)]
doors_opened = False

for start in start_points:
    cur_graph = graph.copy()
    can_visited = dfs(graph, start)
    # проверяем доступность ключей
    for key in key_points:
        if can_visited[key]:
            doors_opened = True
            break
    # открываем все двери
    if doors_opened:
        for door in doors:
            cur_graph[door[0]].append(door[1])
            cur_graph[door[1]].append(door[0])
        can_visited_with_doors = dfs(cur_graph, start)
    # проверяем доступность путей с ключами и без
    for finish in finish_points:
        if can_visited[finish]:
            print(f'Из точки S-{start} можно добраться до финиша ({finish}) без ключа')
        elif doors_opened and can_visited_with_doors[finish]:
            print(f'Из точки S-{start} можно добраться до финиша ({finish}) с помощью ключа')
        else:
            print(f'Из точки S-{start} нельзя добраться до финиша ({finish})')
