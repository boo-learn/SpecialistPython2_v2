maze_3 = [
    [3],  # 0
    [2],  # 1
    [1],  # 2
    [0],  # 3
    [7],  # 4
    [8],  # 5
    [7],  # 6
    [4, 6],  # 7
    [5]  # 8
]

interests_points = {
    "home": 0,
    "shop": 2,
    "bank": 7
}

visited = dfs(maze_3, interests_points["home"])
# print(visited)
for key, value in interests_points.items():
    if visited[value]:
        print(f"Сan go to the {key}")
    else:
        print(f"Сan't go to the {key}")
