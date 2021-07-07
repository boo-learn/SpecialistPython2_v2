# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.


def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    return [random.randint(at, to) for _ in range(size)]


def distribute(stones):
    print(stones)
    stones.sort(reverse=True)
    heap1 = []
    heap2 = []
    for stone in stones:
        if sum(heap1) < sum(heap2):
            heap1.append(stone)
            continue
        heap2.append(stone)
    print(f"heap1: {heap1}")
    print(f"heap2: {heap2}")

    ratio = sum(heap1) / sum(heap2)
    if ratio > 2 or ratio < 0.5:
        print("Невозможно поделить")
    else:
        print("Ок")


distribute([1, 1, 1, 1, 4])
print('***')
distribute([1, 1, 9, 9, 50])
print('***')
distribute(gen_list(7, 1, 10))
