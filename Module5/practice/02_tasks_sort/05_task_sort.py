# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.

def bubble_sort(nums):
    count = 0
    j = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - j - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    print(count)
    return nums

def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов вдиапазоне at..to 
    """
    random_list = [random.randint(at, to) for i in range(size)]
    return random_list

gen = gen_list(10)
gen_sort = bubble_sort(gen)
