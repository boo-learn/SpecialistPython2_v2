# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = 2  # Задайте самостоятельно, выбрав произвольное число
b = 10  # Задайте самостоятельно, выбрав произвольное число

def sum_elements(nums):
    search_sum = 0
    for i in range(len(nums)):
        if a < nums[i] < b:
            search_sum += nums[i]
    return search_sum

print(sum_elements(numbers))
