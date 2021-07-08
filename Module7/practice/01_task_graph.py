graph = [ # список смежности
[1],        # 0
[0, 2, 4],  # 1
[1, 3, 4],  # 2
[2],        # 3
[1, 2, 5, 6], # 4
[4],        # 5
[4, 7, 8],  # 6
[6],        # 7
[6],        # 8
[10],       # 9
[9]]        # 10

visited = [False] * (len(graph))

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)

start = 3
dfs(start)
print('Из точки S-1 можно дойти до финиша' if visited[8]
else 'Из точки S-1 нельзя дойти до финиша')

visited = [False] * (len(graph))
start = 0
dfs(start)
print('Из точки S-2 можно дойти до финиша' if visited[8]
else 'Из точки S-2 нельзя дойти до финиша')

visited = [False] * (len(graph))
start = 9
dfs(start)
print('Из точки S-3 можно дойти до финиша' if visited[8]
else 'Из точки S-3 нельзя дойти до финиша')

