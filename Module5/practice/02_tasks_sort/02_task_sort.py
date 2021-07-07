# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.

from random import randint

list = [randint(-100, 100) for i in range(25)]
print (list)
sum = 0
a = -15
b = 25
for i in list:
    if i > a and i < b:
        sum +=i
print(f'Сумма элементов массива, больших числа', a, ',но меньших', b, '=', sum)
