# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов

import random

def bubble_sort(nums):
    swapped = True
    z = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - z):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        z += 1

def gen_list(size, at, to):
    s=[]
    for _ in range(size):
        s.append(random.randint(at,to))
    return s


sp=gen_list(20,0,10)
print ("list = ",sp)
bubble_sort(sp)
sp.reverse()
print ("sort list = ",sp)

summ=0
for i in range (10):
    summ+=sp[i]

print ("summ = ", summ)
