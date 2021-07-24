graph= [
#     # список смежности
    [1,4],         # 0
    [0,2],   # 1
    [1],         # 2
    [7],      # 3
    [0],         # 4
    [6,9],      # 5
    [5,10],            # 6
    [3,11],             # 7
    [9,12],             # 8
    [8,5,10],             # 9
    [6,9,14],             # 10
    [7],             # 11
    [8],             # 12
    [],             # 13
    [10,15],            # 14
    [14]             # 15    
]
treas = {1:1,2:2,4:3,6:5,7:4,9:5,10:3,13:8,14:4,15:7}
start_points = {0: 'S-1', 12: 'S-2', 3: 'S-3'}


# 
for start_point in start_points.keys():
     visited = dfs(start_point, graph)
     all_tres = []
     for trea in treas.keys():
         if visited[trea]:
             all_tres.append(treas[trea])
     all_tres.sort('key:Reverse')
     mytres = sum(all_tres[:2])
     print(f'Из точки {start_points[start_point]} можно собрать {mytres}')
