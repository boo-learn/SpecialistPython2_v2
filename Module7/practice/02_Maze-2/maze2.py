graph2 = [
    [1], # 0
    [0, 2], # 1
    [1,3], # 2
    [2,7], # 3
    [5], # 4
    [4,6], # 5
    [5], # 6
    [3,11], # 7
    [9,12], # 8
    [8, 10], # 9
    [9, 11], # 10
    [7,10,15], # 11
    [8,13], # 12
    [12,14], # 13
    [13], # 14
    [11], # 15
]
s1 = 1
s2 = 5
s3 = 15
start_point_list = [s1, s2, s3]
for start_point in start_point_list:
    if dfs(start_point, graph2)[14] == True:
        print(f'Из точки S - {start_point} можно дойти до финиша')
    else:
        print(f'Из точки S - {start_point} нельзя дойти до финиша')

for start_point in start_point_list:
    if bfs(start_point, graph2)[14] != None:
        print(f'Из точки S - {start_point} можно дойти до финиша')
    else:
        print(f'Из точки S - {start_point} нельзя дойти до финиша')
