# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = 2
b = 20
summary = 0
for number in numbers:
    if a < number < b:
        summary += number

print(summary)
