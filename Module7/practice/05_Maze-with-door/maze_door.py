from copy import deepcopy

def dfs(graph: list, start_point: int) -> list[bool]:
    """
    Алгоритм поиска в глубину
    """
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited

region = [
    # список смежности
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],   # 8
    [10, 8],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11],  # 15
]

start_points = [('s-1', 5), ('s-2', 13), ('s-3', 3), ('s-4', 8)]
finish_point = 0
key_points = [7, 10]
doors = [(4, 5), (12, 13), (14, 15)]

for point_name, point_num in start_points:
    visited = dfs(region, start_point=point_num)
    if visited[finish_point]:
        print(f'Из точки {point_name} можно добраться до финиша без ключа')
    else:
        can_get_key = False
        for key_point in key_points:
            if visited[key_point]:
                can_get_key = True
                # opening doors
                region_doors_opened = deepcopy(region)
                for door in doors:
                    region_doors_opened[door[1]].append(door[0])
                    region_doors_opened[door[0]].append(door[1])
                visited = dfs(region_doors_opened, start_point=point_num)
                if visited[finish_point]:
                    print(f'Из точки {point_name} можно добраться до финиша, используя ключ')
                else:
                    print(f'Из точки {point_name} нельзя добраться до финиша')
                break
        if not can_get_key:
            print(f'Из точки {point_name} нельзя добраться до финиша')


# Решите задачу и выведите ответ в нужном формате
