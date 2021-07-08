# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение
graph = [
    # список смежности
    [1],  # 0
    [2, 4],  # 1
    [1, 3, 4],  # 2
    [2],  # 3
    [1, 6, 5],  # 4
    [4],  # 5
    [4, 7, 8],  # 6
    [6],  # 7
    [6],     #8
    [10],    #9
    [9]     #10
]

visited = [False] * (len(graph))
prev = [None] * (len(graph))
start = 0
start_points = {0 : "S-3", 3 : "S-2", 9 : "S-1"}

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


dfs(start)
print(visited)
for point, name in start_points.items():
    if visited[point]: print(f'можно дойти из точки : {name}')
    if not visited[point]: print(f'нельзя дойти из точки : {name}')
