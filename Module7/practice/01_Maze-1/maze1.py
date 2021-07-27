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
    [6, 9, 11, 14],  # 10
    [10], #11
    [8], #12
    [None], #13
    [10, 15], #14
    [14] #15
]
visited = [False] * len(graph)
start = 0


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)

def labirint(start, finish):
    dfs(start)
    if visited[finish]:
        return f'Из точки {start} можно дойти до финиша'
    return f'Из точки {start} нельзя дойти до финиша'
