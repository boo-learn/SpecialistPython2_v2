# Все алгоритмы сортировки из examples/ оберните в функции
import random


def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                # Меняем элементы
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True


def sort_choice(lst):
    i = 0
    while i < len(lst) - 1:
        m = i
        j = i + 1
        while j < len(lst):
            if lst[j] < lst[m]:
                m = j
            j += 1
        lst[i], lst[m] = lst[m], lst[i]
        i += 1


def quick_sort(lst):
    def _partition(nums, low, high):
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
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

    def _quick_sort(items, low, high):
        if low < high:
            # Индекс опорного элемента
            split_index = _partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(lst, 0, len(lst) - 1)


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=200):
    lst = []
    for _ in range(size):
        lst.append(random.randint(at, to))
    return lst


nums = gen_list(10)
print("before sort = ", nums)
quick_sort(nums)
print("after sort = ", nums)
