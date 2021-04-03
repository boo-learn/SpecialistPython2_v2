# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.
import random


def gen_list(size, at=-100, to=100):
    nums = []
    for _ in range(size):
        nums.append(random.randint(at, to))
    return nums


def bubble_sort(nums):
    counter = 0
    swapped = True
    j = len(nums) - 1
    while swapped:
        swapped = False
        # print("*****")
        for i in range(j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                counter += 1
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j -= 1
    print ('counter:', counter)

nums = gen_list(20)
print(nums)
bubble_sort(nums)
