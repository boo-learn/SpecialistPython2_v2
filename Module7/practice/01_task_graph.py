# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение

graph = [
    # список смежности
    [4],  # 0
    [5],  # 1
    [11],  # 2
    [14],  # 3
    [0, 6, 10],  # 4
    [1, 8, 6],  # 5
    [4, 5, 13, 7],  # 6
    [6],  # 7
    [5],  # 8
    [14],  # 9
    [4],  # 10
    [2],  # 11
    [13],  # 12
    [12, 15, 14],  # 13
    [13, 3, 9],  # 14
    [13]  # 15
]

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)

visited = [False] * (len(graph))
prev = [None] * (len(graph))
start_list = [1, 2, 3, 4]
finish = 15
for i in start_list:
    start = i
    dfs(start)
    if visited[finish]:
        print(f'Из точки P{start} можно добраться до выхода')
    else:
        print(f'Из точки P{start} нельзя добраться до выхода')
    visited = [False] * (len(graph))
