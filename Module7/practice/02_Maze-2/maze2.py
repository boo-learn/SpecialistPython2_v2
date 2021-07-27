graph = [
    # список смежности
    [1],  # 0
    [0, 2],  # 1
    [1, 3],  # 2
    [2, 7],  # 3
    [5],  # 4
    [4, 6],  # 5
    [5],  # 6
    [3, 11],  # 7
    [9, 12],  # 8
    [8, 10],  # 9
    [9, 11],  # 10
    [7, 10, 15], #11
    [8, 13], #12
    [12, 14], #13
    [13], #14
    [11] #15
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

print(labirint(1, 14))
print(labirint(5, 14))
print(labirint(15, 14))
