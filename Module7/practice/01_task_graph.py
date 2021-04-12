# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение
labyrinth = [
    [1],            # 0
    [2, 4],         # 1
    [1, 3, 4],      # 2
    [2],            # 3
    [1, 2, 5, 6],   # 4
    [4],            # 5
    [4, 7, 8],      # 6
    [6],            # 7
    [6],            # 8
    [10],           # 9
    [9],            # 10
]


def find_a_way(start=0, finish=0, graph=[], check_all=False):
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


if __name__ == '__main__':
    start = 3
    finish = 8
    visited = find_a_way(start, finish, labyrinth)
    if visited:
        print(f'Если начать с узла: {start}, то до {finish} добраться возможно')
    else:
        print(f'Если начать с узла: {start}, то до {finish} добраться невозможно')

    start = 9
    finish = 10
    visited = find_a_way(start, finish, labyrinth)
    if visited:
        print(f'Если начать с узла: {start}, то до {finish} добраться возможно')
    else:
        print(f'Если начать с узла: {start}, то до {finish} добраться невозможно')

    start = 3
    finish = 10
    visited = find_a_way(start, finish, labyrinth)
    if visited:
        print(f'Если начать с узла: {start}, то до {finish} добраться возможно')
    else:
        print(f'Если начать с узла: {start}, то до {finish} добраться невозможно')

    # Проверяем сразу все точки:
    visited = find_a_way(finish=8, graph=labyrinth, check_all=True)
    print(f'До финиша можно добраться из таких точек:\n{visited}')
