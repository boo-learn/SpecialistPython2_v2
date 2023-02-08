maze_with_treasures = [
    [1, 4],    # 0
    [0, 2],    # 1
    [1],    # 2
    [7],    # 3
    [0],    # 4
    [6, 9],    # 5
    [5, 10],    # 6
    [3, 11],  # 7
    [9, 12],    # 8
    [8, 5, 10],    # 9
    [9, 6, 14],    # 10
    [7],    # 11
    [8],    # 12
    [],    # 13
    [10, 15],    # 14
    [14]     # 15
]

start = 3
treasure_indexes = {1: 1, 2: 2, 4: 3, 6: 5,
                    7: 3, 9: 5, 10: 3, 13: 8, 14: 4, 15: 7}
visited = dfs(maze_with_treasures, start)
treasure_sum = 0
for index, value in treasure_indexes.items():
    if visited[index]:
        treasure_sum += value

print(f"Из точки '{start}' можно собрать сокровищ на сумму: {treasure_sum}")
