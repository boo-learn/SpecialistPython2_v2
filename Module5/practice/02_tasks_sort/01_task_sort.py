# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 5 # Задайте самостоятельно, выбрав произвольное число

def sum_elements(nums):
    search_sum = 0
    for i in range(len(nums)):
        if nums[i] > a:
            search_sum += nums[i]
    return search_sum

print(sum_elements(numbers))
