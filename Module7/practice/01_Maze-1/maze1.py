# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

def dfs(start_point, graph):
    visited_list = [False] * (len(graph))

    def _dfs(v):
        visited_list[v] = True
        for w in graph[v]:
            if not visited_list[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(start_point)
    return visited_list
# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1], #0
    [0,5], #1
    [6],   #2
    [7],   #3
    [5, 8],#4
    [4],   #5
    [2, 10],#6
    [3],    #7
    [4, 9, 12], #8
    [8, 10], #9
    [6, 9, 11, 14], #10
    [10], #11
    [8], #12
    [], #13
    [10, 15],#14
    [14] #15
]

start_points = {"S-1": 0, "S-2": 12, "S-3": 3}
finish_point = 14
for key, value in start_points.items():
    visited = dfs(value, graph)
    if visited[finish_point]:
        print(f"Из точки {key} можно дойти до финиша")
    else:
        print(f"Из точки {key} нельзя дойти до финиша")
