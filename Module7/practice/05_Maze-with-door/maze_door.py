# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.
from collections import deque

graph = [
    [1],        # 0 – F (финиш)
    [0, 5],     # 1
    [6],        # 2
    [7],        # 3 – точка старта S-3
    [8],        # 4
    [1],        # 5 – точка старта S-1
    [2, 10],    # 6
    [3, 11],    # 7 – K (ключ)
    [4, 9, 12], # 8 – точка старта S-4
    [8, 10],    # 9
    [6, 9],     # 10 – K (ключ)
    [7, 15],    # 11
    [8],        # 12
    [-1],       # 13 – точка старта S-2
    [-1],       # 14
    [11],       # 15
]

doors = [
    (4, 5),
    (12, 13),
    (14, 15)
]

keys = [7, 10]

start_points = {
    5: "S-1",
    13: "S-2",
    3: "S-3",
    8: "S-4"
}
def bfs(start, graph):
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)

    return visited

for start, point_name in start_points.items():
    is_reachable = bfs(start, graph)

    if is_reachable[0]:
        print(f"Из точки {point_name} можно добраться до финиша без ключа")
    elif any(is_reachable[d[1]] and d[0] not in keys for d in doors):
        print(f"Из точки {point_name} нельзя добраться до финиша")
    else:
        print(f"Из точки {point_name} можно добраться до финиша, используя ключ")

# Решите задачу и выведите ответ в нужном формате
