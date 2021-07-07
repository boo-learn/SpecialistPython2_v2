# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.
# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.

import random

def bubble_sort(nums):
    swapped = True
    z = 1
    count=0
    while swapped:
        swapped = False
        for i in range(len(nums) - z):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count+=1
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        z += 1
    return count

def gen_list(size, at, to):
    s=[]
    for _ in range(size):
        s.append(random.randint(at,to))
    return s


sp=gen_list(20,0,10)
print ("list = ",sp)
cc=bubble_sort(sp)
print ("sort list = ",sp)

print ("count = ", cc)
