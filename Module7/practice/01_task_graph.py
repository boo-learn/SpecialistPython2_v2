# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение
"""
    0s      9s
    |       |
    1      10
   / \
  2 - 4
 /   / \
3s  5   6
       / \
      7   8f
"""

graph = [
    [1],            # 0
    [2, 4],         # 1
    [1, 3, 4],      # 2
    [2],            # 3
    [1, 2, 5, 6],   # 4
    [4],            # 5
    [4, 7, 8],      # 6
    [6],            # 7
    [6],            # 8
    [10],           # 9
    [9]             # 10
]
found = False
def search_path_between_nodes(gr, n1, n2):

    visited = [False] * (len(graph))
    start = n1
    end = n2
    end_found = False

    def dfs_path(current):
        nonlocal end_found
        visited[current] = True
        for node in gr[current]:
            if not visited[node]:  # посещён ли текущий сосед?
                if node == end:
                    end_found = True
                else:
                    dfs_path(node)

    dfs_path(start)
    if end_found:
        print(f"It is POSSIBLE to reach node {n2} from node {n1}.")
    else:
        print(f"It is IMPOSSIBLE to reach node {n2} from node {n1}.")

search_path_between_nodes(graph, 0, 8)
search_path_between_nodes(graph, 3, 8)
search_path_between_nodes(graph, 9, 8)

