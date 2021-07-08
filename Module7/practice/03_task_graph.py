# "Лабиринт с сокровищами"
# см. Картинку на гугло-диске в Модуле-7
# T - сокровища(Treasure)
# Определите:
# Сколько сокровищ можно собрать, стартовав из каждой из предложенных точек?
# Стартовав из какой точки можно собрать максимальное количество сокровищ?
# Стартовав из каких точек, можно собрать максимальное количество сокровищ и дойти до выхода(F)?

from pprint import pprint

graph = [
    [5],    # 0
    [9],    # 1
    [6],    # 2
    [4, 5], # 3
    [3],    # 4
    [0, 3, 10], # 5
    [2],    # 6
    [8],    # 7
    [7, 9], # 8
    [1, 8],    # 9
    [5]      # 10
]

start_nodes = {0: ["P-1",0, False], 1: ["P-2",0, False], 2: ["P-3",0, False], 3: ["P-4",0, False]}
treasure_nodes = [5, 6, 7, 8, 9]
finish = 10
TREASURE = 1
FINISH = 2

def dfs(gr, strt):

    def dfsr(v, gr):
        visited[v] = True
        for w in gr[v]:
            if not visited[w]:
                dfsr(w, gr)
    visited = [False] * (len(gr))
    dfsr(strt, gr)
    return visited


for index, lst in start_nodes.items():
    visited = dfs(graph, index)
    #print(visited)
    for i, visited_node in enumerate(visited):
        if visited_node and i in treasure_nodes:
            lst[TREASURE] += 1
    print(f"Gathered {lst[TREASURE]} treasure from {start_nodes[index]}")
    if visited[finish]:
        lst[FINISH] = True

print(start_nodes)



