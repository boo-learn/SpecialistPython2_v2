# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
from random import randint


def gen_list(size, at=-100, to=100):
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    return [randint(at, to) for _ in range(size)]


def bubble_sort(nums, key=lambda x: x, reverse=False):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 -j):
            if reverse:
                expr = key(nums[i]) < key(nums[i + 1])
            else:
                expr = key(nums[i]) > key(nums[i + 1])
            if expr:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return nums


if __name__ == '__main__':
    nums = gen_list(20)
    print(nums)
    nums = bubble_sort(nums, key=abs, reverse=True)
    print(nums)
    print(nums[:10])
    print(sum(nums[:10]))
