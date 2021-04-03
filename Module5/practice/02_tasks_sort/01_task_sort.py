# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
nums = [5, 2, 1, 8, 4]
a = 2
summa = 0
for i in range(len(nums)):
    if nums[i] > a:
        summa += nums[i]
print(summa)
