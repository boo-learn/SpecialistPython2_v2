#!/usr/bin

# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.

def bubble_sort(nums):
    j = 1
    count = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count += 1
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    print(count)
    return nums

nums = [5, 2, 1, 8, 4]
nums = bubble_sort(nums)
print(nums)
