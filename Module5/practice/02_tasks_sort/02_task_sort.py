# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
import random

N = 10
array = [random.randint(-20, 20) for _ in range(N)]
A = 0
B = 10
sum = 0
for element in array:
    if A < element < B:
        sum += element
print(array)
print(f"Sunn of elements between {A} and {B} is {sum}")
