# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = -3  # Задайте самостоятельно, выбрав произвольное число
b = 10  # Задайте самостоятельно, выбрав произвольное число
summa = 0
for el in numbers:
    if a < el < b:
        summa += el

print(summa)
