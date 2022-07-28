# Сюда отправляем решение задачи "Лабиринт с сокровищами"
# Решите задачу и выведите ответ в нужном формате

import p as p

graph = [
    # список смежности
    [1, 4],  # 0
    [0, 2],  # 1
    [1],  # 2
    [7],  # 3
    [0],  # 4
    [6, 9],  # 5
    [5, 10],  # 6
    [3, 11],  # 7
    [9, 12],  # 8
    [5, 8, 10],  # 9
    [9, 6, 14],  # 10
    [7],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15
]

points = [
    {
        'name': 'S-1',
        'position': 0
    },
    {
        'name': 'S-2',
        'position': 12
    },
    {
        'name': 'S-3',
        'position': 3
    },
    {
        'name': 'T',
        'position': 1,
        'value': 1
    },
    {
        'name': 'T',
        'position': 2,
        'value': 2
    },
    {
        'name': 'T',
        'position': 4,
        'value': 3
    },
    {
        'name': 'T',
        'position': 6,
        'value': 5
    },
    {
        'name': 'T',
        'position': 7,
        'value': 3
    },
    {
        'name': 'T',
        'position': 9,
        'value': 5
    },
    {
        'name': 'T',
        'position': 10,
        'value': 3
    },
    {
        'name': 'T',
        'position': 13,
        'value': 8
    },
    {
        'name': 'T',
        'position': 14,
        'value': 4
    },
    {
        'name': 'T',
        'position': 15,
        'value': 7
    }
]


def dfs(v, _graph):
    visited[v] = True
    for w in _graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w, _graph)

def doors_open(_graf, key_colour):
    for doors in points:
        if doors['name'] == 'D':  # ищем список дверей, с ключом цвета key_colour
            if doors['colour'] == key_colour:
                #добавляем в _graf новые связи
                graph_doors_open[doors['from']].append(doors['to'])
                graph_doors_open[doors['to']].append(doors['from'])
                # print(f'opened doors from {doors["from"]} to {doors["to"]}!')

    return _graf


visited = [False] * (len(graph))


for starts in points:
    if starts['name'][:1:] == 'S':
        print(f"Смотрим на {starts['name']}")
        value_gathered = 0
        visited = [False] * (len(graph))
        dfs(starts['position'], graph)

        for treasure in points:
            if treasure['name'] == 'T':
                if visited[treasure["position"]]:
                    value_gathered += treasure["value"]
                    print(f" + Старт из точки {starts['name']}[{starts['position']}]. Собрано сокровище ценностью {treasure['value']} в точке {treasure['position']}, общая ценность сокровищ {value_gathered}")
