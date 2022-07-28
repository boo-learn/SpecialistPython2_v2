# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
import p as p

graph = [
    # список смежности
    [1],  # 0
    [0, 2],  # 1
    [1, 3],  # 2
    [2, 7],  # 3
    [5],  # 4
    [4, 6],  # 5
    [5],  # 6
    [3, 11],  # 7
    [9, 12],  # 8
    [8, 10],  # 9
    [9, 11],  # 10
    [7, 10, 15],  # 11
    [8, 13],  # 12
    [12, 14],  # 13
    [13],  # 14
    [11],  # 15
]

points = [
    {
        'name': 'S-1',
        'position': 1
    },
    {
        'name': 'S-2',
        'position': 5
    },
    {
        'name': 'S-3',
        'position': 15
    },
    {
        'name': 'F',
        'position': 14
    }
]


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


for finish_p in points:
    if finish_p['name'] == 'F':
        print(f"Проверяем точку {finish_p['name']}[{finish_p['position']}]")
        for start in points:
            if start['name'] != 'F':
                visited = [False] * (len(graph))
                dfs(start['position'])
                if visited[finish_p['position']]:
                    print(f" + В точку финиша {finish_p['name']}[{finish_p['position']}] добраться из точки {start['name']}[{start['position']}] можно")
                else:
                    print(f" - В точку финиша {finish_p['name']}[{finish_p['position']}] добраться из точки {start['name']}[{start['position']}] нельзя")


