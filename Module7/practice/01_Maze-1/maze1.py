# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    # список смежности
    [1],     # 0   Home
    [0,4],   # 1
    [5],     # 2
    [4,6],   # 3
    [1,3,5], # 4
    [2,4],   # 5
    [3],     # 6
    [8] ,    # 7  Bank
    [7]      # 8
]


Home = 0
Bank = 7
visited = dfs(graph, start_vertex=Home)
# print(visited)
if  visited[Bank]:
    print("Сan go to the bank")
else:
    print("Can't go to the bank")
