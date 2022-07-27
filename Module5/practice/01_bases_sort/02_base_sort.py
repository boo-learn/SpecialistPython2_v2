import random


def bubble_sort(data):
    max_i = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1 - max_i):
            if data[i] > data[i + 1]:
                # Меняем элементы
                data[i], data[i + 1] = data[i + 1], data[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        max_i += 1
    return data


def sort_choice(data):
    i = 0
    while i < len(data) - 1:
        m = i
        j = i + 1
        while j < len(data):
            if data[j] < data[m]:
                m = j
            j += 1
        data[i], data[m] = data[m], data[i]
        i += 1
    return data


def quick_sort(nums):
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
def gen_list(size, at, to):
    list_of_numbers = []
    i = 1
    while i <= size:
        list_of_numbers.append(random.randint(at, to))
        i += 1
    return list_of_numbers


a = gen_list(10, -1, 10)
print(a)
b = bubble_sort(a)
print(b)
c = quick_sort(a)
print(c)
d = sort_choice(a)
print(d)
