# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
import p as p

graph = [
    # список смежности
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [None],  # 13
    [10, 15],  # 14
    [14],  # 15
]

points = [
    {
        'name': 'S-1',
        'position': 0
    },
    {
        'name': 'S-2',
        'position': 12
    },
    {
        'name': 'S-3',
        'position': 3
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


