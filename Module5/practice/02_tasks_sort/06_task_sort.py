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
        # print("*****")
        for i in range(j):
            # print("i = ", i)
            if reverse:
                condition = key(nums[i]) < key(nums[i + 1])
            else:
                condition = key(nums[i]) > key(nums[i + 1])
            if condition:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j -= 1


nums = gen_list(20)
print(nums)
bubble_sort(nums)
print(nums)
prizers = 0
i = -1
for _ in range(3):
    prizers += 1
    while nums[i - 1] == nums[i]:
        prizers += 1
        i -= 1
    i -= 1
print(prizers)
