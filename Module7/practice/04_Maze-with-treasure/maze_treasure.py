# Сюда отправляем решение задачи "Лабиринт с сокровищами"
def dfs(start_point,graph):
    visited = [False] * (len(graph))
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(start_point)
    return visited

graph = [
    # список смежности
    [1,4],             # 0
    [0,2],             # 1
    [1],               # 2
    [7],               # 3
    [0],               # 4
    [6,9],             # 5
    [5,10],            # 6
    [3,11],            # 7
    [9,12],            # 8
    [5,8,10],          # 9
    [6,9,14],          # 10
    [7],               # 11
    [8],               # 12
    [],                # 13
    [10,15],           # 14
    [14],              # 15
]
rich=[
    0,             # 0
    1,             # 1
    2,             # 2
    0,             # 3
    3,             # 4
    0,             # 5
    5,             # 6
    3,             # 7
    0,             # 8
    5,             # 9
    3,             # 10
    0,             # 11
    0,             # 12
    8,             # 13
    4,             # 14
    7              # 15
]

start_points={
    0: "S-1",
    12: "S-2",
    3: "S-3",
    }

for vertex, point_name in start_points.items():
    visit_rich=[]
    visited = dfs(vertex, graph)
    for i in range(len(visited)):
        if visited[i]:
            visit_rich.append(rich[i])
    visit_rich.sort(reverse=True)
    print(f"Из точки {point_name} можно собрать сокровищ суммарной ценностью {sum(visit_rich[:2])}")
