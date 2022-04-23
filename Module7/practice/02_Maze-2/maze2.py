def dfs(start_point, graph):
    visited_list = [False] * (len(graph))

    def _dfs(v):
        visited_list[v] = True
        for w in graph[v]:
            if not visited_list[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(start_point)
    return visited_list


def find_ways(start_points, finish_point, graph):
    for key, value in start_points.items():
        visited = dfs(value, graph)
        if visited[finish_point]:
            print(f"Из точки {key} можно дойти до финиша")
        else:
            print(f"Из точки {key} нельзя дойти до финиша")
# Опишите список смежности по изображению лабиринта из файла task.md


if __name__ == "__main__":
    graph = [
        [1],  # 0
        [0, 2],  # 1
        [1, 3],  # 2
        [7],  # 3
        [5],  # 4
        [6, 4],  # 5
        [5],  # 6
        [3, 11],  # 7
        [9, 12],  # 8
        [8, 10],  # 9
        [9, 11],  # 10
        [7, 10, 15],  # 11
        [8, 13],  # 12
        [12, 14],  # 13
        [13],  # 14
        [11]  # 15
    ]
    start_points = {"S-1": 1, "S-2": 5, "S-3": 15}
    finish_point = 14
    find_ways(start_points, finish_point, graph)
