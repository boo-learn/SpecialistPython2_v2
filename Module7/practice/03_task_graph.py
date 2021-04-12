# "Лабиринт с сокровищами"
# см. Картинку на гугло-диске в Модуле-7
# T - сокровища(Treasure)
# Определите:
# Сколько сокровищ можно собрать, стартовав из каждой из предложенных точек?
# Стартовав из какой точки можно собрать максимальное количество сокровищ?
# Стартовав из каких точек, можно собрать максимальное количество сокровищ и дойти до выхода(F)?


# Сюда отправляем полное решение
def start_bfs(start, graph):
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


graph = [
    # список смежности
    [1, 3],  # 0
    [0, 2],  # 1
    [1],  # 2
    [0],  # 3
    [5],  # 4
    [4],  # 5
    [7],  # 6
    [6, 9],  # 7
    [9, 10],  # 8
    [7, 8, 10],  # 9
    [8, 9]  # 10
]
treasures = [0, 1, 3, 4, 6, 9]
start_points = {
    'P-1': 8,
    'P-2': 2,
    'P-3': 5,
    'P-4': 7
}
finish_point = 10
optimal_points = {}

# 1. Сколько сокровищ можно собрать, стартовав из каждой из предложенных точек?
for point_name, start_point in start_points.items():
    visited = start_bfs(start_point, graph)
    count_treasure = 0
    for treasure in treasures:
        if visited[treasure]:
            count_treasure += 1

    optimal_points[point_name] = count_treasure
    print(f"Из точки {point_name} можно собрать {count_treasure} сокровищ")

# 2. Стартовав из какой точки можно собрать максимальное количество сокровищ?
optimal_points = sorted(optimal_points.items(), reverse=True, key=lambda couple: couple[1])
print(f"Максимальное количество сокровищ можно собрать, стартовав из точки {optimal_points[0][0]}")

# 3. Стартовав из каких точек, можно собрать максимальное количество сокровищ и дойти до выхода(F)?
optimal_points = {}
for point_name, start_point in start_points.items():
    visited = start_bfs(start_point, graph)
    count_treasure = 0
    for treasure in treasures:
        if visited[treasure] and visited[finish_point]:
            count_treasure += 1

    optimal_points[point_name] = count_treasure

optimal_points = sorted(optimal_points.items(), reverse=True, key=lambda couple: couple[1])

finish_points = {}
optimal_point = optimal_points[0]
for current_point in optimal_points:
    if current_point[1] == optimal_point[1]:
        finish_points[current_point[0]] = current_point[1]

for key, value in finish_points.items():
    print(f"Максимальное количество сокровищ {value} можно собрать и дойти до выхода, стартовав из точки {key}")

