# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
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
    [1],          # 0
    [0, 4],       # 1
    [5],          # 2
    [4, 6],       # 3
    [1, 3, 5],    # 4
    [2, 4],       # 5
    [3],          # 6
    [8],          # 7
    [7],          # 8
]

home = 0
bank = 7

path_lengths = bfs(graph, home)
if path_lengths[bank] is not None:
    print("Can go to the bank")
else:
    print("Can't go to the bank")
