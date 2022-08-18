# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def dfs(graph, start):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start)
    return visited

# Опишите список смежности по изображению лабиринта из файла task.md
def check(graph, start_point, finish_point):
    res = dfs(graph, start_point)

    if res[finish_point]:
        return f'Из точки {start_point} можно добраться до финиша' #точки {finish_point}
    else:
        return f'Из точки {start_point} нельзя добраться до финиша'

graph = [
    [1], # 0
    [0,2], # 1
    [1,3], # 2
    [2,7], # 3
    [5], # 4
    [4,6], # 5
    [5], # 6
    [3,11], # 7
    [9,12], # 8
    [8,10], # 9
    [9,11], # 10
    [7,10,15], # 11
    [8,13], # 12
    [12,14], # 13
    [13], # 14
    [11], # 15
]

# Решите задачу и выведите ответ в нужном формате
S_1 = 1
S_2 = 5
S_3 = 15

F = 14

print(check(graph,S_1,F))
print(check(graph,S_2,F))
print(check(graph,S_3,F))

