# Сюда отправляем решение задачи "Лабиринт с сокровищами"


def dfs(graph, start_point):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


graph = [[1, 4], [0, 2], [1], [7],
         [0], [6, 9], [5, 10], [3, 11],
         [9, 12], [5, 8, 10], [6, 9, 14], [7],
         [8], [], [10, 15], [14]
         ]
start_points = {'S-1': 0,
                'S-2': 12,
                'S-3': 3,
                }
treasures = {1: 1,
             2: 2,
             4: 3,
             6: 5,
             7: 3,
             9: 5,
             10: 3,
             13: 8,
             14: 4,
             15: 7,
             }
treasures_list = [treasures.get(v, 0) for v in range(len(graph))]

for start_name, start in start_points.items():
    can_visited = dfs(graph, start)
    treasures_sum = sum([value * is_visited for value, is_visited in zip(treasures_list, can_visited)])
    print(f'Из точки {start_name}({start}) можно собрать сокровищ суммарной ценностью {treasures_sum}')
