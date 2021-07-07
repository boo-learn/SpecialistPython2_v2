# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
import random

N = 10
array = [random.randint(-10, 10) for _ in range(10)]
key_value = 0
sum = 0
for element in array:
    if element > key_value:
        sum += element
print(array)
print(f"Sunn of elements greater than {key_value} is {sum}")
