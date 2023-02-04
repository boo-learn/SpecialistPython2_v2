# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов
from base_sort import sort_choice

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]

sort_choice(numbers)

sum_number = 0

for number in numbers[-5:]:
    sum_number += number

print(sum_number)
