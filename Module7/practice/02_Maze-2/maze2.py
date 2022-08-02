from DFS_and_bfs import dfs
graph = [
    [1], #0
    [0,1], #1
    [1,3], #2
    [2,7], #3
    [5], #4
    [4,6], #5
    [5], #6
    [3,11], #7
    [12,9], #8
    [8,10], #9
    [9,11], #10
    [7,15,10], #11
    [8,13], #12
    [14,12], #13
    [13], #14
    [11], #15
    
]    

start_vertex = 4

finish = 15


path = dfs(graph,start_vertex)

if path[finish]:
    print (f"Из точки {start_vertex = } можно дойти до финиша")
else :
    print (f"Из точки {start_vertex = } нельзя дойти до финиша")
