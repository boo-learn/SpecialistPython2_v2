# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


# Решите задачу и выведите ответ в нужном формате
def dfs(graph, start):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start)
    return visited

graph_close_doors = [
    [1], #0
    [0, 5], #1
    [6], #2
    [7], #3
    [8], #4
    [1], #5
    [2, 10], #6
    [3, 11], #7
    [4, 9, 12], #8
    [8, 10], #9
    [9, 6], #10
    [7, 15], #11
    [8], #12
    [], #13
    [], #14
    [11] #15
]

graph_open_doors = [
    [1], #0
    [0, 5], #1
    [6], #2
    [7], #3
    [5, 8], #4
    [1, 4], #5
    [2, 10], #6
    [3, 11], #7
    [4, 9, 12], #8
    [8, 10], #9
    [9, 6], #10
    [7, 15], #11
    [8, 13], #12
    [12], #13
    [15], #14
    [11, 14] #15 
]

key_points = [7, 10]

start_points = {
    'S-1': 5,
    'S-2': 13,
    'S-3': 3,
    'S-4': 8
}

finish_point = 0

for name, start in start_points.items():
    if dfs(graph_close_doors, start)[finish_point]:
        print(f"Из точки {name} можно дойти до финиша без ключа")
    else:
        has_key = False
        for key in key_points:
            if dfs(graph_close_doors, start)[key]:
                has_key = True
        if has_key:
            if dfs(graph_open_doors, start)[finish_point]:
                print(f"Из точки {name} можно дойти до финиша c ключом")
            else:
                print(f"Из точки {name} нельзя дойти до финиша")
        else:
            print(f"Из точки {name} нельзя дойти до финиша")
