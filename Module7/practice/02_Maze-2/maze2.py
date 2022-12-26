# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи
def dfs(graph, start_point):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


def go_to_bank(graph, home, bank):
    if dfs(graph, home)[bank]:
        print("Сan go to the bank")
    else:
        print("Сan't go to the bank")

# Решите задачу и выведите ответ в нужном формате


graph = [[1, 3, 4],
         [0, 4],
         [5],
         [0, 4, 6],
         [1, 3],
         [2, 8],
         [3],
         [8],
         [5, 7],
         ]

go_to_bank(graph, 2, 7)
