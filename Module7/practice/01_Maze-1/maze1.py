# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],                # 0
    [0, 5],             # 1
    [6],                # 2
    [7],                # 3
    [5, 8],             # 4
    [4, 1],             # 5
    [2, 10],            # 6
    [3],                # 7
    [4, 9, 12],         # 8
    [8, 10],            # 9
    [9, 6, 11, 14],     # 10
    [10],               # 11
    [8],                # 12
    [],                 # 13
    [10, 15],           # 14
    [14]                # 15
]

start = 0
lengths = [None] * (len(graph))
lengths[start] = 0
# print(lengths)
queue = [start]
# print([start])
while queue:
    cur_vertex = queue.pop(0)
    for vertex in graph[cur_vertex]:
        if lengths[vertex] is None:
            lengths[vertex] = lengths[cur_vertex] + 1
            queue.append(vertex)

for i in range(len(lengths)):
    print(f'Из точки S-{i} {"можно" if str(lengths[i]) != "None" else "нельзя"} дойти до финиша')

# print(lengths)
# visited = [False] * (len(graph))
# start = 0
#
#
# def dfs(v):
#     visited[v] = True
#     for w in graph[v]:
#         if not visited[w]:  # посещён ли текущий сосед?
#             dfs(w)
# dfs(start)
# print(visited)
# Решите задачу и выведите ответ в нужном формате
