# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.

nums = [4,7,1,7,9,1,0,34,23]
A = 3
B = 6
for num in nums:
    if A < num < B:
        count += num
