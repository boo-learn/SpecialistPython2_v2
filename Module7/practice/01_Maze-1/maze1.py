# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md

def dfs(start_point, graph):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                _dfs(w)

    _dfs(start_point)
    return visited

def finish(finish_list, finish_point):
    if finish_list[finish_point]:
        return (f"Из точки {start_1} можно дойти до финиша")
    else:
        return (f"Из точки {start_1} нельзя дойти до финиша")

graph = [[1],             #0
         [0, 5],          #1
         [6],             #2
         [7],             #3
         [5, 8],          #4
         [1, 4],          #5
         [2, 10],         #6
         [3],             #7
         [4, 9, 12],      #8
         [8, 10],         #9
         [6, 9, 11, 14],  #10
         [10],            #11
         [8],             #12
         [],              #13
         [10, 15],        #14
         [14],            #15
]

start_1 = 0
start_2 = 3
start_3 = 12

finish_1 = dfs(start_1, graph)
finish_2 = dfs(start_2, graph)
finish_3 = dfs(start_3, graph)

f_1 = finish(finish_1, 14)
f_2 = finish(finish_2, 14)
f_3 = finish(finish_3, 14)

print(f"{f_1},\n{f_2},\n{f_3}")

