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
bank_point = 3
shop_point = 5
bar_point = 8

visited = dfs(graph, start_point=home_point)

if visited[bank_point]:
    print("Сan go to the bank")
else:
    print("Сan't go to the bank")
if visited[shop_point]:
    print("Сan go to the shop")
else:
    print("Сan't go to the shop")
if visited[bar_point]:
    print("Сan go to the bar")
else:
    print("Сan't go to the bar")
