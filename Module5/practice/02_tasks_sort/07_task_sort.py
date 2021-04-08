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
import random
def gen_list(size, at=0, to=10):
    nums = []
    for _ in range(size):
        nums.append(random.randint(at, to))
    return nums


def bubble_sort(nums, key=lambda x: x, reverse=False):
    swapped = True
    j = len(nums) - 1
    while swapped:
        swapped = False
        for i in range(j):
            if reverse:
                condition = key(nums[i]) < key(nums[i + 1])
            else:
                condition = key(nums[i]) > key(nums[i + 1])
            if condition:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j -= 1

l = gen_list(6, 0, 20)
print(l)
bubble_sort(l, reverse=True)
num_check = len(l) - len(l) // 2
print(sum(l[:num_check]))
