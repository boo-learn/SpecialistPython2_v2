# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение
graph = [
    [1],    # 0
    [0, 2, 4],  # 1
    [1, 3, 4],      # 2
    [2],    # 3
    [1, 2, 5, 7],   # 4
    [4],    # 5
    [4, 7, 8],  # 6
    [6],    # 7
    [6],    # 8
    [10],   # 9
    [9]     # 10
]


def path_finder(start: int, finish):
    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
            if cur_vertex == finish:
                return True
    return False


s = 0
f = 8
if path_finder(s, f):
    print(f"Из точки {s} можно дойти до финиша")
else:
    print(f"Из точки {s} нельзя дойти до финиша")
