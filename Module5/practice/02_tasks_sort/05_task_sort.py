# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.
import random

def bubble_sort(nums):
    swapped = True
    j = 0
    count = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
                count += 1
        j += 1  # оптимизация алгоритмов, чтобы не проходить каждый раз полный список
    print('Количество перестановок', count)

lst_input = [random.randrange(-20, 20) for _ in range(100)]
bubble_sort(lst_input)
