# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

from random import randint

list = [randint(-100, 100) for i in range(25)]
print (list)
sum = 0
a = 5
for i in list:
    if i > a:
        sum +=i
print(f'Сумма элементов массива, больших числа ', a, '=', sum)
