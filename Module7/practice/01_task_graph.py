graph = [
    # список смежности
    [1, 4],  # 0
    [2, 4],  # 1
    [3, 4],  # 2
    [2],  # 3
    [1, 2, 5, 6],  # 4
    [4],  # 5
    [4, 7, 8],  # 6
    [6],  # 7
    [6], # 8
    [10],  # 9
    [9]  # 10
]
starts = [0, 3, 9]
finish = 8


def my_graf(v):
    visited = [False] * (len(graph))

    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                dfs(w)
    dfs(v)
    if visited[finish]:
        return print(f'Из точки {v} можно дойти до финиша')
    else:
        return print(f'Из точки {v} нельзя дойти до финиша')


for var in starts:
    my_graf(var)
