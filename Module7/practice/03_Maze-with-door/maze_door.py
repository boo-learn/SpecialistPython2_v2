# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md

from DFS_and_bfs import dfs

graph_close_door = [
    [1],  # 0
    [0,5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2,10],  # 6
    [3,11],  # 7
    [9,4,12],  # 8
    [8,10],  # 9
    [6,9],  # 10
    [7,15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11],  # 15
]

graph_open_door = [
    [1],  # 0
    [0,5],  # 1
    [6],  # 2
    [7],  # 3
    [8,5],  # 4
    [1,4],  # 5
    [2,10],  # 6
    [3,11],  # 7
    [9,4,12],  # 8
    [8,10],  # 9
    [6,9],  # 10
    [7,15],  # 11
    [8,13],  # 12
    [12],  # 13
    [15],  # 14
    [11,14],  # 15
]


starts = {'S-1': 5, 'S-2': 13, 'S-3': 3, 'S-4': 8}

finish = 0

key = (10,7)

result1 = dfs(graph_close_door, finish)

result2 = dfs(graph_open_door, finish)

key1 = dfs(graph_close_door, key[0])

key2 = dfs(graph_close_door, key[1])

for point_name, point_value in starts.items():
    if result1[point_value]:
        print(f'Из точки {point_name} можно дойти до финиша без ключа')
    elif key1[point_value] or key1[point_value]:
        if result2[point_value]:
            print(f'Из точки {point_name} можно дойти до финиша , используя ключ')
    else:
        print(f'Из точки {point_name} нельзя дойти до финиша')
