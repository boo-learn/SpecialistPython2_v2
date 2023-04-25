graph = [
    [1],    # 0
    [0, 4],  #1
    [5],    # 2
    [4], # 3
    [1, 3, 7],     # 4
    [2],  # 5
    [],  # 6
    [8, 4],  # 7
    [7], # 8
]

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

bar_point =  8
home_point = 1
bank_point = 3
shop_point = 5
shop_way = (dfs(graph, home_point)[shop_point], "shop")
bank_way = (dfs(graph, home_point)[bank_point], "bank")
bar_way = (dfs(graph, home_point)[bar_point], "bar")
def answer(var):
    if var[0]:
        print(f"Can go to the {var[1]}")
    else:
        print(f"Can't go to the {var[1]}")

answer(shop_way)
answer(bank_way)
answer(bar_way)
