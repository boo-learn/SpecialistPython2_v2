# "Лабиринт с сокровищами"
# см. Картинку на гугло-диске в Модуле-7
# T - сокровища(Treasure)
# Определите:
# Сколько сокровищ можно собрать, стартовав из каждой из предложенных точек?
# Стартовав из какой точки можно собрать максимальное количество сокровищ?
# Стартовав из каких точек, можно собрать максимальное количество сокровищ и дойти до выхода(F)?


treasure_labyrinth = [
    [1, 8, 11],     # 0
    [0],            # 1
    [7],            # 2
    [4],            # 3
    [3],            # 4
    [6],            # 5
    [5, 7],         # 6
    [2, 6],         # 7
    [0],            # 8
    [10, 11],       # 9
    [9],            # 10
    [0, 9],         # 11
]
entrypoints = [
    {'name': 'P-1', 'point': 1},
    {'name': 'P-2', 'point': 2},
    {'name': 'P-3', 'point': 3},
    {'name': 'P-4', 'point': 9},
]
treasures = [4, 5, 6, 7, 10, 11]
finish = 8


def find_a_way(start=0, finish=0, graph=None, check_all=False):
    visited = [False] * (len(graph))
    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                dfs(w)
    dfs(start)
    if check_all:
        return visited
    return visited[finish]


def get_labyrinth_data(entrypoints, finish, treasures, treasure_labyrinth):
    res = []
    for entry in entrypoints:
        to_finish = find_a_way(start=entry['point'], finish=finish, graph=treasure_labyrinth)
        founded_treasures = 0
        for treasure in treasures:
            to_treasure = find_a_way(start=entry['point'], finish=treasure, graph=treasure_labyrinth)
            if to_treasure:
                founded_treasures += 1
        res.append({'point': entry, 'treasures': founded_treasures, 'finished': to_finish})
    return res


def humanize_results(data):
    finished = ''
    max_treasures = {'point': {'name': None,}, 'treasures': -1}
    for d in data:
        expression = f"Стартовав из точки {d['point']['name']} можно собрать {d['treasures']} сокровищ и "

        if d['finished']:
            finished += f"{d['point']['name']} собрав {d['treasures']} сокровищ, "
            expression += 'добраться до финиша'
        else:
            expression += 'не добраться до финиша'

        if d['treasures'] > max_treasures['treasures']:
            max_treasures = d

        print(expression)
    print()
    finished = finished[:-2]
    print(f'До финиша добрались {finished}')
    print(f"Больше всего сокровищ в количестве {max_treasures['treasures']} штук(и) собрал "
          f"{max_treasures['point']['name']}")


if __name__ == '__main__':
    data = get_labyrinth_data(entrypoints, finish, treasures, treasure_labyrinth)
    humanize_results(data)
