# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


def possible(graph, start_vertex, end_vertex):
    if graph[end_vertex]:
        return f'Из точки {start_vertex} можно дойти до финиша'
    else:
        return f'Из точки {start_vertex} нельзя дойти до финиша'


# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
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
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15
]

# Решите задачу и выведите ответ в нужном формате
s1 = 0
s2 = 12
s3 = 3
end1 = 14

visited1 = dfs(graph, s1)
print(possible(visited1, s1, end1))

visited2 = dfs(graph, s2)
print(possible(visited2, s2, end1))

visited3 = dfs(graph, s3)
print(possible(visited3, s3, end1))
