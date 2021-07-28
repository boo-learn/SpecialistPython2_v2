# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.
# Решите задачу и выведите ответ в нужном формате
import copy
graph = [
    # список смежности
    [1],             # 0
    [0,5],             # 1
    [6],             # 2
    [7],             # 3
    [8],             # 4
    [1],             # 5
    [2,10],          # 6
    [3,11],             # 7
    [4,9,12],          # 8
    [8,10],          # 9
    [6,9],     # 10
    [7,15],            # 11
    [8],             # 12
    [],              # 13
    [],         # 14
    [11],            # 15
]

def create_new_graph(graph,doors):
    graph_with_door=copy.deepcopy(graph)

    for door in doors:
        graph_with_door[door[0]].append(door[1])
        graph_with_door[door[1]].append(door[0])
    return graph_with_door

def dfs(start_point,graph):
    visited = [False] * (len(graph))
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(start_point)
    return visited

doors=[[4,5],[12,13],[14,15]]
keys=[7,10]
start_points={
    5: "S-1",
    13: "S-2",
    3: "S-3",
    8: "S-4",
}
finish_point=0

if doors!=[]:
    graph_with_door=create_new_graph(graph,doors)

for vertex, point_name in start_points.items():
    text=""
    visited = dfs(vertex, graph)
    if not visited[finish_point]:
        visited_with_door = dfs(vertex, graph_with_door)
        for key in keys:
            if visited[key] and visited_with_door[finish_point]:
                text=f"Из точки {point_name} можно добраться до финиша, используя ключ"
    else:
        text=f"Из точки {point_name} можно добраться до финиша без ключа"
    if text=="":
        text = f"Из точки {point_name} нельзя добраться до финиша"
    print(text)
