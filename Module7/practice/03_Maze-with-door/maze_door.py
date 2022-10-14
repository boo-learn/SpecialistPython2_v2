# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def dfs(start_point, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


graph_no_door = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [12],  # 13
    [10, 15],  # 14
    [14],  # 15
]
graph = [
    [1],  # 0
    [5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10],  # 14
    [],  # 15
]

# Решите задачу и выведите ответ в нужном формате
finish_point = 0
start_points = {
    "S-1": 5,
    "S-2": 13,
    "S-3": 3,
    "S-4": 8
}
vis = dfs(finish_point, graph)
vis_no_door = dfs(finish_point, graph_no_door)
rezult_vis=[]
for i in range(len(vis)):
    if vis[i] or vis_no_door[i]:
        rezult_vis.append(True)
    else:
        rezult_vis.append(False)

for point_name, vertex in start_points.items():
    if rezult_vis[vertex]:
        print(f'Из точки {point_name} можно дойти до финиша')
    else:
        print(f'Из точки {point_name} нельзя дойти до финиша')

