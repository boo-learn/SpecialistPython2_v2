# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.
# Решите задачу и выведите ответ в нужном формате
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
    [0,5], #1
    [6], #2
    [7], #3
    [8], #4
    [1], #5
    [2,10], #6
    [3,11], #7
    [4,9,12], #8
    [8,10], #9
    [6,9], #10
    [7,15], #11
    [8], #12
    [], #13
    [], #14
    [11] #15
]
graph_open = [
    [1], #0
    [0,5], #1
    [6], #2
    [7], #3
    [8,5], #4
    [1,4], #5
    [2,10], #6
    [3,11], #7
    [4,9,12], #8
    [8,10], #9
    [6,9], #10
    [7,15], #11
    [8,13], #12
    [12], #13
    [15], #14
    [11] #15
]

finish_=0
start_points=[
    {"name":"S-1","num":5},
    {"name":"S-2","num":13},
    {"name":"S-3","num":3},
    {"name":"S-4","num":8},
]
keys_points=[
    10, 7
]

for point in start_points:
    vis=dfs(graph,point["num"])
    yes="можно" 
    if not vis[finish_]: yes="нельзя"
    print(f'Из точки {point["name"]} {yes} дойти до финиша без ключей')
    if not vis[finish_]:
        for key in keys_points:
            #print(key,vis[key],vis)
            if vis[key]:
                vis_key=dfs(graph_open,point["num"])
                if vis_key[finish_]:
                    print("Но с ключем можно")
