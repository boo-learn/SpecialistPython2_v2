# Все алгоритмы сортировки из examples/ оберните в функции
import random

def bubble_sort(nums:list):
    #print("before sort = ", nums)
    swapped = True
    max_index = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - max_index):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        max_index += 1
    #print("after sort = ", nums)

def sort_choice(nums:list):
    #print("before sort = ", nums)

    # В цикле переменная i хранит индекс ячейки,
    # в которую записывается минимальный элемент.
    # Сначала это будет первая ячейка.
    i = 0

    # N - 1, так как последний элемент
    # обменивать уже не надо.
    while i < len(nums) - 1:

        # ПОИСК МИНИМУМА
        # Сначала надо найти минимальное значение
        # на срезе от i до конца списка.
        # Переменная m будет хранить индекс ячейки
        # с минимальным значением.
        # Сначала предполагаем, что
        # в ячейке i содержится минимальный элемент.
        m = i
        # Поиск начинаем с ячейки следующей за i.
        j = i + 1
        # Пока не дойдем конца списка,
        while j < len(nums):
            # будем сравнивать значение ячейки j,
            # со значением ячейки m.
            if nums[j] < nums[m]:
                # Если в j значение меньше, чем в m,
                # сохраним в m номер найденного
                # на данный момент минимума.
                m = j
            # Перейдем к следующей ячейке.
            j += 1

        # ОБМЕН ЗНАЧЕНИЙ
        # В ячейку i записывается найденный минимум,
        # а значение из ячейки i переносится
        # на старое место минимума.
        nums[i], nums[m] = nums[m], nums[i]

        # ПЕРЕХОД К СЛЕДУЮЩЕЙ НЕОБРАБОТАННОЙ ЯЧЕЙКЕ
        i += 1

    # Вывод отсортированного списка
    #print("after sort = ", nums)

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

# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    #import random
    l = []
    for i in range(size):
        l.append(random.randint(at, to))
    return l

# Проверяем, что оно работает
#nums = [22, 5, 1, 18, 99, 32, 12, 18, 5]
nums = gen_list(10,-100,100)
print("before sort = ", nums)
quick_sort(nums)
print("after sort (quick_sort) = ", nums)

#nums = [22, 5, 1, 18, 99, 32, 12, 18, 5]
nums = gen_list(10,-100,100)
print("before sort = ", nums)
sort_choice(nums)
print("after sort (sort_choice) = ", nums)

#nums = [22, 5, 1, 18, 99, 32, 12, 18, 5]
nums = gen_list(10,-100,100)
print("before sort = ", nums)
bubble_sort(nums)
print("after sort (bubble_sort) = ", nums)
