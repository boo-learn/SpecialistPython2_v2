maze_1 =  [
    [3], # 0
    [2], # 1
    [1], # 2
    [0], # 3
    [7], # 4
    [8], # 5
    [7], # 6
    [4,6], # 7
    [5] # 8
]
home = 0
bank = 7
maze_1_sol = dfs(maze_1, home)
print(maze_1_sol)

if maze_1_sol[bank]:
    print("Сan go to the bank")
if not maze_1_sol[bank]:
    print("Сan't go to the bank")
