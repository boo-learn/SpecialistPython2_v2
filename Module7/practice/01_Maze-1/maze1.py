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
def check(graph, start_points, finish_point):
    res = dfs(graph, finish_point)
    for name, value in start_points.items():
        if res[value]:
            print(f'Из точки {name} можно добраться до финиша') #точки {finish_point}
        else:
            print(f'Из точки {name} нельзя добраться до финиша')


graph = [
    [1], # 0
    [0,5], # 1
    [6], # 2
    [7], # 3
    [5,8], # 4
    [1,4], # 5
    [10], # 6
    [3], # 7
    [4,9,12], # 8
    [8,10], # 9
    [6,9,11,14], # 10
    [10], # 11
    [8], # 12
    [], # 13
    [10,15], # 14
    [14], # 15
]

# Решите задачу и выведите ответ в нужном формате
start_points ={
'S_1':0,
'S_2':3,
'S_3':12
}
F = 14

check(graph,start_points,F)


