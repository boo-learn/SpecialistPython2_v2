graph = [
    [1],         # 0
    [5],         # 1
    [6],         # 2
    [7],         # 3
    [5, 8],      # 4
    [1, 4],      # 5
    [2, 10],     # 6
    [3],         # 7
    [4, 9, 12],  # 8
    [8, 10],     # 9
    [6, 9, 11, 14],  # 10
    [10],        # 11
    [8],         # 12
    [],          # 13
    [10, 15],    # 14
    [14]         # 15
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
s1_start = 0
if check_reachability(s1_start, finish_point):
    print("Из точки S-1 можно дойти до финиша")

s2_start = 12
if check_reachability(s2_start, finish_point):
    print("Из точки S-2 можно дойти до финиша")

s3_start = 3
if check_reachability(s3_start, finish_point):
    print("Из точки S-3 можно дойти до финиша")
