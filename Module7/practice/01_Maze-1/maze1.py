# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
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

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [[1],
         [0, 4],
         [5],
         [4, 6],
         [1, 3, 5],
         [2, 4],
         [3],
         [8],
         [7],
         ]

# Решите задачу и выведите ответ в нужном формате
go_to_bank(graph, 0, 7)
