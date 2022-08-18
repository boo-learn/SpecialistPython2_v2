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
def check(graph_close,graph_open,keys,start_points,finish_point):
    check_close = False
    start_points_finish = []
    for name, value in start_points.items():
        res = dfs(graph_close, value)

        if res[finish_point]:
            print(f'Из точки {name} можно добраться до финиша без ключа') #точки {finish_point}
        else:

            check_key = False
            for key in keys:
                if res[key]:
                    check_key = True
            if check_key:
                res_open = dfs(graph_open, finish_point)
                if res_open[value]:
                    print(f'Из точки {name} можно добраться до финиша c ключом') #точки {finish_point}
                else:
                    print(f'Из точки {name} нельзя добраться до финиша')
            else:
                print(f'Из точки {name} нельзя добраться до финиша')


graph_close = [
    [1], # 0
    [0,5], # 1
    [6], # 2
    [7], # 3
    [8], # 4
    [1], # 5
    [2,10], # 6
    [3,11], # 7
    [4,9,12], # 8
    [8,10], # 9
    [6,9], # 10
    [7,15], # 11
    [8], # 12
    [], # 13
    [], # 14
    [11], # 15
]

graph_open = [
    [1], # 0
    [0,5], # 1
    [6], # 2
    [7], # 3
    [5,8], # 4
    [1,4], # 5
    [2,10], # 6
    [3,11], # 7
    [4,9,12], # 8
    [8,10], # 9
    [6,9], # 10
    [7,15], # 11
    [8,13], # 12
    [12], # 13
    [15], # 14
    [11,14], # 15
]

keys = [7, 10]

# Решите задачу и выведите ответ в нужном формате
start_points ={
'S-1':5,
'S-2':13,
'S-3':3,
'S-4':8
}
F = 0

check(graph_close,graph_open,keys,start_points,F)


