# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение
graph1 = [
    # список смежности
    [1],  # 0
    [0, 2, 4],  # 1
    [1, 3, 4],  # 2
    [2],  # 3
    [1, 2, 5, 6],  # 4
    [4],  # 5
    [4, 7, 8],  # 6
    [6],  # 7
    [6],  # 8
    [10],  # 9
    [9]  # 10
]


def dfs_main(graph, start):
    visited = [False] * (len(graph))
    prev = [None] * (len(graph))

    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                dfs(w)

    dfs(start)
    return visited


print("Лабиринт 1")
finish = 8

start = 3
visit = dfs_main(graph1, start)
if visit[finish]:
    print(f"Из точки S-1({start}) можно дойти до финиша ({finish})")
else:
    print(f"Из точки S-1({start}) нельзя дойти до финиша ({finish})")


start = 0
visit = dfs_main(graph1, start)
if visit[finish]:
    print(f"Из точки S-2({start}) можно дойти до финиша ({finish})")
else:
    print(f"Из точки S-2({start}) нельзя дойти до финиша ({finish})")

start = 9
visit = dfs_main(graph1, start)
if visit[finish]:
    print(f"Из точки S-3({start}) можно дойти до финиша ({finish})")
else:
    print(f"Из точки S-3({start}) нельзя дойти до финиша ({finish})")
# print(visit)
print("\nЛабиринт 2")

graph2 = [
    # список смежности
    [],  # 0
    [2, 4, 5],  # 1
    [1, 3, 4],  # 2
    [2],  # 3
    [1, 2, 5, 6],  # 4
    [1, 4],  # 5
    [4, 7, 8],  # 6
    [6],  # 7
    [6],  # 8
    [10],  # 9
    [9]  # 10
]


start = 9
visit = dfs_main(graph2, start)
if visit[finish]:
    print(f"Из точки S-1({start}) можно дойти до финиша ({finish})")
else:
    print(f"Из точки S-1({start}) нельзя дойти до финиша ({finish})")


start = 3
visit = dfs_main(graph2, start)
if visit[finish]:
    print(f"Из точки S-2({start}) можно дойти до финиша ({finish})")
else:
    print(f"Из точки S-2({start}) нельзя дойти до финиша ({finish})")

start = 0
visit = dfs_main(graph2, start)
if visit[finish]:
    print(f"Из точки S-3({start}) можно дойти до финиша ({finish})")
else:
    print(f"Из точки S-3({start}) нельзя дойти до финиша ({finish})")

start = 7
visit = dfs_main(graph2, start)
if visit[finish]:
    print(f"Из точки S-4({start}) можно дойти до финиша ({finish})")
else:
    print(f"Из точки S-4({start}) нельзя дойти до финиша ({finish})")
