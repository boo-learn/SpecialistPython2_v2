# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под условия текущей задачи
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
    [1, 3], # 0 
    [0, 4], # 1
    [5], # 2 bank
    [0, 4, 6], # 3
    [3, 1], # 4
    [2, 8], # 5
    [3], # 6
    [8], # 7 Home
    [7, 5], # 8
]


home = 7
bank = 2
home_to_bank = dfs(graph, home)
if home_to_bank[home] == home_to_bank[bank]:
    print("Сan go to the bank")
else:
    print("Сan't go to the bank")

# Решите задачу и выведите ответ в нужном формате
