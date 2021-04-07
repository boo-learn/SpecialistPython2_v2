# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

import random
target_a = int(input('Число А: '))
count = int(input('Количество элементов списка: '))
nums = []
for _ in range(count):
    nums.append(random.randint(-100, 100))
print(nums)
result_oversum = 0
for num in nums:
    if num > target_a:
        result_oversum += num

print(f'{result_oversum=}')
