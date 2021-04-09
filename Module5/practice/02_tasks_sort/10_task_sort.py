# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

def bubble_sort(nums, key=lambda x: x, reverse=False):
    j = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - j - 1):
            if reverse:
                cond = key(nums[i]) < key(nums[i + 1])
            else:
                cond = key(nums[i]) > key(nums[i + 1])
            if cond:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    return nums


def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов вдиапазоне at..to 
    """
    random_list = [random.randint(at, to) for i in range(size)]
    return random_list


n = 5
stones = gen_list(n, at=1, to=3000)

print(stones)
sum_stone = sum(stones)
max_stone = max(stones)
if max_stone > sum_stone * 2 // 3:
    print('Кучи разбить нельзя')
else:
    stones_sort = bubble_sort(stones)
    i = 0
    w = max_stone
    while w < sum_stone // 3:
        w += stones_sort[i]
        i += 1
    print(w, stones_sort[:i] + [max_stone])
    print(sum_stone - w, stones_sort[i:-1])
