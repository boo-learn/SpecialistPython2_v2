# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.
from base_sort import sort_choice

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = 1  # Задайте самостоятельно, выбрав произвольное число
b = 5  # Задайте самостоятельно, выбрав произвольное число

sort_choice(numbers)

sum_num = 0
for i in range(len(numbers)):
    if numbers[i] > a and numbers[i] < b :
        sum_num += numbers[i]

print(numbers)

print(sum_num)
