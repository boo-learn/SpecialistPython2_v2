graph = [
    # список смежности
    [1],         # 0
    [0, 5],   # 1
    [6],         # 2
    [7],      # 3
    [5,8],         # 4
    [1,4],      # 5
    [2,10],            # 6
    [3],             # 7
    [4,9,12],             # 8
    [8,10],             # 9
    [6,8,11,14],             # 10
    [10],             # 11
    [8],             # 12
    [13],             # 13
    [10,15],            # 14
    [14]             # 15
]

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)

finish = 14
start = [0,12,3]
tekstart = 1
for posstart in start: 
    visited = [False] * (len(graph))
    dfs(posstart)
    if visited[finish]:
        print(f'Из точки S-{tekstart} можно дойти до финиша')
    else:
        print(f'Из точки S-{tekstart} нельзя дойти до финиша')
    tekstart +=1
