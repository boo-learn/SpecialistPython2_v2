# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


def route(start, finish):
    global visited
    visited = [False] * len(graph)
    dfs(start)
    return visited[finish]


# Опишите список смежности по изображению лабиринта из файла task.md
graph = [  # список смежности
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [4, 1],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15
]

visited = [False] * (len(graph))    # Список, заполненный значениями False, по длине равный списку graph
target_point = 14
start_1 = 0
start_2 = 12
start_3 = 3
s1_name = "S-1"
s2_name = "S-2"
s3_name = "S-3"
target_name = "F"


# Решите задачу и выведите ответ в нужном формате
if route(start_1, target_point):
    print(f'Из точки {s1_name} можно дойти до точки {target_name}')
else:
    print(f'Из точки {s1_name} нельзя дойти до точки {target_name}')

if route(start_2, target_point):
    print(f'Из точки {s2_name} можно дойти до точки {target_name}')
else:
    print(f'Из точки {s2_name} нельзя дойти до точки {target_name}')

if route(start_3, target_point):
    print(f'Из точки {s3_name} можно дойти до точки {target_name}')
else:
    print(f'Из точки {s3_name} нельзя дойти до точки {target_name}')
