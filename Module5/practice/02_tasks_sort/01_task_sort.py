# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
import random

lst_input = [random.randrange(0, 50) for _ in range (10)]
print(lst_input)

sum_lst = sum([i for i in lst_input if i > 45])
print('Сумма чисел', sum_lst)
