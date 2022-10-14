from dfs import dfs, bfs

graph = [

       [1],  #0
        [0,5], #1
        [6], #2
        [7], #3
        [5,8], #4
        [1,4],  #5
        [2, 10], #6
        [3], #7
        [4, 9, 12], #8
        [8,10], #9
        [6, 9, 11, 14], #10
        [10], #11
        [8], #12
        [], #13
        [10, 15],#14
        [14] #15

]

print(bfs(0, graph))
print(bfs(12, graph))
print(bfs(3, graph))
n = int(input())
if not(bfs(n, graph)[14] is None):
 print(f'Из точки {n} можно дойти до финиша')
else:
 print(f'Из точки {n} нельзя дойти до финиша')
