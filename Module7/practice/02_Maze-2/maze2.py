# Скопируйте решение из предыдущей задачи(Maze-1) и адаптируйте под условия текущей задачи
# Чем меньше пришлось вносить изменений в код программы, тем лучше было решение предыдущей задачи


# Решите задачу и выведите ответ в нужном формате

def dfs(start_vertex, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


graph = [
    [1],
    [0,2],
    [1,3],
    [2,7],
    [5],
    [4,6],
    [5],
    [3,11],
    [9,12],
    [8,10],
    [9,11],
    [10,7,15],
    [8,13],
    [12,14],
    [13],
    [11]
]

start = {'S-1':1, 'S-2':5, 'S-3':15}
finish = 14

for key, value in start.items():
    result = dfs(value, graph)
    if result[finish]:
        print(f"Из точки {key} можно дойти до финиша")
    else:
        print(f"Из точки {key} нельзя дойти до финиша")
