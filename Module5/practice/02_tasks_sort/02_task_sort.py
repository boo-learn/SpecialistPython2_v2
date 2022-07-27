# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

import random

def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        j += 1
        for i in range(len(nums) - j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = random.randint(-10,10)
b = random.randint(-10,10)
sum_num = 0
for number in numbers:
    if a < number < b:
        sum_num +=number

print(a)
print(b)
print(sum_num)
