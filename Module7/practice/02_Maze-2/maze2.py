graph = [
    [1],             # 0
    [2],             # 1
    [1, 3],          # 2
    [2, 7],          # 3
    [5],             # 4
    [4, 6],          # 5
    [5],             # 6
    [3, 11],         # 7
    [9, 12],         # 8
    [8, 10],         # 9
    [9, 11],         # 10
    [7, 10, 15],     # 11
    [8, 13],         # 12
    [12, 14],        # 13
    [13],            # 14
    [11]             # 15
]

visited = [False] * len(graph)


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


def check_reachability(start, finish):
    global visited
    visited = [False] * len(graph)
    dfs(start)

    return visited[finish]


finish_point = 14
s1_start = 1
if check_reachability(s1_start, finish_point):
    print("Из точки S-1 можно дойти до финиша")

s2_start = 5
if check_reachability(s2_start, finish_point):
    print("Из точки S-2 можно дойти до финиша")

s3_start = 15
if check_reachability(s3_start, finish_point):
    print("Из точки S-3 можно дойти до финиша")
