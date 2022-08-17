# Все алгоритмы сортировки из examples/ оберните в функции

def bubble_sort(nums):
    # Алгоритм
    # Сначала сравниваются первые два элемента списка.
    # Если первый элемент больше, они меняются местами.
    # Если они уже в нужном порядке, оставляем их как есть. Затем переходим к следующей паре элементов,
    # сравниваем их значения и меняем местами при необходимости.
    # Этот процесс продолжается до последней пары элементов в списке.

    # nums = [5, 2, 1, 8, 4]
    print("bubble_sort, before sort = ", nums)
    swapped = True
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    print("bubble_sort, after sort = ", nums)


def sort_choice(nums):
    from random import randint

    # Алгоритм:
    # 1. Найти наименьшее значение в списке.
    # 2. Записать его в начало списка, а первый элемент - на место, где раньше стоял наименьший.
    # 3. Снова найти наименьший элемент в списке. При этом в поиске не участвует первый элемент.
    # 4. Второй минимум поместить на второе место списка. Второй элемент при этом перемещается на освободившееся место.
    # 5. Продолжать выполнять поиск и обмен, пока не будет достигнут конец списка.

    # nums = [5, 2, -1, 8, 4, -4, 7]
    print("sort_choice, before sort = ", nums)
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
    print("sort_choice, after sort = ", nums)


def quick_sort(nums):
    # Алгоритм:
    # 1. Выбор опорного элемента из массива.
    # 2. Перераспределение элементов в массиве таким образом, что элементы меньше опорного помещаются перед ним,
    # а больше или равные — после.
    # 3. Рекурсивное применение первых двух шагов к двум подмассивам слева и справа от опорного элемента.
    # Рекурсия не применяется к массиву, в котором только один или отсутствуют элементы.

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

    print("quick_sort, after sort = ", nums)


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    res = []

    for i in range(1,size):
        res.append(random.randint(at,to))

    return res

# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков

nums = gen_list(7, -4, 8)
print(nums)
# nums = [5, 2, -1, 8, 4, -4, 7]
sort_choice(nums)
# nums = [5, 2, -1, 8, 4, -4, 7]
bubble_sort(nums)
# nums = [5, 2, -1, 8, 4, -4, 7]
quick_sort(nums)
