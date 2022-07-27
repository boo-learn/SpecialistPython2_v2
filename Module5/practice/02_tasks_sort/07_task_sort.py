# Призеры олимпиады
# По результатам олимпиады участники награждаются дипломами.
# Набравшие одинаковые  баллы  получают дипломы  одинаковой степени.
# Призером олимпиады считается участник, получивший диплом  не хуже III степени.
# По результатам олимпиады определите количество призеров.
# Вход: натуральное число участников(N < 100) и далее N натуральных# чисел – результаты участников.
# Выход: одно число – число призеров.
# Пример:
# Вход
#
# 10 1 3 4 3 5 6 7 7 6 1
# Выход
# 5

def gen_list(size, at=1, to=1000):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    return [random.randint(at, to) for _ in range(size)]


def bubble_sort(nums, reverse=False):
    swapped = True
    cnt = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - cnt):
            if reverse:
                condition = nums[i] < nums[i + 1]
            else:
                condition = nums[i] > nums[i + 1]
            if condition:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        cnt += 1


nums = gen_list(10, to=6)
print(nums)
scores = list(set(nums))
bubble_sort(scores, reverse=True)
# print(scores)
winners = list(filter(lambda x: x in scores[:3], nums))
print(len(winners))

