maze = [
    [1],    # 0
    [0, 5],    # 1
    [6],    # 2
    [7],    # 3
    [8],    # 4
    [1],    # 5
    [2, 10],    # 6
    [3, 11],  # 7
    [4, 9, 12],    # 8
    [8, 10],    # 9
    [9, 6],    # 10
    [7, 15],    # 11
    [8],    # 12
    [],    # 13
    [],    # 14
    [11]     # 15
]

keys = [7, 10]
doors = [[14, 15], [4, 5], [12, 13]]
start = 14
finish = 0


def open_door(door: list) -> None:
    maze[door[0]].append(door[1])
    maze[door[1]].append(door[0])


way_to_finish = ""
visited = dfs(maze, start)

if not visited[finish]:
    visited_index = []
    for i in range(len(visited)):
        if visited[i]:
            visited_index.append(i)
    if (keys[0] in visited_index) or (keys[1] in visited_index):
        for door in doors:
            if (door[0] in visited_index) or (door[1] in visited_index):
                open_door(door)
                way_to_finish = ", используя ключ"
    visited = dfs(maze, start)
else:
    way_to_finish = " без ключа"

if visited[finish]:
    way_to_finish = f"Из точки '{start}' можно добраться до финиша" + way_to_finish
else:
    way_to_finish = f"Из точки '{start}' невозможно добраться до финиша"

print(way_to_finish)
