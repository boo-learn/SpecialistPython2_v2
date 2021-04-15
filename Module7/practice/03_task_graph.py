# "Лабиринт с сокровищами"
# см. Картинку на гугло-диске в Модуле-7
# T - сокровища(Treasure)
# Определите:
# Сколько сокровищ можно собрать, стартовав из каждой из предложенных точек?
# Стартовав из какой точки можно собрать максимальное количество сокровищ?
# Стартовав из каких точек, можно собрать максимальное количество сокровищ и дойти до выхода(F)?


# Сюда отправляем полное решение
def dfs(graph, v):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(v)
    return visited


graph = [
    [1, 5],  # 0
    [0, 5],  # 1
    [10],  # 2
    [6],  # 3
    [7, 5],  # 4
    [0, 1, 4],  # 5
    [3],  # 6
    [4],  # 7
    [9],  # 8
    [8, 10],  # 9
    [2, 9]  # 10
]

point_finish = 0
start_points = {
    "P-1": 1,
    "P-2": 2,
    "P-3": 3,
    "P-4": 4
}
chests = [5, 6, 7, 8, 9, 10]

max_count = 0
max_count_with_finish = 0
result = {}
result_with_finish = {}
for point_name, vertex in start_points.items():
    visited = dfs(graph, vertex)
    count = 0
    finish_flag = 0
    if visited[point_finish]:
        finish_flag += 1
    for chest in chests:
        if visited[chest]:
            count += 1
            if max_count < count:
                result.clear()
                max_count = count
                result[point_name] = max_count
            if finish_flag and max_count_with_finish <= count:
                max_count_with_finish = count
                result_with_finish[point_name] = max_count_with_finish
    print(f'Начав с точки {point_name} можно собрать {count} сундуков')

print(f"Максимальное количество сундуков ({list(result.values())[0]}) можно собрать, "
      f"стартовав из точки {''.join(list(i for i in result.keys()))}")
print(f"Дойдя до финиша, максимальное количество сундуков ({list(result_with_finish.values())[0]}) можно собрать, "
      f"стартовав из точек {', '.join(list(i for i in result_with_finish.keys()))}")
