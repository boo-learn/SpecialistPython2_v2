# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

def gen_list(size, at=1, to=1000):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    return [random.randint(at, to) for _ in range(size)]


# Проверку что N больше 1 не делал
stones = gen_list(2)
print(stones)
stones.sort()

heap1 = stones[::2]
heap2 = stones[1::2]
weight1 = sum(heap1)
weight2 = sum(heap2)
print('heap1', heap1)
print('heap2', heap2)
rel = weight1 / weight2
if rel < 1:
    rel = 1 / rel

if rel > 2:
    print('Вес отличается более чем в 2 раза')
else:
    print('Вес отличается в', rel, 'раз')
