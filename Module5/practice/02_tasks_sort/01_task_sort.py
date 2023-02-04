# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a
from base_sort import sort_choice

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 15  # Задайте самостоятельно, выбрав произвольное число
sum = 0

sort_choice(numbers)

for number in numbers:
    if number > a:
        sum += number
print(sum)
