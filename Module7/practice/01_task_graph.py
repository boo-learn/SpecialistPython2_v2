# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение
#dear python here is my graph and its relationships
graph = [
    # список смежности
    [1, 4],  # 0
    [0, 2, 4],  # 1
    [1,3],  # 2
    [2],  # 3
    [1, 5, 6],  # 4
    [4],  # 5
    [7,8],  # 6
    [6],  # 7
    [6],  #8
    [10], #9
    [9]  #10
]
#start at station 3
start = 3
#then please find the shortest path to segment 8, thank you

#using plagarized code it'll be...
lengths = [None] * (len(graph))
lengths[start] = 3
queue = [start]
while queue:
    cur_vertex = queue.pop(0)
    for vertex in graph[cur_vertex]:
        if lengths[vertex] is None:
            lengths[vertex] = lengths[cur_vertex] + 1
            queue.append(vertex)
        else:
        #please print in a separate new list that's called 'path not chosen'
            path_not_chosen[]
        #Forgot how to make lists
            append.path_not_chosen()
            print("path not chosen:    ", path_not_chosen)
print(lengths, "path chosen")
