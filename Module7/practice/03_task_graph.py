# "Лабиринт с сокровищами"
# см. Картинку на гугло-диске в Модуле-7
# T - сокровища(Treasure)
# Определите:
# Сколько сокровищ можно собрать, стартовав из каждой из предложенных точек?
# Стартовав из какой точки можно собрать максимальное количество сокровищ?
# Стартовав из каких точек, можно собрать максимальное количество сокровищ и дойти до выхода(F)?


# Сюда отправляем полное решение
graph = [
    [1],  # 0
    [0, 2, 5],  # 1
    [1, 3],  # 2
    [2, 4],  # 3
    [3],  # 4
    [1],  # 5
    [7],  # 6
    [6],  # 7
    [9],  # 8
    [8, 10],  # 9
    [9, 11],  # 10
    [10],  # 11
]


def dfs(graph, v):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(v)
    return visited


point_finish = 5
treasures = [2, 4, 6, 8, 9, 10]
start_points = {
    "P-1": 0,
    "P-2": 11,
    "P-3": 7,
    "P-4": 3,
}


def treasures_func(graph, treasures, start_points, finish=None):
    sum_treasures = {}
    for point_name, vertex in start_points.items():
        visited = dfs(graph, vertex)
        if finish is None:
            condition = True
            exit_str = ''
        else:
            condition = visited[finish]
            exit_str = 'дойти до выхода и '
        if condition:
            sum_treasures[point_name] = sum(visited[i] for i in treasures)
            print(f'Из точки {point_name} можно {exit_str}собрать сокровищ в количестве: {sum_treasures[point_name]}')
    print("**************************************")
    for point_name, summa in sum_treasures.items():
        if summa == max(sum_treasures.values()):
            print(f'Максимальное количество сокровищ можно собрать из точки {point_name}')


treasures_func(graph, treasures, start_points)
print()
treasures_func(graph, treasures, start_points, finish=point_finish)
