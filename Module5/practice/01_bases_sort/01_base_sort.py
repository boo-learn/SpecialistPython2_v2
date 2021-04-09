# Возьмите алгоритм сортировки пузырьком из examples/bubble_sort.py
# Раскомментируйте print-ы, изучите вывод в консоли.
# Вспомнив теорию, оптимизируйте алгоритм сортировки...
from time import time
from random import randint


def benchmark(iters=1):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time()
                return_value = func(*args, **kwargs)
                end = time()
                total = total + (end - start)
            print(f'[*] Среднее время выполнения: {total / iters} секунд.')
            return return_value
        return wrapper
    return actual_decorator


@benchmark()
def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return nums


def gen_list(size, at=-100, to=100):
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to
    """
    return [randint(at, to) for _ in range(size)]


if __name__ == '__main__':
    nums = gen_list(10000)
    print(nums)
    nums = bubble_sort(nums)
    print(nums)
