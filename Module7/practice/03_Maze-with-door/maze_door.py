# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.


# Решите задачу и выведите ответ в нужном формате
import p as p

graph = [
    # список смежности
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [None],  # 13
    [None],  # 14
    [11],  # 15
]

points = [
    {
        'name': 'S-1',
        'position': 5
    },
    {
        'name': 'S-2',
        'position': 13
    },
    {
        'name': 'S-3',
        'position': 3
    },
    {
        'name': 'S-4',
        'position': 8
    },
    {
        'name': 'F',
        'position': 0
    },
    {
        'name': 'K',
        'position': 7
    },
    {
        'name': 'K',
        'position': 10
    },
    {
        'name': 'D',
        'colour': 'green',
        'from': 4,
        'to': 5
    },
    {
        'name': 'D',
        'colour': 'green',
        'from': 12,
        'to': 13
    },
    {
        'name': 'D',
        'colour': 'green',
        'from': 14,
        'to': 15
    }
]


def dfs(v, _graph):
    visited[v] = True
    for w in _graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w, _graph)

def doors_open(_graf, key_colour):
    for doors in points:
        if doors['name'] == 'D':  # ищем список дверей, с ключом цвета key_colour
            if doors['colour'] == key_colour:
                #добавляем в _graf новые связи
                _graf[doors['from']].append(doors['to'])
                _graf[doors['to']].append(doors['from'])
                print(f'opened doors from {doors["from"]} to {doors["to"]}!')

    return _graf



visited = [False] * (len(graph))
graph_doors_open = []
graph_doors_open = doors_open(graph, 'green')


for finish_p in points:
    if finish_p['name'] == 'F':
        print(f"Проверяем точку {finish_p['name']}[{finish_p['position']}]")
        for start in points:
            if start['name'][:1:] == 'S':

                visited = [False] * (len(graph))
                dfs(start['position'], graph)           # первый проход по графу с закрытыми дверями
                for keys in points:
                    if keys['name'] == 'K' and visited[keys['position']]:       # проходили хотя бы раз по ключам
                        visited = [False] * (len(graph))
                        graph_doors_open = doors_open(graph)
                        dfs(start['position'], graph_doors_open)  # первый проход по графу с закрытыми дверями
                        break                               # прекращаем проход, если нашли хотя бы 1 ключ

                if visited[finish_p['position']]:
                    print(f" + В точку финиша {finish_p['name']}[{finish_p['position']}] добраться из точки {start['name']}[{start['position']}] можно")
                else:
                    print(f" - В точку финиша {finish_p['name']}[{finish_p['position']}] добраться из точки {start['name']}[{start['position']}] нельзя")


