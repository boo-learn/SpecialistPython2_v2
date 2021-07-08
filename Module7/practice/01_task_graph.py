# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение
def bfs(graph, start, finish):

    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)

    return lengths[finish]

######################
# лабиринт:
#graph = [
        # список смежности
    #     [1],  # 0
    #     [2, 4],  # 1
    #     [1, 4, 3],  # 2
    #     [2],  # 3
    #     [1, 2, 5, 6],  # 4
    #     [4],  # 5
    #     [4,7,8],  # 6
    #     [6],  # 7
    #     [6],  # 8
    #     [10],  # 9
    #     [9]  # 10
    # ]

graph = [
        # список смежности
        [],  # 0
        [2],  # 1
        [1, 3, 6],  # 2
        [2],  # 3
        [5],  # 4
        [4],  # 5
        [2],  # 6
    ]

#список точек старта:
#S = [3, 0, 9]
S = [4, 1, 0]
F = 3

for start in S:
    if bfs(graph, start, F) is None:
        result = 'нельзя'
    else:
        result = 'можно'
    print(f"Из точки S-{S.index(start)} {result} дойти до финиша")
