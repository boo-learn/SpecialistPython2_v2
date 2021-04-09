# Все алгоритмы сортировки из examples/ оберните в функции
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


@benchmark()
def sort_choice(l):
    i = 0
    while i < len(l) - 1:
        m = i
        j = i + 1
        while j < len(l):
            if l[j] < l[m]:
                m = j
            j += 1
        l[i], l[m] = l[m], l[i]
        i += 1
    return l


@benchmark()
def quick_sort(nums):
    def partition(nums, low, high):
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1
            j -= 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                return j
            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            nums[i], nums[j] = nums[j], nums[i]

        # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # Индекс опорного элемента
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    return nums


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to
    """
    return [randint(at, to) for _ in range(size)]

# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков

if __name__ == '__main__':
    l = gen_list(10000)
    print(l)
    l = sort_choice(l)
    print(l)
    l = gen_list(10000)
    print(l)
    l = bubble_sort(l)
    print(l)
    l = gen_list(10000)
    print(l)
    l = quick_sort(l)
    print(l)
