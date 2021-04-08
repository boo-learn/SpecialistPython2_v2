# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
import random

list_ = [random.randint(-10, 10) for _ in range(10)]

A = -5
B = 5
sum = 0
for num in list_:
    if B > num > A:
        sum += num

print('Sum =', sum)
