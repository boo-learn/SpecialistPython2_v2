
# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

from base_sort import sort_choice

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]

sort_choice(numbers)

print(numbers[-1:-6:-1])

sum_num = sum(numbers[-1:-6:-1])

print(sum_num)
