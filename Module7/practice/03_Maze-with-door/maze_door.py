def dfs(start_point, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.

graph_doors = [
    [4],  # 0
    [2],  # 1
    [1,3],  # 2
    [2],  # 3
    [0],  # 4 5-door
    [6],  # 5 4-door
    [5,7],  # 6 7-key
    [6],  # 7
    [],  # 8
    [5,13],  # 9
    [11,14],  # 10
    [10],  # 11 10 - key
    [],  # 12 13-door
    [9,14],  # 13 12-door 
    [13,10],  # 14 10-key 15-door
    []  # 15 14 -door
]

graph_with_key =[
    [4],  # 0
    [2],  # 1
    [1,3],  # 2
    [2],  # 3
    [0,5],  # 4 5-door
    [4,6],  # 5 4-door
    [5,7],  # 6 7-key
    [6],  # 7
    [],  # 8
    [5,13],  # 9
    [11,14],  # 10
    [10],  # 11 10 - key
    [13],  # 12 13-door
    [12,9,14],  # 13 12-door 
    [13,10,15],  # 14 10-key 15-door
    [14]  # 15 14 -door
]
# Решите задачу и выведите ответ в нужном формате

finish_point = 0
# start_points = (1,5,15)
start_points = {
    "S-1": 5,
    "S-2": 13,
    "S-3": 3,
    "S-4": 8
}
key_points = (7, 10)
for point_name, vertex in start_points.items():
    vis_without_key = dfs(vertex, graph_doors)
    if vis_without_key[finish_point]:
        print(f'Из точки {point_name} можно дойти до финиша без ключа')
    else:
        fin= False
        for key_point in key_points:
            if vis_without_key[key_point]:
                vis_with_key = dfs(vertex, graph_with_key)
                if vis_with_key[finish_point]:
                    fin = True
        if fin:
            print(f'Из точки {point_name} можно дойти до финиша, используя ключ')
        else:
            print(f'Из точки {point_name} нельзя дойти до финиша')
