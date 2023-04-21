# Все алгоритмы сортировки из examples/ оберните в функции

def bubble_sort(list_to_sort: list):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(list_to_sort) - 1 - j):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swapped = True
        j += 1
    return list_to_sort


def sort_choice(list_to_sort: list):
    i = 0
    while i < len(list_to_sort) - 1:
        m = i
        j = i + 1
        while j < len(list_to_sort):
            if list_to_sort[j] < list_to_sort[m]:
                m = j
            j += 1
        list_to_sort[i], list_to_sort[m] = list_to_sort[m], list_to_sort[i]
        i += 1


def quick_sort_alg(list_to_sort: list):
    def partition(nums, low, high):
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

    def quick_sort(nums):
        # Создадим вспомогательную функцию, которая вызывается рекурсивно
        def _quick_sort(items, low, high):
            if low < high:
                # Индекс опорного элемента
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)

    quick_sort(list_to_sort)

# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    temp_list = []
    i = 0
    while i < size:
        temp_list.append(random.randint(at, to))
        i += 1
    return temp_list

# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков

num = gen_list(20, -100, 100)
print(num)
bubble_sort(num)
print(num)

print()
num = gen_list(20, -100, 100)
print(num)
sort_choice(num)
print(num)

print()
num = gen_list(20, -100, 100)
print(num)
quick_sort_alg(num)
print(num)
