# DFS(Depth-First Search) - поиск в глубину
# Позволяет построить обход ориентированного или неориентированного графа,
# при котором посещаются все вершины, доступные из начальной вершины.

# Алгоритм обхода в глубину:
# 1. Пойти в какую-нибудь смежную вершину, не посещенную ранее.
# 2. Запустить из этой вершины алгоритм обхода в глубину
# 3. Вернуться в начальную вершину.
# 4. Повторить пункты 1-3 для всех не посещенных ранее смежных вершин.

#         3 --5--2   6--7
#        / \ /  /
#       0---1--4

def dfs(graph, graph_doors, start, keys, with_key=False):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True

        if with_key:
            if v in keys:
                for door in graph_doors:
                    graph[door[0]].append(door[1])
                    graph[door[1]].append(door[0])

        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start)
    return visited

def main():
    graph = [
        # список смежности
        [1],  # 0
        [0, 5],  # 1
        [6],  # 2
        [7],  # 3
        [8],  # 4
        [1],  # 5
        [2, 10],  # 6
        [3, 11],  # 7
        [4, 9, 12],  # 8
        [8, 10],  # 9
        [9, 6],  # 10
        [7, 15],  # 11
        [8],  # 12
        [],  # 13
        [],  # 14
        [11]  # 15
    ]

    graph_doors = [
        [4, 5],     #d0
        [12, 13],   #d1
        [14, 15]    #d2
    ]
    keys = [10, 7]


    start = {'s-1': 5, 's-2': 13, 's-3': 3, 's-4': 8}
    finish_point = 0
    for i in [True, False]:
        text = 'with key' if i else 'without key'
        print(text)
        for i in start:
            visited = dfs(graph, graph_doors, start[i], keys, i)
            if visited[finish_point]:
                print(f'Из точки {i} можно дойти до финиша')
                continue
            print(f'Из точки {i} нельзя дойти до финиша')

main()
