from DFS_and_bfs import dfs
graph = [
    [1], #0
    [0,5], #1
    [6], #2
    [7], #3
    [5,8], #4
    [1,4], #5
    [6,10], #6
    [3], #7
    [4,9,12], #8
    [8,10], #9
    [9,11,14,6], #10
    [10], #11
    [8], #12
    [], #13
    [10,15], #14
    [14], #15
    
]    

start_vertex = 12

finish = 15


path = dfs(graph,start_vertex)

if path[finish]:
    print (f"Из точки {start_vertex = } можно дойти до финиша")
else :
    print (f"Из точки {start_vertex = } нельзя дойти до финиша")


