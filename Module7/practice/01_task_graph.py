# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение
# DFS(Depth-First Search) - поиск в глубину
# Позволяет построить обход ориентированного или неориентированного графа,
# при котором посещаются все вершины, доступные из начальной вершины.

# Алгоритм обхода в глубину:
# 1. Пойти в какую-нибудь смежную вершину, не посещенную ранее.
# 2. Запустить из этой вершины алгоритм обхода в глубину
# 3. Вернуться в начальную вершину.
# 4. Повторить пункты 1-3 для всех не посещенных ранее смежных вершин.

graph = [
    # список смежности
    [1],  # 0
    [0, 2, 3],  # 1
    [1, 3, 4, 6],  # 2
    [1, 2, 9],  # 3
    [2],  # 4
    [6],  # 5
    [2, 5, 10],  # 6
    [8],  # 7
    [7],  # 8
    [3],  # 9
    [6]  # 10
]

visited = [False] * (len(graph))
start = 7
exit_point = 10


def dfs(v, x):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w, x)


dfs(start, exit_point)
if visited[exit_point] is True:
    print(f"Из стартовой точки {start} дойти можно")
else:
    print(f"Из стартовой точки {start} дойти нельзя")
#print(visited)
