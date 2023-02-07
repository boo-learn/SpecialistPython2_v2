maze_2 = [
    [], # 0
    [2], # 1
    [1], # 2
    [], # 3
    [7,5], # 4
    [4], # 5
    [7], # 6
    [4,6], # 7
    [] # 8
]

home = 7
bank = 2
maze_2_sol = dfs(maze_2, home)
print(maze_2_sol)

if maze_2_sol[bank]:
    print("Сan go to the bank")
if not maze_2_sol[bank]:
    print("Сan't go to the bank")
