# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение

graph = [
    # список смежности
    [1],  # 0
    [2, 4, 0],  # 1
    [1],  # 2
    [5],  # 3
    [1, 5, 6, 10],  # 4
    [3, 7, 4],  # 5
    [4],  # 6
    [5],  # 7
    [11],  # 8
    [10],  # 9
    [9, 11, 13],  # 10
    [10, 12, 8],  # 11
    [11],  # 12
    [10],  # 13
    [15],  # 14
    [14]  # 15
]


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


F = 13

visited = [False] * (len(graph))
prev = [None] * (len(graph))
start_p1 = 0
dfs(start_p1)
if visited[F]:
    print("Дойти из точки p1 до финиша можно")
else:
    print("Дойти из точки p1 до финиша нельзя")

visited = [False] * (len(graph))
prev = [None] * (len(graph))
start_p4 = 5
dfs(start_p4)
if visited[F]:
    print("Дойти из точки p4 до финиша можно")
else:
    print("Дойти из точки p4 до финиша нельзя")

visited = [False] * (len(graph))
prev = [None] * (len(graph))
start_p3 = 12
dfs(start_p4)
if visited[F]:
    print("Дойти из точки p3 до финиша можно")
else:
    print("Дойти из точки p3 до финиша нельзя")

visited = [False] * (len(graph))
prev = [None] * (len(graph))
start_p2 = 14
dfs(start_p2)
if visited[F]:
    print("Дойти из точки p2 до финиша можно")
else:
    print("Дойти из точки p2 до финиша нельзя")
