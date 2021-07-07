# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
import random

lst_input = [random.randrange(0, 50) for _ in range(10)]
A = 20
B = 30

sum_lst = sum([i for i in lst_input if i > A and i < B])

print('исходный список ',lst_input)
print('Сумма чисел', sum_lst)
