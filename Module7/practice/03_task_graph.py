#!/usr/bin

graph = [
    [8, 7], # 0
    [2], # 1
    [3, 1], # 2
    [2, 4], # 3
    [3], # 4
    [6], # 5
    [5], # 6
    [0, 8], # 7
    [7, 0, 9], # 8
    [8, 10], # 9
    [9] # 10
]

finish = 0
treasures = [2, 3, 4, 5, 10, 8]
P1 = 7
P2 = 1
P3 = 6
P4 = 9
starts_list = [P1, P2, P3, P4]
visited = [False] * (len(graph))

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


# 1. Сколько сокровищ можно собрать, стартовав из каждой из предложенных точек?

for start in starts_list:
    visited = [False] * (len(graph))
    dfs(start)
    treasure_num = 0
    for treasure in treasures:
        if visited[treasure]:
            treasure_num += 1
    print(f"Starting from point {start} {treasure_num} treasures can be collected")

# 2. Стартовав из какой точки можно собрать максимальное количество сокровищ?

maximum = 0
nums = {}
for start in starts_list:
    visited = [False] * (len(graph))
    dfs(start)
    treasure_num = 0
    for treasure in treasures:
        if visited[treasure]:
            treasure_num += 1
    if treasure_num > maximum:
        maximum = treasure_num
    nums[start] = treasure_num

print()
print("Maximum amount of treasures can be collected starting from points:")
for key in nums:
    if nums[key] == maximum:
        print(key)
# 3. Стартовав из каких точек, можно собрать максимальное количество сокровищ и дойти до выхода(F)?

def fin_dfs(v):
    fin_visited[v] = True
    for w in graph[v]:
        if not fin_visited[w]:  # посещён ли текущий сосед?
            fin_dfs(w)

maximum = 0
nums = {}
fin_visited = [False] * (len(graph))
fin_dfs(finish)

for start in starts_list:
    visited = [False] * (len(graph))
    dfs(start)
    treasure_num = 0
    for treasure in treasures:
        if visited[treasure]:
            treasure_num += 1
    if treasure_num > maximum and fin_visited[start]:
        maximum = treasure_num
    nums[start] = treasure_num

print()
print("Maximum amount of treasures can be collected and fin reached starting from points:")
for key in nums:
    if nums[key] == maximum:
        print(key)


