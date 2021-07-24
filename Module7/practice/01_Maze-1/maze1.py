# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1, 5], # 0
    [5, 0], # 1
    [6], # 2
    [7], # 3
    [5, 8], # 4
    [1, 4], # 5
    [2, 10], # 6
    [3], # 7
    [4, 9, 12], # 8
    [8, 10], # 9
    [6, 9, 11, 14], # 10
    [10], # 11
    [8], # 12
    [], # 13
    [10, 15], # 14
    [14], # 15
]

# Решите задачу и выведите ответ в нужном формате
visited = [False] * (len(graph))
start = 0


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


dfs(start)

print(visited)

marker = []

    
count = -1
for i in range(len(visited)):
    count += 1
    if visited[i]:
        print(f"Из точки 0 можно дойти до точки {count}")
    if visited[i]==False:
        print(f"Из точки 0 нельзя дойти до точки {count}")
