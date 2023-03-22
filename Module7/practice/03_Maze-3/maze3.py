# Скопируйте решение из предыдущей задачи и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи

def dfs(graph, start_vertex):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited

graph = [
    [1], # 0 home
    [0, 4], # 1
    [5], # 2 shop
    [4, 6], # 3
    [3, 1, 5], # 4
    [2, 4], # 5
    [3], # 6
    [8], # 7 bank
    [7], # 8
]

home = 0

needed_places = [
    ["bank", 7], 
    ["shop", 2]
    ]

home_to = dfs(graph, home)
for place in needed_places:
    if home_to[place[1]]:
        print(f"Сan go to the {place[0]}")
    else:
        print(f"Сan't go to the {place[0]}")

