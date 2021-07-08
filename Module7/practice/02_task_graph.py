# "Лабиринт с ключем"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - стартовые точки
# Посетив клетку K, можно подобрать ключ, который отпирают любую дверь.
# Определите:
# Из каких точек можно добраться до точки F?
# Какую дверь нужно открыть, чтобы добраться до точки P-2?

from pprint import pprint

graph_unlocked = [
    [9, 1],       # 0
    [0, 2, 4, 9], # 1
    [1, 8, 11], # 2
    [10],       # 3
    [1, 5],     # 4
    [4],        # 5
    [7],        # 6
    [6, 8],     # 7
    [2, 7],     # 8
    [0, 1, 12], # 9
    [3],        # 10
    [2],        # 11
    [9]         # 12
]

start_nodes = [0, 4, 7, 10, 11, 12]
finish = 6
key = 5
doors = [8, 9]


def gen_locked_graph(full_graph, doors):
    graph = [node[:] for node in full_graph]
    for node in graph:
        if graph.index(node) in doors:
            node = []
        for link in node:
            if link in doors:
                node.remove(link)
    pprint(graph)
    return graph


def dfs(gr, strt):

    def dfsr(v, gr):
        visited[v] = True
        for w in gr[v]:
            if not visited[w]:
                dfsr(w, gr)
    visited = [False] * (len(gr))
    dfsr(strt, gr)
    return visited


graph_locked = gen_locked_graph(graph_unlocked, doors)
for sn in start_nodes:
    visited = dfs(graph_locked, sn)
    if visited[finish]:
        print(f"Reached node {finish}(finish) without key({key}) from node {sn}.")
    else:
        if visited[key]:
            print(f"Visited key({key}) from node {sn}.")
            visited = dfs(graph_unlocked, sn)
            #for i, v in enumerate(visited): print(i, v)
            if visited[finish]:
                print(f"Reached node {finish}(finish) with key({key}) from node {sn}.")
            else:
                print(f"Can'treach  node {finish}(finish) with key({key}) from node {sn}.")
        else:
            print(f"Can't reach neither key({key}) nor finish({finish}) from node {sn}.")
