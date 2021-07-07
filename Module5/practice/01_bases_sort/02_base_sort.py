# Все алгоритмы сортировки из examples/ оберните в функции

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


def bubble_sort(lst):
    swapped = True
    unsorted_border = len(lst) - 1
    while swapped:
        swapped = False
        for i in range(unsorted_border):
            if lst[i] > lst[i + 1]:
                # Меняем элементы
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        unsorted_border -= 1


def partition(lst, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = lst[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while lst[i] < pivot:
            i += 1

        j -= 1
        while lst[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        lst[i], lst[j] = lst[j], lst[i]


def quick_sort(lst):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # Индекс опорного элемента
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(lst, 0, len(lst) - 1)


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    l = []
    for i in range(size):
        l.append(random.randint(at, to))
    return l


# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков
def test_sort_method(sort_func, sort_list):
    print("Before sort:", sort_list)
    sort_func(sort_list)
    print("After sort:", sort_list)


print("Choice:")
lst = gen_list(10)
test_sort_method(sort_choice, lst)
print("Bubble:")
lst = gen_list(10)
test_sort_method(bubble_sort, lst)
print("Quick:")
lst = gen_list(10)
test_sort_method(quick_sort, lst)
