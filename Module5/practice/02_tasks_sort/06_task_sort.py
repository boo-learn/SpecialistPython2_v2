# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход: натуральное число товаров (N < 1000) и далее N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 5 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10
def gen_list(size, at=1, to=1000):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    return [random.randint(at, to) for _ in range(size)]


def bubble_sort(nums):
    swapped = True
    cnt = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - cnt):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        cnt += 1


nums = gen_list(10)
#print(nums)
bubble_sort(nums)
#print(nums)
medium = len(nums) // 2
low_price = nums[:medium]
hi_price = nums[medium:]
# можно просто просумировать hi_price или сделать итоговый список и взять срез через 1
result_list = []
for i in range(len(hi_price)):
    result_list.append(hi_price[i])
    if i < len(low_price):
        result_list.append(low_price[i])
#print(result_list)
summa = sum(result_list[::2])
print(summa)
