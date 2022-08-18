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
graph = [
    [1], #0
    [0, 5], #1
    [6], #2
    [7], #3
    [5, 8], #4
    [1, 4], #5
    [2, 10], #6
    [3], #7
    [4, 9, 12], #8
    [8, 10], #9
    [6, 9, 11, 14], #10
    [10], #11
    [8], #12
    [], #13
    [10, 15], #14
    [14] #15
]
# Решите задачу и выведите ответ в нужном формате

start = {'s1': 0, 
         's2': 12, 
         's3': 3}
finish = 14
for key in start:
    point = dfs(graph, start[key])
    if key in point:
        print(f'Из точки {start[key]} можно дойти до финиша')
    else:
        print(f'Из точки {start[key]} нельзя дойти до финиша')
