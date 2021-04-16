# В 7-ом модуле мы изучали "алгоритм поиска в ширину(bfs)".
# Перепишите предложенный алгоритм, используя в качестве очереди класс "Очередь" из модуля collections
# collections.deque()


from collections import deque


graph = [
    # список смежности
    [1, 3],  # 0
    [0, 3, 4, 5],  # 1
    [4, 5],  # 2
    [0, 1, 5],  # 3
    [1, 2],  # 4
    [1, 2, 3],  # 5
    [7], # 6
    [6] # 7
]


def bfs(graph):
    start = 0
    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        cur_vertex = queue.popleft()
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)

    return lengths


if __name__ == '__main__':
    print('deque task')
    res = bfs(graph)
    print(res)
