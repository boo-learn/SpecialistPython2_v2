# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.

import random


def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1


random_list = [random.randint(-10, 10) for _ in range(100)]

abs_list = [abs(num) for num in random_list]

bubble_sort(abs_list)
print('Sum =', sum(abs_list[-10:]))
