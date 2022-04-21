# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.
def stones(stones_heap):
    flag = False
    stones_heap.sort(reverse=True)
    stones_heap_1 = stones_heap.copy()
    stones_heap_2 = [stones_heap_1.pop()]
    while len(stones_heap_1) != 0:
        if 0.5 <= sum(stones_heap_1) / sum(stones_heap_2) <= 2:
            flag = True
            break
        stones_heap_2.append(stones_heap_1.pop())
    if flag:
        print(f'Первая куча {stones_heap_1}, суммарный вес камней {sum(stones_heap_1)}')
        print(f'Вторая куча {stones_heap_2}, суммарный вес камней {sum(stones_heap_2)}')
    else:
        print('Разбиение невозможно')


stones_heap = [500, 200, 100, 1000]
stones(stones_heap)
