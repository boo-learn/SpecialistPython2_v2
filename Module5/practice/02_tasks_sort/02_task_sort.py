# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.

import random
target_a = int(input('Число А: '))
target_b = int(input('Число B: '))
count = int(input('Количество элементов списка: '))
nums = []
for _ in range(count):
    nums.append(random.randint(-100, 100))
print(nums)
result_oversum = 0
for num in nums:
    if num > target_a and num < target_b:
        result_oversum += num

print(f'{result_oversum=}')
