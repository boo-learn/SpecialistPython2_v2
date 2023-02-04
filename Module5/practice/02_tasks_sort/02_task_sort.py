# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

from base_sort import sort_choice

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = -100  # Задайте самостоятельно, выбрав произвольное число
b = -100  # Задайте самостоятельно, выбрав произвольное число
sum_number = 0

sort_choice(numbers)

for number in numbers:
    if number > a and b < number:
        sum_number += number
print(sum_number)
