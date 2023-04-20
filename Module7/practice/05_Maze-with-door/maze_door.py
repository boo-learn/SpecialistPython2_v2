def dfs(graph, start_vertex):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited

closed_graph = [
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
    [9,6], #10
    [7,15], #11
    [8], #12
    [], #13
    [], #14
    [11], #15
]
open_graph = [
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
    [9,6], #10
    [7,15], #11
    [8,13], #12
    [12], #13
    [15], #14
    [11,14], #15
]



finish = 0
keys = [7,10]

def start_to_key(visited, keys):
    for key in keys:
        if visited[key]:
            return True
    return False

for start in range(len(closed_graph)):
    closed_visited = dfs(closed_graph, start)
    open_visited = dfs(open_graph, start)

    if closed_visited[finish]:
        print(f"Из точки {start} можно добраться до финиша {finish} без ключа")

    elif start_to_key(closed_visited, keys) and open_visited[finish]:
        print(f"Из точки {start} можно добраться до финиша {finish}, используя ключ")

    else:
        print(f"Из точки {start} нельзя добраться до финиша {finish}")
