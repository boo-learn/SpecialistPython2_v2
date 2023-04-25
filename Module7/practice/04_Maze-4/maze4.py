# Скопируйте решение из предыдущей задачи и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи
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

region = [
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
bank_point = (3, 'bank')
shop_point = (5, 'shop')
bar_point = (8, 'bar')

points = [bank_point, shop_point, bar_point]

visited = dfs(region, start_point=home_point)

for point, place in points:
    if visited[point]:
        print(f"Сan go to the {place}")
    else:
        print(f"Сan't go to the {place}")

# Решите задачу и выведите ответ в нужном формате
