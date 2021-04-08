# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.

def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    return [random.randint(at, to) for _ in range(size)]


def bubble_sort(nums: list):
    count = 0
    swapped = True
    offset = 1
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - offset):

            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count += 1
                # Устанавливаем swapped в True для следующей итерации

                swapped = True
        offset += 1
    print(count)


nums = gen_list(20)

bubble_sort(nums)
