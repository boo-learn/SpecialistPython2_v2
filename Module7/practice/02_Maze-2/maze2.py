graph = [
    # список смежности
    [1],         # 0
    [0,2],   # 1
    [1,3],         # 2
    [2,7],      # 3
    [5],         # 4
    [4,6],      # 5
    [5],            # 6
    [3,11],             # 7
    [9,12],             # 8
    [8,10],             # 9
    [11,9],             # 10
    [10,15],             # 11
    [13],             # 12
    [12,14],             # 13
    [13],            # 14
    [11]             # 15
]

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)

finish = 14
start = [1,5,15]
tekstart = 1
for posstart in start: 
    visited = [False] * (len(graph))
    dfs(posstart)
    if visited[finish]:
        print(f'Из точки S-{tekstart} можно дойти до финиша')
    else:
        print(f'Из точки S-{tekstart} нельзя дойти до финиша')
    tekstart +=1
