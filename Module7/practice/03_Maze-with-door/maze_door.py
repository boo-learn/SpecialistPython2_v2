graphopen = [
#     # список смежности
    [1],         # 0
    [0,5],   # 1
    [6],         # 2
    [7],      # 3
    [5,8],         # 4
    [1,4],      # 5
    [2,10],            # 6
    [3,11],             # 7
    [4,12,9],             # 8
    [8,10],             # 9
    [6,9],             # 10
    [7,15],             # 11
    [8,13],             # 12
    [12],             # 13
    [15],            # 14
    [14,11]             # 15    
]
graphclose = [
#     # список смежности
    [1],         # 0
    [0,5],   # 1
    [6],         # 2
    [7],      # 3
    [8],         # 4
    [1],      # 5
    [2,10],            # 6
    [3,11],             # 7
    [4,12,9],             # 8
    [8,10],             # 9
    [6,9],             # 10
    [7,15],             # 11
    [8],             # 12
    [],             # 13
    [],            # 14
    [11]             # 15    
]

keys = [7,10]
finish = 0

start_points = {5: 'S-1', 13: 'S-2', 3: 'S-3',8: 'S-4'}

for start_point in start_points.keys():
    visited = dfs(start_point, graphclose)
    if visited[finish]:
        print(f'Из точки {start_points[start_point]} можно дойти до финиша без ключа')
    else:
        use_key = False
        for key in keys:
             if visited[key]:
                 use_key = True
                 break
        if use_key:
            visited = dfs(start_point, graphopen)
            if visited[finish]:
                print(f'Из точки {start_points[start_point]} можно дойти до финиша c ключом')
            else:
                print(f'Из точки {start_points[start_point]} нельзя дойти до финиша даже с ключом')
        else:
            print(f'Из точки {start_points[start_point]} нельзя дойти до финиша')
           
