# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
import random


def bubble_sort(lst):
    swapped = True
    unsorted_border = len(lst) - 1
    count = 0
    while swapped:
        swapped = False
        for i in range(unsorted_border):
            count += 1
            if lst[i] > lst[i + 1]:
                # Меняем элементы
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        unsorted_border -= 1


N = 30
array = [random.randint(-20, 20) for _ in range(N)]
sum_max_10 = 0
bubble_sort(array)

for i in range(len(array)-10, len(array)):
    sum_max_10 += array[i]
print(array)
print(f"Sum of 10 greatest elements is {sum_max_10}")
