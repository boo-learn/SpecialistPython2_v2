# Скопируйте решение из предыдущей задачи и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи


# Решите задачу и выведите ответ в нужном формате
def dfs(graph: list, start_point: int) -> list[bool]:
    """
    Алгоритм поиска в глубину
    """
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


graph = [
    # список смежности
    [1],  # 0
    [0, 4],  # 1
    [5],  # 2
    [4],  # 3
    [1, 3, 7],  # 4
    [2],  # 5
    [],  # 6
    [4, 8],  # 7
    [7]  # 8
]

home_point = 1
points = {
    "bank": 3,
    "shop": 5,
    "bar": 8,
    "new": 0
}

visited = dfs(graph, start_point=home_point)

for place, point in points.items():
    if visited[point]:
        print(f"Сan go to the {place}")
    else:
        print(f"Сan't go to the {place}")
