# Скопируйте решение из предыдущей задачи и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи
from typing import List, Optional

def bfs(graph: List[List[int]], start_point: int) -> List[Optional[int]]:
    """
    Алгоритм поиска в ширину
    """
    lengths = [None] * len(graph)
    lengths[start_point] = 0
    queue = [start_point]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    return lengths

graph = [
    [1],          # 0 - home
    [0, 4],       # 1
    [5],       # 2 - shop
    [4, 6],       # 3
    [1, 3, 5],    # 4
    [2, 4],       # 5
    [3],          # 6
    [8],       # 7 - bank
    [7],          # 8
]

home = 0
shop = 2
bank = 7

path_lengths_from_home = bfs(graph, home)
path_lengths_from_shop = bfs(graph, shop)

if path_lengths_from_home[bank] is not None:
    print("Can go to the bank from home")
else:
    print("Can't go to the bank from home")

if path_lengths_from_shop[bank] is not None:
    print("Can go to the bank from shop")
else:
    print("Can't go to the bank from shop")

# Решите задачу и выведите ответ в нужном формате
