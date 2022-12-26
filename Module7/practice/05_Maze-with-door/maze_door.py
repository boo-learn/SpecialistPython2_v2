graph = [
    # список смежности
    [1],         # 0
    [0, 5],   # 1
    [6],         # 2
    [7],      # 3
    [8],         # 4
    [1],      # 5
    [2, 10],            # 6
    [3, 11],            # 7
    [4, 9, 12],             # 8
    [8, 10], # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8], # 12
    [],  # 13
    [],  # 14
    [11]  # 15
]

#ячейки с ключами
keys = [7, 10]
#двери
doors = [(4,5), (12,13), (14,15)]
#точки начала
start_points = {'s1':5, 's2':13, 's3':3, 's4':8}
#точка конца
finish_point = 0
#есть ли ключ после 1го прохода у точки
point_keys = {'s1':False, 's2':False, 's3': False, 's4':False}
point_finish = {'s1':False, 's2':False, 's3': False, 's4':False}

def dfs(graph, start_point):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(start_point)
    return visited

#достигла ли точка финиша
def is_finish(visited, finish_point):
    if visited[finish_point]:
        return True

#достигли ли стартовые точки ключей
for sp_name, sp_val in start_points.items():
    vis = dfs(graph, sp_val)
    #print(vis, is_finish(vis, finish_point))
    for index, val in enumerate(vis):
        if index in keys and val:
            point_keys[sp_name] = True

print (f"Точки старта с ключами: {point_keys}")
#print(dfs(graph, 0))
#измененный граф - с открытыми дверями

#не работает надо копировать по элементно
#gr2 = graph.copy()

for k,v in start_points.items():
    if is_finish(dfs(graph,v), finish_point):
        point_finish[k] = True

for num, val in enumerate(graph):
    for doornum in doors:
       if doornum[0] == num:
            graph[num].append(doornum[1])
       if doornum[1] == num:
            graph[num].append(doornum[0])

for k,v in start_points.items():
    if not point_finish[k] and is_finish(dfs(graph,v), finish_point) and point_keys[k]:
        point_finish[k] = True

print(f"Доступность финишной точки для стартовых точек: {point_finish}")
