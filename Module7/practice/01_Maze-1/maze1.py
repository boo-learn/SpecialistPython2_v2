def dfs(graph, start_vertex):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited

# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1], # 0 Home
    [0, 4], # 1
    [5], # 2
    [4, 6], # 3
    [3, 1, 5], # 4
    [2, 4], # 5
    [3], # 6
    [8], # 7 bank
    [7], # 8
]

# Решите задачу и выведите ответ в нужном формате

home = 0
bank = 7
home_to_bank = dfs(graph, home)
if home_to_bank[home] == home_to_bank[bank]:
    print("Сan go to the bank")
else:
    print("Сan't go to the bank")
