def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


graph = [
    # список смежности
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
    [13],  # 13
    [10, 15],  # 14
    [14]  # 15
]

start1 = 0
start2 = 12
start3 = 3
finish = 14

visited1 = dfs(graph, start1)

start_list =[]
start_list.append(start1)
start_list.append(start2)
start_list.append(start3)

for start in start_list:
    visited = dfs(graph, start)
    if visited[finish] == True:
        print (f"Из точки {start} можно дойти то точки финиша")
    else:
        print (f"Из точки {start} нельзя дойти то точки финиша")
