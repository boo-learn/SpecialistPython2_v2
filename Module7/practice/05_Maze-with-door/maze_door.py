graph = [
    [1],         # 0
    [0, 5],      # 1
    [6],         # 2
    [7],         # 3 точка старта S3
    [8],         # 4 дверь
    [1],         # 5 точка старта S1
    [2, 10],     # 6
    [3, 11],     # 7 ключ
    [4, 9, 12],  # 8 точка финиша S4
    [8, 10],     # 9
    [9, 6],      # 10 ключ
    [7, 15],     # 11
    [8],         # 12 дверь
    [13],        # 13 точка старта S2
    [14],        # 14
    [11],        # 15 дверь
]

def dfs(graph, start, end, visited=None, has_key=False):
    if visited is None:
        visited = set()
    if start == end:
        return True, has_key
    visited.add(start)
    if start in [7, 10]:
        has_key = True
    for neighbor in graph[start]:
        if neighbor not in visited:
            if neighbor in [4, 12, 15]:
                if has_key:
                    success, _ = dfs(graph, neighbor, end, visited.copy(), has_key)
                    if success:
                        return True, has_key
            else:
                success, _ = dfs(graph, neighbor, end, visited.copy(), has_key)
                if success:
                    return True, has_key
    return False, has_key

start_points = [3, 5, 13]
finish_point = 0

for start_point in start_points:
    can_reach_finish, has_key = dfs(graph, start_point, finish_point)
    if can_reach_finish and has_key:
        print(f"Из точки S-{start_point} можно добраться до финиша, используя ключ")
    elif can_reach_finish:
        print(f"Из точки S-{start_point} можно добраться до финиша без ключа")
    else:
        print(f"Из точки S-{start_point} нельзя добраться до финиша")
