# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
import random

def bubble_sort(nums):
    swapped = True
    j = 0
    nums_copy = nums[:]
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1  # оптимизация алгоритмов, чтобы не проходить каждый раз полный список

lst_input = [random.randrange(0, 50) for _ in range(20)]
print('Исходный список', lst_input)

bubble_sort(lst_input)
print('Отсортированный список', lst_input)

print('Сумма 10 самых больших чисел', sum(lst_input[-10:]))
