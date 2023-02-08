def dfs(graph, start_point):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited

doors_closed = [
    [1], # 0
    [0, 5], # 1
    [6], # 2
    [7], # 3
    [8], # 4
    [1], # 5
    [2, 10], # 6
    [3, 11], # 7
    [4, 9, 12], # 8 
    [8, 10], # 9 
    [6, 9], # 10
    [7, 15], # 11 
    [8], # 12 
    [], # 13 
    [], # 14 
    [11] # 15 
]

doors_opend = [
    [1], # 0
    [0, 5], # 1
    [6], # 2
    [7], # 3
    [8, 5], # 4
    [1, 4], # 5
    [2, 10], # 6
    [3, 11], # 7
    [4, 9, 12], # 8 
    [8, 10], # 9 
    [6, 9], # 10
    [7, 15], # 11 
    [8, 13], # 12 
    [12], # 13 
    [15], # 14 
    [11, 14] # 15 
]

finish = 0
starts = {'S-1': 5, 'S-2': 13, 'S-3': 3, 'S-4': 8}
# keys = [7, 10]
key = 10

for start_name, start_position in starts.items():
    visited = dfs(doors_closed, start_position)
    if visited[finish]:
        print(f"Из точки {start_name} можно добраться до финиша без ключа")
    elif visited[key]:
        visited = dfs(doors_opend, start_position)
        if visited[finish]:
            print(f"Из точки {start_name} можно добраться до финиша используя ключ")
        else:
            print(f"Из точки {start_name} нельзя добраться до финиша")
    else:
        print(f"Из точки {start_name} нельзя добраться до финиша")
