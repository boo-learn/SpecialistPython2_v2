# Все алгоритмы сортировки из examples/ оберните в функции

def bubble_sort(nums):
    # print("before sort = ", nums)
    swapped = True
    j = 1
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

        j += 1
    pass


def sort_choice(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    pass


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


def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # Индекс опорного элемента
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    pass


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    rand_list = []

    for i in range(size):
        rand_list.append(random.randint(at, to))
    return rand_list


nums = gen_list(1000, 10, 20000)
print("before sort = ", nums)
bubble_sort(nums)
print("after sort = ", nums)
print('-' * 10)
nums = gen_list(1000, 10, 20000)
print("before sort = ", nums)
sort_choice(nums)
print("after sort = ", nums)
print('-' * 10)
nums = gen_list(1000, 10, 20000)
print("before sort = ", nums)
quick_sort(nums)
print("after sort = ", nums)

# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков
