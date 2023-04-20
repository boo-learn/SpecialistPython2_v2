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
    [1], # 0 
    [0, 4], # 1 home
    [5], # 2 
    [4], # 3 bank
    [3, 1, 7], # 4
    [2], # 5 shop
    [], # 6
    [8, 4], # 7 
    [7], # 8 bar
]


home = 1
needed_places = [
    ["bank", 3], 
    ["shop", 5],
    ["bar", 8]
    ]

home_to = dfs(graph, home)
for place in needed_places:
    if home_to[place[1]]:
        print(f"Сan go to the {place[0]}")
    else:
        print(f"Сan't go to the {place[0]}")

# Решите задачу и выведите ответ в нужном формате
