# Все алгоритмы сортировки из examples/ оберните в функции
from random import randint

def gen_list(size, at, to):

    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to
    """
    list = [randint(at, to) for i in range(size)]
    return list

def bubble_sort():
    print("before sort = ", a)
    swapped = True
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(a) - 1):
            # print("i = ", i)
            if a[i] > a[i + 1]:
                # Меняем элементы
                a[i], a[i + 1] = a[i + 1], a[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    print("after sort = ", a)

def sort_choice():
    print("before sort = ", b)
    i = 0
    while i < len(b) - 1:
        m = i
        j = i + 1
        while j < len(b):
            if b[j] < b[m]:
                m = j
            j += 1
        b[i], b[m] = b[m], b[i]
        i += 1
    print("after sort = ", b)

def quick_sort():
    pass

# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков
a = gen_list(25, -100, 100)
b = gen_list(25, -100, 100)

c = sort_choice()
print(c)
#
d = bubble_sort()
print(d)
