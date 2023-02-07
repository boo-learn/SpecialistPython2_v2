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

home = 0
bank = 7
shop = 2
maze_3_sol = dfs(maze_3, home)
print(maze_3_sol)

if maze_3_sol[bank]:
    print("Сan go to the bank")
if not maze_3_sol[bank]:
    print("Сan't go to the bank")
if maze_3_sol[shop]:
    print("Сan go to the shop")
if not maze_3_sol[shop]:
    print("Сan't go to the shop")
