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


def go_to_point(visited, finish_point, point_name='bank'):
    if visited[finish_point]:
        print(f"Сan go to the {point_name}")
    else:
        print(f"Сan't go to the {point_name}")

# Решите задачу и выведите ответ в нужном формате


graph = [[1],
         [0, 4],
         [5],
         [4],
         [1, 3, 7],
         [2],
         [],
         [4, 8],
         [7],
         ]
home = 1
bank = 3
shop = 5
bar = 8
can_visit = dfs(graph, home)
go_to_point(can_visit, bank, 'bank')
go_to_point(can_visit, shop, 'shop')
go_to_point(can_visit, bar, 'bar')
