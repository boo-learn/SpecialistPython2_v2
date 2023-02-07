# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи


# Решите задачу и выведите ответ в нужном формате

# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    # список смежности
    [1, 3, 4],      # 0
    [0, 3, 4],      # 1
    [5],            # 2
    [4, 6, 1, 0],   # 3
    [1, 3, 0],      # 4
    [2, 8],         # 5
    [3],            # 6
    [8],            # 7
    [7, 5]          # 8
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


visited_vertex = dfs(graph, start_point=2)

if visited_vertex[7] == False:
    print("Can't go to the bank")
else:
    print("Can go to the bank")
