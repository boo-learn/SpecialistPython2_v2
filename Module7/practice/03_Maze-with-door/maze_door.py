# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


# Решите задачу и выведите ответ в нужном формате
graph_close = [
    [1],     #0
    [0,5],     #1
    [6],     #2
    [7],     #3
    [8],     #4
    [1],     #5
    [2,10],     #6
    [3],     #7
    [4,9,12],         #8
    [8,10],           #9
    [6,9],     #10
    [7,15],     #11
    [8],     #12
    [],     #13
    [],     #14
    [11],     #15
]

graph_open = [
    [1],     #0
    [0,5],     #1
    [6],     #2
    [7],     #3
    [5,8],     #4
    [1,4],     #5
    [2,10],     #6
    [3],     #7
    [4,9,12],         #8
    [8,10],           #9
    [6,9],     #10
    [7,15],     #11
    [8,13],     #12
    [12],     #13
    [15],     #14
    [11,14],     #15
]

starts = {'S-1': 5, 'S-2': 13, 'S-3': 3, 'S-4': 8}
finish = 0
keys = [7, 10]
key_success = []

result_close = dfs(graph_close, finish)
result_open = dfs(graph_open, finish)

for point_name, point_value in starts.items():
    key_success = []
    if result_close[point_value]:
        print(f'Из точки {point_name} можно дойти до финиша')
    else:
        to_keys = dfs(graph_close, point_value)
        for key in keys:
            key_success.append(to_keys[key])
        if result_open[point_value] and True in key_success:
            print(f'Из точки {point_name} можно дойти до финиша с ключом')
        else:
            print ( f'Из точки {point_name} нельзя дойти до финиша' )
