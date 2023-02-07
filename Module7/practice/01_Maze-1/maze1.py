# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    # список смежности
    [1],            # 0
    [0, 4],         # 1
    [5],            # 2
    [4, 6],         # 3
    [1, 3, 5],      # 4
    [2, 4],         # 5
    [3],            # 6
    [8],            # 7
    [7]             # 8
]

# Решите задачу и выведите ответ в нужном формате

def dfs(graph, start_point):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


visited_vertex = dfs(graph, start_point=0)

if visited_vertex[7] == False:
    print("Can't go to the bank")
else:
    print("Can go to the bank")
