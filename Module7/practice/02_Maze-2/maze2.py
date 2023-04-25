# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под условия текущей задачи
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
    [1,3],          # 0
    [0, 4],       # 1
    [5],          # 2
    [0, 4, 6],       # 3
    [1, 3],    # 4
    [2, 8],       # 5
    [3],          # 6
    [8],          # 7
    [5, 7],          # 8
]

home = 2
bank = 7

path_lengths = bfs(graph, home)
if path_lengths[bank] is not None:
    print("Can go to the bank")
else:
    print("Can't go to the bank")

# Решите задачу и выведите ответ в нужном формате
